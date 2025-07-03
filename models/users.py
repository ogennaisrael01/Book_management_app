from storage.save_user import save_user, load_user
import uuid

class User:
    """
        Class for user management
    """
    def __init__(self):
        self.users = load_user()
    
    def register(self):
        """
            Account can only be register by an admin
        """
        admin = input("Are you an admin? Yes/No: ").strip().lower()
        if admin != "yes": 
            print("Only admins can register an account")
            return False
        admin_name = input("What is your name, admin? ").strip().capitalize() # to keep record of the admin who register a  user

        for user in self.users:
            if user["Name"].lower() == admin_name and user["Role"] == "admin":

                print(f"Account Registration by {admin_name}")

                name = input("Enter user name: ")
                password = input("Enter user password: ").strip() 
                if len(password) < 8:
                    print("password must be 8 characters long")
                    return False
                role = input("Enter user role (admin/user): ").strip().lower() # admins can aswell create another admin 

                if role not in ["admin", "user"]:
                    print("Role must be either 'admin' or 'user'")
                    return False
                
                for user in self.users:
                    if user["Name"] == name:
                        print("User already exist. login")
                        return False
                userID = str(uuid.uuid4())    
                self.users.append({
                    "Name": name,   
                    "ID": userID,
                    "Password": password,
                    "Role": role
                })
                save_user(self.users)
                print(f"[!] User registration, success!")

                return f"{name} Registered by {admin_name}"
            else:
                print("You are not authorized to register a user.")
                return False
        return True   
