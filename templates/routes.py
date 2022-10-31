
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user, current_user, login_required



@app.route('/signup', methods = ["GET", "POST"])
user = User.query.filter_by(username=username).first()
if user:
    if check_password_hash(user.password, password):
        print('successfully logged in')
        login_user(user)
        return redirect(url_for('realHomePage'))
    else:
        print('incorrect password')
else:
                print('user does not exist')
return render_template('login.html', form=form)
