from flask_app import app
from flask_socketio import SocketIO, send
from flask_app.controllers import users_controller
from flask_app.controllers import scores_controller

socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('message')
def handle_message(message):
    print('Player says:' + message)
    if message != "User connected!":
        send(message, broadcast=True)

if __name__ == "__main__":
    socketio.run(app, host='localhost', port=5001)
    # app.run(debug=True, port = 5001)