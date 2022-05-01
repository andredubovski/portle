from flask import Flask, render_template, request, url_for, redirect
from flask_socketio import SocketIO, join_room

app = Flask(__name__)
socketIO = SocketIO(app)

users = 0


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/lounge')
def chat():
    username = request.args.get('username')
    lounge_id = request.args.get('lounge_id')

    # count how many users joined and automatically assign user_id
    global users


    if username:
        users += 1
        user_id = users
        return render_template('lounge.html', username=username, user_id=user_id, lounge_id=lounge_id)
    else:
        return redirect(url_for('home'))


@socketIO.on('join_lounge')
def handle_join_lounge_event(data):
    app.logger.info("{} has joined the lounge {} with ID {}".format(data['username'], data['lounge_id'], data['user_id']))
    join_room(int(data['lounge_id']))
    socketIO.emit('join_lounge_announcement', data)

@socketIO.on('message_modified')
def handle_message_modified(data):
    app.logger.info("{} with ID {} set message to {}".format(data['username'],
                                                             data['user_id'],
                                                             data['message']))
    socketIO.emit('receive_update', data)


if __name__ == '__main__':
    socketIO.run(app, debug=True)
