from email_validator import validate_email, EmailNotValidError

def validar_email(email: str) -> bool:
    try:
        validate_email(email)
        return True
    except EmailNotValidError as e:
        print(e)
        return False

print(validar_email("humbcavbr@gmail.com")) 
print(validar_email("@gmail.com"))
print(validar_email(".humbcavbr@gmail.com")) 
print(validar_email("humbcavbr@gmail.com.")) 
print(validar_email("humbcavbr@gmail.com.br")) 
print(validar_email("humbcavbr@")) 
print(validar_email("humbcavbr_gmail.com")) 
print(validar_email("humbcavbr_1@gmail.com")) 
print(validar_email("humbcavbr123@gmail.com"))    
print(validar_email("humbcav-br@gmail.com")) 