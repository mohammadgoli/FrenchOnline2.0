# _*_ coding: utf-8 _*_
from project import db
from project.models import User, Post



import os
import datetime 
from khayyam import JalaliDate


db.create_all()

#db.session.add(Question('mohmmad', 'asdf@asf.ss', 'salam'))
#db.session.add(User('mohmmad', '1a2b3F', '9039639690', 112,2017, 17, False, 0))
for i in range(1,5):
    db.session.add(Post(u'تست {}'.format(i) , u'این یک تست برای{}'.format(i) , '/sample.jpg', JalaliDate.today().strftime('%A %d %B %Y'), u'تست متن سات این یک تست متن است', u'محمد گلی', 55))
db.session.commit()
