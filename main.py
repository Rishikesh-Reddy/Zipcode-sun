import sys

from checks import check_arguments, check_date
from places import Place


def main():
    if check_arguments(sys.argv):
        if check_date(sys.argv[1]):
            place = Place()
            if place.extract_apis_information(sys.argv[3], sys.argv[2], sys.argv[1]) == None:
                return
            place.display_output()
        else:
            print("Provided date is invalid")
            return
    else:
        print('[ERROR] You need to provide 3 arguments in the following order: <date> <post_code> <country_code>')
        return


if __name__ == '__main__':
    main()

