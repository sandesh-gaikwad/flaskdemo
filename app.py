from flask import Flask

app = Flask(__name__)

#from api import *

if __name__ == '__main__':
    from api import *
    app.run(debug=True)

