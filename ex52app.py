from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template
from ex52 import plainsphere


app = Flask(__name__)


@app.route("/")
def index():
    session['room_name'] = plainsphere.START
    return redirect(url_for("game"))


@app.route("/game", methods=['GET', 'POST'])
def game():
    room_name = session.get('room_name')


    if request.method == "GET":
        if room_name:
            room = plainsphere.load_room(room_name)
            return render_template("show_room.html", room=room)
        else:
            return render_template("you_died.html")

    else:
        action = request.form.get('action')


        if room_name and action:
            room = plainsphere.load_room(room_name)
            next_room = room.go(action)

            if not next room:
                session['room name'] = plainsphere.name_room
            else:
                session['room_name'] = plainsphere.name_room

            return redirect(url_for("game"))

        app.secret_key = 'HELLO'

        if __name__ == "__main__":
            app.run()
      
