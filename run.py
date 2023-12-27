from flask import Flask, jsonify
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/api/hello')
def hello_world():
    return jsonify({'message': 'Hello, world!'})


@socketio.on('message')
def handle_message(data):
    print('Received message:', data)
    socketio.emit('response', {'data': 'Message received'})


if __name__ == '__main__':
    socketio.run(app, debug=True)
