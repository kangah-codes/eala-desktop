from app import *

# create user auth apis

@app.route('/create_account', methods=['POST'])
def create_user():
	pass

@app.route('/login', methods=['POST'])
def login_user():
	pass

@app.route('/forgot_password')
def forgot_password():
	pass

@app.route('/reset_password')
def reset_password():
	pass

@app.route('/delete_account')
@login_required
def delete_account():
	pass

@app.route('/home')
@login_required
def home():
	pass

@app.route('/profile')
@login_required
def profile():
	pass

@app.route('/notes')
@login_required
def notes():
	pass

@app.route('/wiki')
@login_required
def wiki():
	pass

@app.route('/todo')
@login_required
def todo():
	pass

@app.route('/notifications')
@login_required
def notifications():
	pass

@app.login_manager.unauthorized_handler
def unauth_handler():
	return redirect('/login')

@login.user_loader
def user_loader(user_id):
    return User.query.filter_by(user_id=user_id).first()