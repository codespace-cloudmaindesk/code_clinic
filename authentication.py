import firebase_admin
from firebase_admin import credentials, auth, firestore

class sign_up:
    auth_firebase = credentials.Certificate()
    firebase_admin.initialize_app(auth_firebase)
    db_firestore = firestore.client()

    def __init__(self):
        #Automatically takes input when object is created 
        self.first_name = ""
        self.last_name = ""
        self.email = ""
        self.password = ""

        #Call methods to collect input from the user
        self.validate_user()
    def create_user(self):
        try:
            user = auth.create_user(
                display_name = self.first_name,
                email = self.email,
                password = self.password
            )
            print(f"You have successfully logged in as {user.display_name}")
        except Exception as e :
            print(f"Error creating user: {e}")

    def validate_user(self):
        while True:
            self.first_name = input("First name: ").strip()
            if not self.first_name:
                print("Please fill out all required fields")
            elif not self.first_name.isalpha():
                print("Name should contain only letters without any whitespaces")
            else:
                break
    
        while True:
            self.email = input("Email: ").strip()
            if not self.first_name:
                print("invalid Email :")
            else:
                break

        while True:
            self.password = input("Enter your Password: ")
            if not self.password:
                print(f"Enter valid password:")
            else:
                break

user = sign_up()
user.validate_user()



