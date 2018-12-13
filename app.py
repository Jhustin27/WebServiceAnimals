from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

animals = [
    {
        "id": "1",
        "name": "Gallinazo Rey",
        "class": "Ave",
        "order": "Incertae Sedis",
        "family": "Cathartidae",
        "gender": "Sarcoramphus",
        "species": "Arcoramphus papa",
        "commonName": "Zopilote rey, condor real, cuervo real"
    },
    {
       "id": "2",
        "name": "Pavon negro o Crax rubra",
        "class": "Ave",
        "order": "galliformes",
        "family": "cracidae",
        "gender": "crax",
        "species": "crax rubra",
        "commonName": "pavon negro, hocofaisan, pavon norteno" 
    },
    {
        "id": "3",
        "name": "Guacamaya Amarilla",
        "class": "Ave",
        "order": "Psittaciformes",
        "family": "Psittacidae",
        "gender": "Ara",
        "species": "Ara ararauna",
        "commonName": "Guacamaya azul o azul amarillo, papagayo o paraba azul amarillo" 
    }
]

class Animal(Resource):
    def get(self, id):
        for animal in animals:
            if(id == animal["id"]):
                return animal, 200
        return "User not found", 404

    def post(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("class")
        parser.add_argument("order")
        parser.add_argument("family")
        parser.add_argument("gender")
        parser.add_argument("species")
        parser.add_argument("commonName")
        args = parser.parse_args()

        for animal in animals:
            if(id == animal["id"]):
                return "Animal with name {} already exists".format(id), 400

        animal = {
            "id": id,
            "name": args["name"],
            "class": args["class"],
            "order": args["order"],
            "family": args["family"],
            "gender": args["gender"],
            "species": args["species"],
            "commonName": args["commonName"]
        }
        animals.append(animal)
        return animal, 201

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("id")
        parser.add_argument("class")
        parser.add_argument("order")
        parser.add_argument("family")
        parser.add_argument("gender")
        parser.add_argument("species")
        parser.add_argument("commonName")
        args = parser.parse_args()

        for animal in animals:
            if(id == animal["id"]):
                animal["class"] = args["class"]
                animal["order"] = args["order"]
                animal["family"] = args["family"]
                animal["gender"] = args["species"]
                animal["species"] = args["species"]
                animal["commonName"] = args["commonName"]
                return animal, 200
        
        animal = {
            "id": id,
            "name": args["name"],
            "class": args["class"],
            "order": args["order"],
            "family": args["family"],
            "gender": args["gender"],
            "species": args["species"],
            "commonName": args["commonName"]
        }
        animals.append(animal)
        return animal, 201

    def delete(self, name):
        global animals
        animals = [animal for animal in animals if animal["id"] != animal]
        return "{} is deleted.".format(id), 200
      
api.add_resource(Animal, "/animal/<string:id>")

app.run(debug=False)