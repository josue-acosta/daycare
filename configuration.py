class BaseConfig(object):
	'''Base config class'''
	SECRETE_KEY = "a secrete key"
	DEBUG = True
	TESTING = False
	NEW_CONFIG_VARIABLE = "my value"

class ProductionConfig(BaseConfig):
	'''Production config class'''
	DEBUG = False
	ENV = "production"
	NEW_CONFIG_VARIABLE = "my value"

class StagingConfig(BaseConfig):
	'''Staging config class'''
	DEBUG = False

class DevelopmentConfig(BaseConfig):
	'''Development config class'''
	DEBUG = True
	TESTING = True
	ENV = "development"
	SECRETE_KEY = "another secrete key"