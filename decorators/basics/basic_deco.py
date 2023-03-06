# Basic Decorator Intro

access_level = "not-admin"


# Base Function
def get_access():
    return "Access Granted!"


# Decorator, will alter or complement the Base Function actions
def verify_access(func):
    def secure_access():
        if access_level == "admin":
            return func()
        else:
            return f"You're not an administrator"
    return secure_access


# This redefines the base function using the decorator on it.
get_access = verify_access(get_access)

# Calls the new function definition
result = get_access()

# Prints the result
print(result)
