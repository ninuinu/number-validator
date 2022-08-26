# TODO Create Class

from datetime import datetime
from src.util.luhnsAlgorithm import luhnsAlgorithm
import re

class Samordningsnummer:
    def __init__(self, number):
        self.patterns = {
            "six_plus_four": "(\d{6})\+(\d{4})",
            "six_hyphen_four": "(\d{6})-(\d{4})",
            "eight_hyphen_four": "(\d{8})-(\d{4})",
            "ten_digits": "(\d{10})",
            "twelve_digits": "(\d{12})"}
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
        try:
            for k, v in self.patterns.items():
                if re.match(v, pn):
                    return True
        except:
            print("ERROR")

    def standardizePnFormat(self, pn):
        if pn:
            pn = pn.replace("+", "").replace("-", "")
            pn = pn[2:] if len(pn) == 12 else pn
            return pn

    # TODO remove hardcoded date prefix
    def isValidDate(self, pn):
    #    self.convertToRealDate(pn[4:6])

        day = int(pn[4:6])-60
        if len(str(day)) == 1:
            day = "0"+str(day)

        date = "19" + pn[:4] + str(day)
        if pn:
            try:
                datetime.strptime(date, '%Y%m%d')
                return True
            except Exception as e:
                print(e)
                print("ERROR werwre")

    def isValidLastNumber(self, pn):
        luhnsAlgorithm(pn)


    def convertToRealDate(self, pn):
        print(pn)
        date = "19" + pn[:6]