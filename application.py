from flask import Flask, request
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)
app.app_context().push()

class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(150))

    def __repr__(self):
        return f"{self.name} - {self.description}"  


@app.route('/')
def index():
    return 'Hello GB!'

@app.route('/drinks')
def drinks():
    drinks = Drink.query.all()

    output = []
    for data in drinks:
        drink_data = {'description': data.description, 'name': data.name}
        output.append(drink_data)
    return {'Drink':output}

@app.route('/drinks/<id>')
def get_drinks(id):
    drinks = Drink.query.get_or_404(id)
    return {'name':drinks.name, 'description':drinks.description}

@app.route('/drinks', methods=['POST'])
def add_drinks():
    drink = Drink(name=request.json['name'], description = request.json['description'])
    db.session.add(drink)
    db.session.commit()
    return {'id':drink.id}

@app.route('/drinks/<id>', methods=['DELETE'])
def delete(id):
    drink = Drink.query.get(id)
    if drink is None:
        return {"Error":"Not Found"}
    
    db.session.delete(drink)
    db.session.commit()
    return {"Message":"Sucessfully Delete"}

if __name__ == "__main__":        
    app.run()