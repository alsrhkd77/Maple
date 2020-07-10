from flask import Flask, render_template, make_response
import time, os
from firebase_admin import credentials, firestore, initialize_app

app = Flask(__name__)

# Initialize Firestore DB
cred = credentials.Certificate('maple-2ff40-firebase-adminsdk-p4ept-99ccbba79e.json')
default_app = initialize_app(cred)
db = firestore.client()
todo_ref = db.collection('todos')


def format_server_time():
    server_time = time.localtime()
    return time.strftime("%I:%M:%S %p", server_time)


@app.route('/')
def hello_world():
    context = {'server_time': format_server_time()}
    return render_template('index.html', context=context)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
