from flask import Flask
import random
from models import db, Student, Faculty


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.cli.command("add-student")
def add_data():
    for i in range(1, 4):
        faculty = Faculty(
            name=f'faculty_{i}'
        )
        db.session.add(faculty)

    for i in range(0, 10):
        student = Student(
            firstname=f'firstname{i}',
            lastname=f'lastname{i}',
            gender=random.choice(['male', 'female']),
            group=random.randint(1, 5),
            id_faculty=random.randint(1, 3)
        )
        db.session.add(student)
    db.session.commit()
    print('Done')




