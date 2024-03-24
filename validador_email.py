import re

def validate_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if re.match(pattern, email):
        return True
    return False

email = 'matheus.marchetti@energisa.com;matheus.marchetti@energisa.com'

print(validate_email(email))