import firebase_admin
import click
from firebase_admin import credentials, auth, firestore
import datetime

class sign_up:
    """
    Initialize Firebase authentication 
    """
    auth_firebase = credentials.Certificate()
    firebase_admin.initialize_app(auth_firebase)
    db_firestore = firestore.client()

    def __init__(self,name,email,password,role,expertise=""):
        """
        Initialize the SignUp class with user details.
        """
        self.name = name 
        self.email = email
        self.password = password
        self.role = role
        self.expertise = expertise

    def register_user(self):
        """
        Register a new user using Firebase Authentication.
        """
        try:
            user = auth.create_user(
                display_name = self.name,
                email = self.email,
                password = self.password
            )
            click.echo(f"You have successfully registered as {user.display_name}")
        except Exception as e :
            click.echo(f"Error registering new user: {e}")
    # Register new user 
    @click.command()
    @click.option('--name', prompt='Enter your name', help='Name to use for signup')
    @click.option('--email', prompt='Enter your email',help='Email address to use for signup')
    @click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True, help='Set password to use for signup')
    @click.option('--role', type=click.Choice(['mentee', 'mentor']), prompt='role', help='Role to use for signup')
    @click.option("--expertise", prompt="Expertise (if mentor )", default="", help="Enter your expertise ")
    def validate_user(name, password, role, expertise):
        """
        Validate user input and register the user.
        """
        new_user = sign_up(name,password,role,expertise)
        new_user.register_user()

    #
    @click.command()
    @click.option('--username', prompt='email', help='Enter your email')
    @click.option('--password', prompt=True, hide_input=True, help='Enter your password')
    def login(self,email,password):
        """
        Attempt to login in with the provided email and password
        """
        try:
            user = auth.sign_in_with_email_and_password(email,password)  
            click.echo(f"Login successful! Welcome, {self.email}")       
            return user
        except Exception as e:
            click.echo(f"Error: Incorrect password or email: {e}")
            return None

    @click.group()
    def cli():
        """
         CLI group to add commands.
        """
        pass


    # Add the validate_user command to the CLI group
    cli.add_command(validate_user)
    

# if __name__ == "__main__":
#     


