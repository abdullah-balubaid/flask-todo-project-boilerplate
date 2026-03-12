from flask import Flask
from flask_cors import CORS
import config
import crud

app = Flask(__name__)

# Load configuration
app.config['SECRET_KEY'] = config.SECRET_KEY
CORS(app)

# Register routes
@app.route('/')
def index():
    return "Hello from Flask!"

@app.route('/todosCreate',methods=["[POST]"])
def create_todo():
    # create
    return {}

@app.route('/todosRead', methods=["GET"])
def read_todo():
    # read
    return {}

@app.route('/todosUpdate', methods=["PUT"])
def update_todo():
    # update
    return {}

@app.route('/todosDelete', methods=["DELETE"])
def delete_todo():
    # delete
    return {}



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
