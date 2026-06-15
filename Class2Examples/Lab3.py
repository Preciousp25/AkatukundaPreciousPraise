def login_system():
    print("Welcome to the login system!")
    # Define a dictionary to store usernames and passwords
    users = {
        "admin": "12345", 
        "Technician": "password1", 
        "Farmer": "password2"}
    # Set the maximum number of login attempts
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
#check if the username exists 
        if username in users:
            if users[username] == password:
                print(f"Login successful! Welcome, {username}!")
                return True
            else:
                print("Incorrect password. Please try again.")
        else:
            print("Username not found. Please try again.")
        
        attempts += 1
        print(f"Attempt {attempts} of {max_attempts}.\n")
    print("Maximum login attempts reached. Access denied.")
    return False
login_system()
        

    