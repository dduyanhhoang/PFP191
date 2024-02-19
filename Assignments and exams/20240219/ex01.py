def have_valid_length(password) -> list:
    return [6 <= len(password) <= 12, len(password)]


def contain_special(password) -> list:
    for c in password:
        if c in '$#@':
            return [True, c]
    return [False, None]


def contain_digit(password) -> list:
    for c in password:
        if '0' <= c <= '9':
            return [True, c]
    return [False, None]


def contain_upper_case(password) -> list:
    for c in password:
        if 'A' <= c <= 'Z':
            return [True, c]
    return [False, None]


def contain_lower_case(password) -> list:
    for c in password:
        if 'a' <= c <= 'z':
            return [True, c]
    return [False, None]


def get_password(prompt: str) -> dict:
    while True:
        try:
            usr_password = input(prompt)
            if not have_valid_length(usr_password)[0]:
                raise ValueError('Password must be between 6 and 12 characters long')
            elif not contain_special(usr_password)[0]:
                raise ValueError('Password must contain at least one special character')
            elif not contain_digit(usr_password)[0]:
                raise ValueError('Password must contain at least one digit')
            elif not contain_upper_case(usr_password)[0]:
                raise ValueError('Password must contain at least one uppercase letter')
            elif not contain_lower_case(usr_password)[0]:
                raise ValueError('Password must contain at least one lowercase letter')
            else:
                return {
                        "Password": usr_password, 
                        "Length": have_valid_length(usr_password)[1], 
                        "Special": contain_special(usr_password)[1], 
                        "Digit": contain_digit(usr_password)[1], 
                        "Upper": contain_upper_case(usr_password)[1], 
                        "Lower": contain_lower_case(usr_password)[1],
                        }
        except ValueError as e:
            print(e)


def main():
    password = get_password("Enter a password:")
    print(password)


if __name__ == '__main__':
    main()

