from app import *
import datetime

class User(db.Model):
	__tablename__ = 'users'
	__table_args__ = {'extend_existing': True}
	user_id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(12), unique=True)
	first_name = db.Column(db.String(50))
	last_name = db.Column(db.String(50))
	email = db.Column(db.String(50), unique=True)
	password = db.Column(db.String(100))
	dob = db.Column(db.DateTime)
	profile_picture = db.Column(db.Text)

	is_verified = db.Column(db.Boolean, default=False)
	last_login = db.Column(db.DateTime, default=datetime.datetime.today())


	def __repr__(self):
		return f"<User {self.username}>"

class Note(db.Model):
	__tablename__ = 'notes'
	note_id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.Text)
	date = db.Column(db.DateTime, default=datetime.datetime.today())

	writer = db.relationship('User', backref=db.backref('notes', lazy=True))
	writer_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)

	def __repr__(self):
		return f"{note_id}"