from flask import request
from flask_restful import Resource
from src.utils.required_data import validating_required_inputs_for_each_services
from src.utils.user_validation import UserValidator
from src.user.models.user_model import User


class RegisterUser(Resource):
    "Register a user"
    def post(self):
        incoming_data = request.get_json()
        input_fileds = ["full_name", "user_name", "email", "password", "confirm_password"]
        input_required = validating_required_inputs_for_each_services(input_fileds, incoming_data)
        print(incoming_data, ":::::::::::::::::::::::::;;")

        if input_required:
            invalid_full_name = UserValidator(incoming_data).invalid_full_name
            invalid_user_name = UserValidator(incoming_data).invalid_username
            invalid_email = UserValidator(incoming_data).invalid_email
            invalid_password =UserValidator(incoming_data).password_match

            invalid_methods = [
                    invalid_user_name,
                    invalid_full_name,
                    invalid_email,
                    invalid_password
            ]

            for method in invalid_methods:
                if method():
                    return method()
                
            full_name = incoming_data['full_name'] 
            user_name = incoming_data['user_name']
            email = incoming_data['email']
            password = incoming_data['password']   

            user = {
                "full_name": full_name,
                "user_name": user_name,
                "email": email,
                "password": password
            }
            user_registration = User(user)
            user_registration.save()

         
    



