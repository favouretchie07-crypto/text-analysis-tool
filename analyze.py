def welcomeUser():
    print("\nWelcome to the text analysis tool, I will analyze a body of text you give me!")

# Get Username
def getUsername():
    # Print message prompting user to input user name
    usernameFromInput = input("\nTo begin, please enter your username\n")
    return usernameFromInput

#Greet the user
def greetUser(name):
print("Hello, " + name)
welcomeUser()
username = getUsername()
greetUser(username)


