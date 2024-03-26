from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import time

app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://web_api:password@localhost/myapp_db'

db = SQLAlchemy(app)

class LogEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    time = db.Column(db.Time)

print("SLDKFJLDSJ\n\n\n\n\n")

app.run()
db.create_all()
db.session.add(LogEntry(name="me", time=time.time()))
db.session.commit()
print("SLDKFJLDSJ\n\n\n\n\n")
