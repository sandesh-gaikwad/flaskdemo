from flask import Flask

app = Flask(__name__)

#from api import *

if __name__ == '__main__':
    from api import *
    app.run(host='0.0.0.0', port=5000, debug=True)

