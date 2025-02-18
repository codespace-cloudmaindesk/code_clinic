import firebase_admin
from firebase_admin import credentials, auth, firestore

class sign_up:
    auth_firebase = credentials.Cerficate()
    firebase_admin.initialize_app(auth_firebase)
    db_firestore = firestore.client()

    def __init__(self,name,surname,email,password):
        self.first_name = name
        self.last_name = surname
        self.email = email
        self.password = password

    def validate_user(self):
        while True:
            self.first_name = input("First name: ").strip()
            if not self.first_name:
                print("invalid name : First name cannot be empty.")
            elif not self.first_name.isalpha():
                print("Name should contain only letters without any whitespaces")
            else:
                break
        print("\nSign up successful!")
        print(f"{self.first_name} {self.last_name}")
        print(f"Email: {self.email}")

user = sign_up("","","","")
user.validate_user()



