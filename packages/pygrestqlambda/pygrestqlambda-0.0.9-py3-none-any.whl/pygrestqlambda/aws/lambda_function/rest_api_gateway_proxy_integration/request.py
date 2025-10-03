"""
Receives payload in format sent by AWS REST API Gateway
https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format
"""

from base64 import b64decode
import json
import logging

# pylint: disable=too-many-instance-attributes
class Request:
    """
    Lambda function proxy integration request
    """

    def __init__(self, event: dict):
        self.event = event
        # Extract authorisation information
        self.cognito_uid = self.get_cognito_uid()
        # Extract headers needed for body and response
        self.accept: str | None = self.get_header('accept')
        self.content_type: str | None = self.get_header('content-type')
        # Extract resource
        self.resource = event.get('resource')
        self.method = event.get('httpMethod')
        # Extract parameters
        self.query_params = event.get('multiValueQueryStringParameters')
        self.path_params = event.get('pathParameters')
        # Extract body
        self.body = self.get_body()


    def get_body(self):
        """
        Returns body from request, decodes from base64 if necessary
        """

        body = self.event.get('body')
        content = body
        if self.event.get('isBase64Encoded'):
            if body:
                content = b64decode(body).decode('utf-8')

        # Handle no content type
        if self.content_type is None:
            return content

        # Handle plain text
        if self.content_type.lower() == 'text/plain':
            return str(content)

        # Handle JSON
        if self.content_type.lower() == 'application/json':
            if isinstance(content, str):
                return json.loads(content)

        return content


    def get_cognito_uid(self):
        """
        Retrieve Cognito UID from supplied claim
        """
        claims = self.event.get('requestContext', {}).get('authorizer', {}).get('claims')

        if claims is None:
            logging.info('No claims in event request context authoriser')
            return None

        cognito_uid = claims.get('sub')

        return cognito_uid


    def get_header(self, header_name: str) -> str | None:
        """
        Retrieve Accept header
        """

        headers = self.event.get('headers')
        if headers is None:
            return None

        # Lowercase all the headers
        headers_lower = {k.lower():v for k,v in headers.items()}

        accept = headers_lower.get(header_name.lower())

        return accept
