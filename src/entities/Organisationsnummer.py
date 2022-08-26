
from datetime import datetime
from src.util.luhnsAlgorithm import luhnsAlgorithm
import re


class Organisationsnummer:
    def __init__(self, number):
        self.patterns = {
            "six_hyphen_four": "(\d{6})-(\d{4})",
            "eight_hyphen_four": "(\d{8})-(\d{4})",
            "ten_digits": "(\d{10})",
            "twelve_digits": "(\d{12})"}
        if self.isValid(number):
            self.number = number

    def isValid(self, pn):
        try:
            self.isValidFormat(pn)
            processed_orgNum = self.standardizeOrgNumberFormat(pn)
            self.isValidThirdDigit(processed_orgNum)
            self.isValidLastNumber(processed_orgNum)
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

    def standardizeOrgNumberFormat(self, orgNum):
        if orgNum:
            orgNum = orgNum.replace("-", "")
            if len(orgNum) == 12:
                orgNum = orgNum[2:]
            return orgNum

    def isValidThirdDigit(self, pn):
        thirdDigit = int(pn[2])
        return thirdDigit >= 2

    def isValidLastNumber(self, pn):
        try:
            if luhnsAlgorithm(pn) == int(pn[-1]):
                return
            else:
                print("EEEEEEEEEEERROR")
        except:
            "ERROR"