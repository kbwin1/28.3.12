"""Flask app for Cupcakes"""

from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import db, connect_db, Cupcake
import requests




app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:pepe1@localhost/cupcake_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] ='lolo'

connect_db(app)
app.app_context().push()

@app.route('/')
def Show_cupcakes():
    cupcakes=Cupcake.query.all()
    return render_template('index.html',cupcakes=cupcakes)


@app.route('/api/cupcakes')
def list_cupcakes():
    all_cupcakes=[cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=all_cupcakes)


@app.route('/api/cupcakes/<int:id>')
def get_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=cupcake.serialize())
    
    
@app.route('/api/cupcakes',methods=['POST'])
def create_cupcake():
    new_cupcake= Cupcake(flavor=request.json['flavor'],size=request.json['size'],rating=request.json['rating'],image=request.json['image']) 
    db.session.add(new_cupcake)
    db.session.commit()
    response_json = jsonify(cupcake=new_cupcake.serialize())
    return (response_json,201)


@app.route('/api/cupcakes/<int:id>',methods=['PATCH'])
def update_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    request.json
    cupcake.flavor = request.json.get('flavor',cupcake.flavor)
    cupcake.size = request.json.get('size',cupcake.size)
    cupcake.rating = request.json.get('rating',cupcake.rating)
    cupcake.image = request.json.get('image',cupcake.image)
    db.session.commit()
    return jsonify(cupcake=cupcake.serialize())


@app.route('/api/cupcakes/<int:id>',methods=['DELETE'])
def delete_cupcake(id):
   cupcake = Cupcake.query.get_or_404(id)
   db.session.delete(cupcake)
   db.session.commit()
   return jsonify(message='deleted')