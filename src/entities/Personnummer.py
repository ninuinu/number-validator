from datetime import datetime
from src.util.luhnsAlgorithm import luhnsAlgorithm
import re

# TODO Add indata validity check
# TODO Create custom Error messages

class Personnummer:
    def __init__(self, number):
        self.patterns = {
            "six_plus_four": "^(\d{6})\+(\d{4})$",
            "six_hyphen_four": "^(\d{6})-(\d{4})$",
            "eight_hyphen_four": "^(\d{8})-(\d{4})$",
            "ten_digits": "^(\d{10})$",
            "twelve_digits": "^(\d{12})$"}
        if self.isValid(number):
            self.number = number

    def isValid(self, pn):

        try:
            self.isValidFormat(pn)
            processed_pn = self.standardizePnFormat(pn)
            self.isValidDate(processed_pn)
            self.isValidLastNumber(processed_pn)

            return True

        except Exception as e:
            print(e)

    def isValidFormat(self, pn):
        self.checkIfEmpty(pn)

        if 10 <= len(pn) <= 13:
            for k, v in self.patterns.items():
                if re.match(v, pn):
                    return True
            raise Exception("ERROR: The input value \"{}\" has an invalid format".format(pn))
        else:
            raise Exception("ERROR: The input value \"{}\" has an invalid format".format(pn))

    def standardizePnFormat(self, pn):
        self.checkIfEmpty(pn)

        pn = pn.replace("+", "").replace("-", "")
        pn = pn[2:] if len(pn) == 12 else pn
        return pn

    # TODO remove hardcoded date prefix
    def isValidDate(self, pn):
        self.checkIfEmpty(pn)
        try:
            date = "19" + pn[:6]
            datetime.strptime(date, '%Y%m%d')

        except Exception as e:
            print(e)

    def isValidLastNumber(self, pn):
        self.checkIfEmpty(pn)
        if luhnsAlgorithm(pn) == int(pn[-1]):
            return True
        else:
            raise Exception("ERROR: The input value \"{}\" has an invalid last digit".format(pn))

    def checkIfEmpty(self, pn):
        if not pn:
            raise Exception("ERROR: The input value \"{}\" is empty".format(pn))