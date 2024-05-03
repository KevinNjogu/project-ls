from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///serviceprices.db'
db=SQLAlchemy(app)
app.app_context().push()


class Burial(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=150), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    
    def __repr__(self):
        return f'{self.name}'


class Cremation(db.Model):
    id=db.Column(db.Integer(), primary_key=True)
    name=db.Column(db.String(length=150), nullable=False, unique=True)
    price=db.Column(db.Integer(), nullable=False)
    
    def __repr__(self):
        return f'{self.name}'


class Transport(db.Model):
    id=db.Column(db.Integer(), primary_key=True)
    name=db.Column(db.String(length=150), nullable=False, unique=True)
    price=db.Column(db.Integer(), nullable=False)
    
    def __repr__(self):
        return f'{self.name}'


class Advice(db.Model):
    id=db.Column(db.Integer(), primary_key=True)
    name=db.Column(db.String(length=150), nullable=False, unique=True)
    price=db.Column(db.Integer(), nullable=False)
    
    def __repr__(self):
        return f'{self.name}'


@app.route("/")
@app.route("/about")
def about_page():
    return render_template('about.html')


@app.route('/services')
def services_page():
    return render_template('our_services.html')


@app.route('/prices')
def prices_page():
    burial=Burial.query.all()  
    cremation=Cremation.query.all()
    transport=Transport.query.all()
    advice=Advice.query.all()
    return render_template('prices.html', burial=burial, cremation=cremation, transport=transport, advice=advice) 


