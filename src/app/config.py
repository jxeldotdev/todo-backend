from os import getenv
class TodoAppConfig:

    # Default configuration
    ALLOWED_ORGINS = [
        "http://localhost",
        "http://localhost:8080",
        "http://localhost:8000"
    ]

    POSTGRES_USER = ""
    POSTGRES_PASS = ""
    POSTGRES_HOST = ""
    POSTGRES_DB = ""
    POSTGRES_USE_TLS = False
    DB_URL = ""
    LOG_LEVEL = ""
    APP_TITLE = "Todo Rest API"

    def __init__(self) -> None:
        self.POSTGRES_DB = getenv('POSTGRES_DB')
        self.POSTGRES_HOST = getenv('POSTGRES_HOST')
        self.POSTGRES_PASS = getenv('POSTGRES_PASSWORD')
        self.POSTGRES_USER = getenv('POSTGRES_USER')

        self.DB_URL = "postgresql://{}:{}@{}/{}".format(
            self.POSTGRES_USER,
            self.POSTGRES_PASS,
            self.POSTGRES_HOST,
            self.POSTGRES_DB
        )

        if getenv('ALLOWED_ORIGINS') is not None:
            self.ALLOWED_ORGINS = getenv('ALLOWED_ORIGINS')