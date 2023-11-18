from flask import Flask

testApp = Flask(__name__)

@testApp.route('/')
def index():
    return "This is the test app to check my flask is running successfully"

testApp.run(host='0.0.0.0', port=5000)