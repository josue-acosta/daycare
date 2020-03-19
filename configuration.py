class BaseConfig(object):
	'''Base config class'''
	SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'
	DEBUG = True
	TESTING = False
	NEW_CONFIG_VARIABLE = "my new base config variable"
	MONGODB_SETTINGS = {
        "db": "test",
        "host": "mongodb+srv://admin:adminPassword001@curriculum-edcoy.mongodb.net/test?ssl=true&ssl_cert_reqs=CERT_NONE&retryWrites=true&w=majority"
    }

class ProductionConfig(BaseConfig):
	'''Production config class'''
	DEBUG = False
	ENV = "production"
	NEW_CONFIG_VARIABLE = "my new production config variable"

class StagingConfig(BaseConfig):
	'''Staging config class'''
	DEBUG = False

class DevelopmentConfig(BaseConfig):
	'''Development config class'''
	DEBUG = True
	TESTING = True
	ENV = "development"
	NEW_CONFIG_VARIABLE = "my new development config variable"