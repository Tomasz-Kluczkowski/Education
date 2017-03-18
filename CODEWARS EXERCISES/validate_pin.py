def validate_pin(pin):
    import string
    if pin not in string.digits:
        return False
    elif len(pin) != 4 and len(pin) != 6:
        return False
    else:
        return True

print(validate_pin("1234"))