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
    },
    {
       "id": "4",
        "name": "Guacamaya Bandera",
        "class": "Ave",
        "order": "Psittaciformes",
        "family": "Psittacidae",
        "gender": "ara",
        "species": "Ara ararauna",
        "commonName": "guacamaya bandera, guacamayo macao, guacamayo rojo" 
    },
    {
       "id": "5",
        "name": "Tapir",
        "class": "mammalia",
        "order": "perissodactyla",
        "family": "tapiridae",
        "gender": "tapirus",
        "species": "tapirus bairdii",
        "commonName": "tapir centroamericano, danta, anteburro, macho de monte" 
    },
    {
        "id": "6",
        "name": "Venado cola blanca",
        "class": " mammalia",
        "order": "  artiodactyla",
        "family": ": cervidae",
        "gender": " odocoileus",
        "species":" odocoileus virginiaus",
        "commonName": " Venado de cola blanca, ciervo de cola blanca, ciervo de virginia"
    },
    {
        "id": "7",
        "name": "Jaguar",
        "class": " Mammalia",
        "order": " Carnívora",
        "family": ": felidae",
        "gender": " panthera", 
        "species":" panthera onca",
        "commonName": " jaguar, Yaguar, Yaguerete Balam, Barum"
    },
    {
        "id": "8",
        "name": "Zorro cangrejero",
        "class": " mammalia",
        "order": " carnivora",
        "family": ": canidae",
        "gender": " cersocyon", 
        "species":" cerdocyon thous",
        "commonName": " zorro de monte, zorro sabanero"
    },
    {
        "id": "9",
        "name": "Nutria",
        "class": " Mammalia",
        "order": " carnívora ",
        "family": ": Mustelidae",
        "gender": " Sanguinus",
        "species":" Lontra longicaudis",
        "commonName": " nutria, lobito de río"
    },
    {
        "id": "10",
        "name": "Saino",
        "class": " Mammalia",
        "order": " artiodactyla",
        "family": ": tayassuidae",
        "gender": "  tayassu",
        "species":" tayassu tajacu",
        "commonName": " saino, pecarí de collar, jabalí"
    },
    {
        "id": "11",
        "name": " puma",
        "class": " Mammalia",
        "order": " carnivora",
        "family": " feliade",
        "gender": " puma",
        "species":" puma con color",
        "commonName": " leon  de montaña"
    },
    {
        "id": "12",
        "name": "  mono cara blanca ",
        "class": " Mammalia",
        "order": " primate",
        "family": " cedibae",
        "gender": " cebus",
        "species":" cebius capuchino",
        "commonName": " cari blanco maicero capuchino tanque manchin"
    },
    {
        "id": "13",
        "name": " mono titi panameño",
        "class": " Mammalia",
        "order": " primates",
        "family": " calitrichidae",
        "gender": " saguinus",
        "species":" saguinus geoffroyi",
        "commonName": " titi tamarindo panameño,tamarindo de nuca café, pinche de morron"
    },
    {
        "id": "14",
        "name": " Loro comun",
        "class": " aves",
        "order": " psittaciformes",
        "family": " psiittacidae",
        "gender": " Amazona",
        "species":" amazona ochrocephala",
        "commonName": " Amazonas Harinoso , Loro Harinoso, amazónico"
    },  
    {
        "id": "15",
        "name": " taira",
        "class": " Mammalia",
        "order": " carnivora",
        "family": ":  mustelidae",
        "gender": " eira",
        "species":" eira barbara",
        "commonName": " huron mayor,cabeza de viejo"
    },
    {
        "id": "16",
        "name": " tucan de pico castaño",
        "class": "  Aves",
        "order": " piciformes",
        "family": " ramphastidae",
        "gender": " ramphastos",
        "species":" ramphastos swainsonii",
        "commonName": " tucan Dio te de"
    },
    {
        "id": "17",
        "name": "  tortuga terrestre de patas rojas",
        "class": " Sauropsida",
        "order": " Testudin",
        "family": " Testudinidae",
        "gender": " chelonoidis",
        "species":" chelonoidis carbonaria",
        "commonName": "tortuga morrocoya"
    },  
    {
        "id": "18",
        "name": "  Tigrillo",
        "class": " Mammalia",
        "order": " carnivora",
        "family": " felidae",
        "gender": " leopardus",
        "species":" leopardus wiedii",
        "commonName": " gato tigre, caucel, maracaya"
    },
    {
        "id": "19",
        "name": "  gato solo",
        "class": " Mammalia",
        "order": " carnivora",
        "family": " procyonidae",
        "gender": " nasua",
        "species":" nasua narica",
        "commonName": "coati"
    },
    {
        "id": "20",
        "name": " mono araña colorado",
        "class": " Mammalia",
        "order": "  primates",
        "family": " cebidae",
        "gender": " ateles",
        "species":" ateles geoffroy",
        "commonName": "mono araña de manos negras"
    },
    {
        "id": "21",
        "name": " suirirí piquirrojo",
        "class": " aves",
        "order": " anseriformes",
        "family": " anatidae",
        "gender": " dendrocygna",
        "species":" Dendrocygna autumnalis",
        "commonName": "güichichi "
    },
    {
        "id": "22",
        "name": " guacamaya rojo",
        "class": " ave",
        "order": " psittaciforme",
        "family": " psittacidae",
        "gender": " Ara",
        "species":" Ara chloropterus",
        "commonName": " guacamayo aliverde"
    },
    {
        "id": "23",
        "name": " águila harpía",
        "class": " ave",
        "order": " accipitriforme",
        "family": " accipitriforme",
        "gender": " harpia",
        "species":" harpia harpyja",
        "commonName": " harpía mayor"
    },
    {
        "id": "24",
        "name": " capibara ronsoco",
        "class": " Mammalia",
        "order": "  rodentia",
        "family": ": caviidae",
        "gender": " hydrochoerus",
        "species":" Hydrochoerus hydrochaeris",
        "commonName": " chigüire, pancho, chigüiro"
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
