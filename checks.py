import re


def check_arguments(args):
    if len(args) != 4:
        return False
    else:
        return True


def check_date(date):
    date_pattern = "^[0-9]{4}\\-[0-9]{1,2}\\-[0-9]{1,2}$"
    if re.match(date_pattern, date):
        return True
    else:
        return False