from src.util.luhnsAlgorithm import luhnsAlgorithm
from src.util.validPatterns import orgnummerPattern as validPatterns
import re


class Organisationsnummer:
    def __init__(self, number):
        assert (self.isValid(number))
        self.number = number

    def isValid(self, pn):
        try:
            self.checkFormat(pn)
            processed_orgNum = self.standardizeOrgNumberFormat(pn)
            self.checkThirdDigit(processed_orgNum)
            self.checkLastNumber(processed_orgNum)
            return True
        except Exception as err:
            raise err

    def checkFormat(self, pn):
        for value in validPatterns().values():
            if re.match(value, pn):
                return True
        raise Exception("ERROR: Input value \"{}\" has an invalid format".format(pn))

    def standardizeOrgNumberFormat(self, orgNum):
        orgNum = orgNum.replace("-", "")
        if len(orgNum) == 12:
            orgNum = orgNum[2:]
        return orgNum

    def checkThirdDigit(self, pn):
        thirdDigit = int(pn[2])
        if thirdDigit >= 2:
            return True
        else:
            raise Exception("ERROR: Input value \"{}\" has an invalid third digit".format(pn))

    def checkLastNumber(self, pn):
        if luhnsAlgorithm(pn) == int(pn[-1]):
            return True
        else:
            raise Exception("ERROR: Input value \"{}\" has an invalid last digit".format(pn))
