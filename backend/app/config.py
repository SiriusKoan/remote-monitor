class Config:
    pass


class Development(Config):
    ENV = "development"
    DEBUG = True


class Testing(Config):
    ENV = "TESTING"
    TESTING = True
    SERVER_NAME = "localhost"


class Production(Config):
    ENV = "production"


config = {
    "development": Development,
    "testing": Testing,
    "production": Production,
}
