# coding=utf-8

from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy import func
from werkzeug.utils import secure_filename

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
        global file
        file = request.files["file"]
        content = file.read()
        file.save(secure_filename("uploaded" + file.filename))
        with open("uploaded" + file.filename, "a") as f:
            f.write("This was added later!")
        return render_template("index.html", btn="download.html")

@app.route("/download")
def download():
    return send_file("uploaded" + file.filename,
                     attachment_filename="yourfile.csv", as_attachment=True)


if __name__ == "__main__":
    app.debug = True
    app.run()
