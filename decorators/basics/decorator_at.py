import functools

# Basic Decorator Intro

access_level = "admin"


# Decorator, will alter or complement the Base Function actions
def verify_access(func):
    # Replacing Function that takes over the function received by the decorator
    @functools.wraps(func)
    def secure_access():
        if access_level == "admin":
            return func()
        else:
            return f"You're not an administrator"
    return secure_access


# Base Function
# Normally it would lose its real name and documentation, to prevent that we
# implement the functools library (take a look on the replacing function)
@verify_access
def get_access():
    return "Access Granted!"


# # This redefines the base function using the decorator on it.
# get_access = verify_access(get_access)
# NOTICE THIS: The substitution on the previous line is not needed anymore
# because the @ symbol makes it in just one go, works the same!

# Calls the new function definition
result = get_access()

# Prints the result
print(result)
print(get_access.__name__)
