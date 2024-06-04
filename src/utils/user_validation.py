
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
    