
import re


class UserValidator:
    def __init__(self, data):
        if not data:
            return{
                'status': 400,
                'message' : "No data provided"
            }, 400
        self.data ={
            'full_name' : data.get('full_name'), 
            'user_name': data.get('user_name'), 
            'email' : data.get('email'),
            'password' : data.get('password'),
            'confirm_password' : data.get('confirm_password')
        }
    
    def invalid_full_name(self, name='name'):
        if (len(self.data[name]) < 3):
            return {"msg": "Name too short"}
        elif (len(self.data[name]) > 40):
            return {"msg" : "Name too long"}
        
    @staticmethod
    def invalid_username(name):
        if type(name) != str or (len(name) < 3):
            return {"msg": "Name too short"}
        elif (len(name) > 20):
            return {"msg" : "Name too long"}
        
    def invalid_email(self):
        reg_email = re.compile(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$")
        email = self.data['email']
        mismatch = not re.match(reg_email, email)
        
        if bool(email) and mismatch:
            return {
                "msg": "Invalid email"
                }, 400  
    def password_match(self):
        if self.data.get('password') != self.data.get('confirm_password'):
            return {
                "msg": "Passwords don't match!"
            }, 400      

