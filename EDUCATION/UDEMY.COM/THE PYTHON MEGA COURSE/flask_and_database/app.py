# coding=utf-8

from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy import func

app = Flask(__name__)
local_database = 'postgresql://postgres:postgres123@localhost/height_collector'
DATABASE_URL = "postgres://hsqgywkpisoodo:13f1328f335e64df1ca6bc604cf2d393d5e21a2f5a3cd427bce570db278ca680@ec2-107-22-162-158.compute-1.amazonaws.com:5432/dkhtoandp6ujc?sslmode=require"
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
db = SQLAlchemy(app)

class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    height = db.Column(db.Integer)

    def __init__(self, email, height):
        self.email = email
        self.height = height

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/success", methods=['POST'])
def success():
    if request.method == 'POST':
        email = request.form["email_name"]
        height = request.form["height_name"]
        if db.session.query(Data).filter(Data.email == email).count() == 0:
            data = Data(email, height)
            db.session.add(data)
            db.session.commit()
            average_height = db.session.query(func.avg(Data.height)).scalar()
            average_height = round(average_height)
            count = db.session.query(Data.height).count()
            send_email(email, height, average_height, count)
            return render_template("success.html")
    return render_template("index.html",
                           text="Sorry, email address already in use.")


if __name__ == "__main__":
    app.debug = True
    app.run()
