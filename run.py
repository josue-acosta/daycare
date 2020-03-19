from my_app import app

# app configurations
app.config.from_object("configuration.DevelopmentConfig")

# run settings
if __name__ == '__main__':
	app.run()