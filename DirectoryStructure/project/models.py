from project import db

import datetime 
import os

# class TABLENAME(db.Model):

# 	__tablename__ = TABLENAME


# 	column = db.Column(db.COLUMNTYPE, primary_key=True, nullable=False, default=datetime.datetime.utcnow(), db.ForeinKey(''))
#              db.relationship('TABLENAMEP', backref='name')
# 	def __init__(self, CLUMNNAMES)
# 	    self.COLUMNNAME  = COLUMNNAME


# 	def __repr__(self):
# 		return ''.format(self.)

class User(db.Model):
	__tablename__ = 'users'

	user_id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)
	# username = db.Column(db.Integer, nullable=False) 
	# THis shit is obsolete and I don't wana be foolish :| or fool or whatever :| 
	password = db.Column(db.Integer, default=os.urandom(6))
	picture = db.Column(db.String, default="/sample.jpg")
	tele_number = db.Column(db.String, nullable=False)
	class_name = db.Column(db.Integer, nullable=False)
	date = db.Column(db.Integer, default=datetime.datetime.now())
	year = db.Column(db.Integer, default=datetime.datetime.now().year)
	payment_verify = db.Column(db.Boolean, default=False)
	payment_id = db.Column(db.Integer, default = 0)

	def __init__(self, name=None, password=None, tele_number=None, class_name=None, date=None, year=None, payment_verify=None, payment_id=None):
		self.name = name
		# self.username = username
		self.password = password
		self.tele_number = tele_number
		self.class_name = class_name
		self.date = date
		self.year = year
		self.payment_verify = payment_verify
		self.payment_id = payment_id

	def __repr__(self):
		return '<U{}:{}>'.format(self.tele_number, self.class_name)

class Post(db.Model):
	__tablename__ = 'blog_posts'

	post_id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String, nullable=False)
	subtitle = db.Column(db.String)
	cover_path = db.Column(db.String)
	date = db.Column(db.Integer, default=datetime.datetime.today().strftime('%d, %b, %Y'))
	body = db.Column(db.String, nullable=False)
	author = db.Column(db.String, nullable=False)
	# comments = db.relationship('Comment', backref='post')
	views = db.Column(db.Integer, default=0)

	def __init__(self, title, subtitle, cover_path, date, body, author, views):
		self.title = title
		self.subtitle = subtitle
		self.cover_path = cover_path
		self.date = date
		self.body = body 
		self.author = author
		self.views = views

	def __repr__(self):
		return '<title {0}>'.format(self.title)



# class Comment(db.Model):
#  	__tablename__ = 'comments'

#  	comment_id = db.Column(db.Integer, primary_key=True)
#  	comment = db.Column(db.String, nullable=False)
#  	phone_number = db.Column(db.)





# class files(db.Model):
# 	__tablename__ = uploads

# 	upload_id = db.Column(db.Integer, primary_key=True)
# 	path = db.Column(db.String, nullable=False)
# 	uploader = db.Column(db.String, nullable=False)
# 	category = db.Column(db.String, nullable=False)
# 	date = db.Column(db.String, default=datetime.datetime.now())
	
# 	