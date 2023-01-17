import os

from dotenv import load_dotenv

# load .env file
load_dotenv()


class RequiredEnv:  # pylint: disable=too-many-instance-attributes
    def __init__(self):
        self.log_format = os.environ.get("LOG_FORMAT")
        if self.log_format is None:
            raise Exception("Missing environment LOG_FORMAT")

        self.grpc_port = os.environ.get("GRPC_PORT")
        if self.grpc_port is None:
            raise Exception("Missing environment GRPC_PORT")

        self.rabbitmq_host = os.environ.get("RABBITMQ_HOST")
        if self.rabbitmq_host is None:
            raise Exception("Missing environment RABBITMQ_HOST")

        self.rabbitmq_user = os.environ.get("RABBITMQ_USER")
        if self.rabbitmq_user is None:
            raise Exception("Missing environment RABBITMQ_USER")

        self.rabbitmq_password = os.environ.get("RABBITMQ_PASSWORD")
        if self.rabbitmq_password is None:
            raise Exception("Missing environment RABBITMQ_PASSWORD")

        self.rabbitmq_exchange = os.environ.get("RABBITMQ_EXCHANGE")
        if self.rabbitmq_exchange is None:
            raise Exception("Missing environment RABBITMQ_EXCHANGE")

        self.rabbitmq_url = os.environ.get("RABBITMQ_URL")
        if self.rabbitmq_url is None:
            raise Exception("Missing environment RABBITMQ_URL")

        self.api_key = os.environ.get("API_KEY")
        if self.api_key is None:
            raise Exception("Missing environment API_KEY")
        self.api_secret = os.environ.get("API_SECRET")
        if self.api_secret is None:
            raise Exception("Missing environment API_SECRET")
        self.api_user = os.environ.get("API_USER")
        if self.api_user is None:
            raise Exception("Missing environment API_USER")
