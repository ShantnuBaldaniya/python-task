class Application(Exception):
    pass

class NumberValidation(Application):
    pass

class MailValidation(Application):
    pass

class DateValidation(Application):
    pass


def validate_number(num):
    if not num.isdigit() or len(num) != 10:
        raise NumberValidation('enter a correct 10-digit number')
    return 'number ok'


def validate_email(mail):
    if "@" not in mail or "." not in mail:
        raise MailValidation(' enter a correct email')
    return 'email ok'


def validate_date(d):
    parts = d.split("-")
    if len(parts) != 3:
        raise DateValidation('enter date format')
    return 'date ok'


def check_all(num, mail, d):
    validate_number(num)
    validate_email(mail)
    validate_date(d)
    return 'all data are valid'


try:
    num = input('enter the number: ')
    mail = input('enter the email address: ')
    d = input('enter your birth: ')

    result = check_all(num, mail, d)
    print(result)

except Application as e:
    print("Validation Error:", e)
