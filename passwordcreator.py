import random
import string

def make_password(length=12):
    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")

    specialCharacters = string.punctuation
    upperCaseLetters = string.ascii_uppercase
    lowerCaseLetters = string.ascii_lowercase
    numbers = string.digits

    specialChar = random.choice(specialCharacters)
    upperCaseLetter = random.choice(upperCaseLetters)
    lowerCaseLetter = random.choice(lowerCaseLetters)
    number = random.choice(numbers)

    requiredChars = specialChar + upperCaseLetter + lowerCaseLetter + number
    remainingChars = ''.join(random.choices(specialCharacters + upperCaseLetters + lowerCaseLetters + numbers, k=length - 4))  # CHANGED

    fullPassword = list(requiredChars + remainingChars)
    random.shuffle(fullPassword)

    return ''.join(fullPassword)


if __name__ == "__main__":
    password_length = int(input("Enter password length: "))
    print("Generated Password:", make_password(password_length))
