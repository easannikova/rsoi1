import os
import signal
from flask import Flask
from fib_summ import fib_summaraiser

#commit
app = Flask(__name__)

signal.signal(signal.SIGINT, lambda s, f: os._exit(0))

#commmit
@app.route("/")
def fib_summaraizer():
    page = '<html><body><h1>'
    page += fib_summaraiser.fibonachi()
    page += '</h1></body></html>'
    return page

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.getenv('PORT')) # port 5000 is the default
