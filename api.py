from flask import Flask
from flask_restful import Resource,Api,reqparse
import pandas
import ast

app = Flask(__name__)
api = Api(app)

#/users

users_path = 'data/users.csv'
#/locations

class Users(Resource):
    def get(self):



class Locations(Resource):
    pass

#api.com/users
api.add_resource(Users,'/users')
api.add_resource(Locations,'/locations')


if __name__ == "__main__":
    app.run()