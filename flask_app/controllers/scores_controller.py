from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_app.models.user import User
from flask_app.models.score import Score

@app.route('/scoreboard')
def scoreboard():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id' : session['user_id']
    }

    # Getting the scoreboard to pass into our html
    scoreboard = Score.scoreboard()

    all_users = User.get_all()
    logged_user = User.get_by_id(data)
    return render_template('scoreboard.html', logged_user=logged_user,scoreboard=scoreboard,all_users=all_users)