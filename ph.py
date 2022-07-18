class Error(Exception):
    pass
class InvalidPhNo(Error):
    pass

resp = input("Enter your Phone Number: ")
try:
    if len(resp) != 10:
        raise InvalidPhNo
    else:
        print("Valid Phone Number")
except InvalidPhNo:
    print("The phone number should be of 10 digits")