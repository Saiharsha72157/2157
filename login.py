
def login(username, password):
    correct_username = "user"
    correct_password = "password"
    
    if username == correct_username and password == correct_password:
        return "Login successful!"
    else:
        return "Invalid username or password."
