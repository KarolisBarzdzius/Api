from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

basedir=os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///"+os.path.join(basedir, "uzduoties.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
database=SQLAlchemy(app)
marshmallow=Marshmallow(app)

# DataBase
class Preke(database.Model):
    __tablename__= "Preke"
    id = database.Column(database.Integer,primary_key=True)
    pavadinimas=database.Column("Pavadinimas",database.String)
    kaina=database.Column("Kaina",database.Float)
    kiekis=database.Column("Kiekis",database.Integer)

# Prekes Schema
class PrekesSchema(marshmallow.Schema):
    class Meta:
        fields=("id","pavadinimas",'kaina','kiekis')

prekes_schema=PrekesSchema()
prekiu_schema=PrekesSchema(many=True)


# CRUD - Create, Read, Update, Delete

# Create
@app.route("/preke", methods=['POST'])
def create():
    database.create_all()
    pavadinimas=request.json["pavadinimas"]
    kaina=request.json["kaina"]
    kiekis=request.json['kiekis']
    nauja_preke=Preke(pavadinimas=pavadinimas,kaina=kaina,kiekis=kiekis)
    database.session.add(nauja_preke)
    database.session.commit()
    return prekes_schema.jsonify(nauja_preke)

# Read
@app.route("/preke/<int:id>",methods=["GET"])
def read_one(id):
    preke=Preke.query.get(id)
    return prekes_schema.jsonify(preke)

@app.route("/preke", methods=["GET"])
def read_all():
    visos_prekes=Preke.query.all()
    prekes=prekiu_schema.dump(visos_prekes)
    return jsonify(prekes)

# Update
@app.route("/preke/<int:id>",methods=["PUT"])
def update(id):
    preke=Preke.query.get(id)
    preke.pavadinimas=request.json['pavadinimas']
    preke.kaina=request.json["kaina"]
    preke.kiekis=request.json['kiekis']
    database.session.commit()
    return prekes_schema.jsonify(preke)

# Delete
@app.route("/preke/<int:id>",methods=["DELETE"])
def delete(id):
    preke=Preke.query.get(id)
    database.session.delete(preke)
    database.session.commit()
    return prekes_schema.jsonify(preke)

#
# @app.route("/", methods=['GET', 'POST'])
# def index():
#     if (request.method == 'POST'):
#         some_json = request.get_json()
#         return jsonify({'you sent': some_json})
#     else:
#         return jsonify({'about': 'Hello World'})
#
# @app.route("/keliamieji/<int:metai>", methods=['GET'])
# def keliamieji(metai):
#     if isleap(metai):
#         return jsonify({'result': "Keliamieji"})
#     else:
#         return jsonify({'result': "NE Keliamieji"})

if __name__ == '__main__':
    app.run()
    database.create_all()