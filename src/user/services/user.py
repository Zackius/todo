from flask import request
from flask_restful import Resource
from src.utils.required_data import validating_required_inputs_for_each_services


class RegisterUser(Resource):
    "Register a user"
    def post(self):
        incoming_data = request.get_json()
        input_fileds = ["full_name", "user_name", "email", "password"]
        input_required = validating_required_inputs_for_each_services(input_fileds, incoming_data)

        if input_required:
            full_name = incoming_data('full_name')
            user_name = incoming_data('user_name')
            email = incoming_data('email')
            


