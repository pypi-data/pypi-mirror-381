"""
Returns payload structure expected by REST API Gateway
https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-output-format
"""

from dataclasses import dataclass
import json
import logging
from pygrestqlambda.aws.lambda_function.json_transform import to_string


@dataclass
class Response:
    """
    Lambda function proxy response for REST API Gateway
    """
    status_code: int | None = 401
    headers: dict | None = None
    multi_value_headers: dict | None = None
    body: str | dict | None = None
    use_default_cors_headers: bool = False


    def get_default_cors_headers(self) -> dict:
        """
        Return default CORS headers
        """

        cors_headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "*",
            "Access-Control-Allow-Headers": "*"
        }

        return cors_headers


    def get_payload(self) -> dict:
        """
        Gets payload to send to REST API Gateway
        """

        is_json = False
        if isinstance(self.body, dict):
            is_json = True

        # Set headers
        if self.headers is None:
            self.headers = {}

        if "Content-Type" not in self.headers:
            logging.debug("No content type header set")
            if is_json:
                logging.debug("Using application/json for content-type")
                self.headers["Content-Type"] = "application/json"
            else:
                logging.debug("Using text/plain for content-type")
                self.headers["Content-Type"] = "text/plain"

        # Optionally include CORS headers
        if self.use_default_cors_headers:
            for key, value in self.get_default_cors_headers().items():
                if key not in self.headers:
                    self.headers[key] = value

        if is_json:
            logging.debug("Body is a JSON object")
            body = json.dumps(self.body, default=to_string)
        else:
            logging.debug("Body is plain text")
            body = self.body

        logging.debug("Transforming dataclass dictionary to JSON")
        data = {
            "isBase64Encoded": False,
            "statusCode": self.status_code,
            "headers": self.headers,
            "multiValueHeaders": self.multi_value_headers,
            "body": body,
        }

        return data
