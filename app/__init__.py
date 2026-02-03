from flask import Flask

def create_app():

	app = Flask(__name__)

	@app.route('/')
	def index():
		return {"message": "Welcome to the Expense Tracker API"}

	return app