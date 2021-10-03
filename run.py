from flask import Flask
import time
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/')
def return_time():
    return_time.strftime("%Y-%m-%d%H:%M:%S",time.localtime())
    
app.run(host='0.0.0.0',
        port=8080,
        debug=True)
