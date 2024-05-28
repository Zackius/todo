# from flask import request
from flask_restful import Resource


class RegisterUser(Resource):
    "Register a user"
    def post(self):
        return  print("HEllo Africa")