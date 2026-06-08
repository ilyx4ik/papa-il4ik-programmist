import sys
import string

class ValidationError(Exception): pass
class InvalidEmailError(ValidationError): pass
class PasswordTooShortError(ValidationError): pass
class PasswordMissingUppercaseError(ValidationError): pass
class PasswordMissingLowercaseError(ValidationError): pass
class PasswordMissingDigitError(ValidationError): pass
class PasswordMissingSpecialCharError(ValidationError): pass

def validate_email(email: str):
    if "@" not in email or "." not in email.split("@")[-1]:
        raise InvalidEmailError("Некоректний формат email.")

def validate_password(password: str):
    if len(password) < 15:
        raise PasswordTooShortError("Пароль має бути не менше 15 символів.")
    if not any(c.isupper() for c in password):
        raise PasswordMissingUppercaseError("Пароль повинен містити велику літеру.")
    if not any(c.islower() for c in password):
        raise PasswordMissingLowercaseError("Пароль повинен містити малу літеру.")
    if not any(c.isdigit() for c in password):
        raise PasswordMissingDigitError("Пароль повинен містити цифру.")
    if not any(c in string.punctuation for c in password):
        raise PasswordMissingSpecialCharError("Пароль повинен містити спеціальний символ.")

def main():
    try:
        email = input().strip()
        password = input().strip()
        validate_email(email)
        validate_password(password)
        print("Успішно")
    except ValidationError as e:
        print(e, file=sys.stderr)

if __name__ == "__main__":
    main()