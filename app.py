from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///teachers.db'

db = SQLAlchemy(app)


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))


@app.route('/')
def home():

    teachers = Teacher.query.all()

    text = ""

    for teacher in teachers:
        text += f"{teacher.name}<br>"

    return text


@app.route('/add/<name>')
def add(name):

    teacher = Teacher(name=name)

    db.session.add(teacher)
    db.session.commit()

    return "Teacher Added"


if __name__ == '__main__':

    with app.app_context():
        db.create_all()

    app.run(debug=True)
