import json


def save_user(user, file_name="users.json"):
    try:
        with open(file_name, "w") as file:
            json.dump(user, file, indent=4)

    except json.JSONDecodeError as e:
        print("Error saving user")

def load_user(file_name="users.json"):
    try:
    
        with open(file_name, 'r') as file:
            users = json.load(file)
            return users
        
    except json.JSONDecodeError:
        return []