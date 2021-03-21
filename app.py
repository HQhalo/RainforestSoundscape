from flask import Flask
from flask_socketio import SocketIO, emit, disconnect
from threading import Lock


async_mode = None
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socket_ = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()



@socket_.on('wake_up', namespace='/wakeup')
def test_message(message):
    print("wake up")
    print(message['data'])


if __name__ == '__main__':
    socket_.run(app, debug=True)