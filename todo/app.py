from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import psycopg2


app = Flask(__name__)
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5432/todo_db"
db.init_app(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)

    def __str__(self):
        return self.title


with app.app_context():
    db.create_all()


@app.route('/', methods=["GET", "POST"])
def homepage():
    if request.method == "POST":
        data = request.form
        todo = Todo(title=data["title"])
        db.session.add(todo)
        db.session.commit()

    todos = db.session.execute(db.select(Todo)).scalars()
    return render_template("index.html", todos=todos)
