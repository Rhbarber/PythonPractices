# import getpass module
import getpass

# Take password from the user
passwd = getpass.getpass('Password:')

# Check the password
if passwd == "password":
    print("You are authenticated")
else:
    print("You are not authenticated")
