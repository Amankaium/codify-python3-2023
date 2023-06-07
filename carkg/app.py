from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5432/car_db"
db.init_app(app)


class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=True)
    price = db.Column(db.Integer, nullable=False)
    is_sold = db.Column(db.Boolean, default=False)


with app.app_context():
    db.create_all()


@app.route('/')
def homepage():
    cars = db.session.execute(db.select(Car)).scalars()  # SELECT\
    return render_template('index.html', cars=cars)


@app.route('/car/<int:id>')
def car_info(id):
    car = db.get_or_404(Car, id)  # SELECT\
    return render_template('car.html', car=car)


@app.route('/car-edit/<int:id>', methods=["GET", "POST"])
def car_edit(id):
    if request.method == "POST":
        data = request.form
        car = db.get_or_404(Car, id)
        car.name = data["name"]
        car.price = int(data["price"])
        car.year = int(data["year"])
        db.session.commit()

    car = db.get_or_404(Car, id)  # SELECT\
    return render_template('car_edit.html', car=car)

if __name__ == '__main__':
    app.run()
