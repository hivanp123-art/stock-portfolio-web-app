class Config:
    API_KEY = 'your_api_key'
    DATABASE_URI = 'your_database_uri'
    REDIS_URL = 'your_redis_url'
    CELERY_BROKER_URL = 'your_celery_broker_url'
    MARKET_SCAN_INTERVAL = 60  # in seconds


class DevelopmentConfig(Config):
    DEBUG = True
    API_KEY = 'development_api_key'
    DATABASE_URI = 'sqlite:///development.db'


class ProductionConfig(Config):
    DEBUG = False
    API_KEY = 'production_api_key'
    DATABASE_URI = 'postgresql://user:password@localhost:5432/prod_db'


class TestingConfig(Config):
    TESTING = True
    API_KEY = 'testing_api_key'
    DATABASE_URI = 'sqlite:///testing.db'