from src.util.luhnsAlgorithm import luhnsAlgorithm
from src.util.validPatterns import orgnummerPattern as validPatterns
import re


class Organisationsnummer:
    def __init__(self, number):
        assert (self.isValid(number))
        self.number = number

    def isValid(self, orgNum):
        try:
            self.checkFormat(orgNum)
            processedOrgNum = self.standardizeOrgNumberFormat(orgNum)
            self.checkThirdDigit(processedOrgNum)
            self.checkLastNumber(processedOrgNum)
            return True
        except Exception as err:
            raise err

    def checkFormat(self, orgNum):
        for value in validPatterns().values():
            if re.match(value, orgNum):
                return True
        raise Exception("ERROR: Input value \"{}\" has an invalid format".format(orgNum))

    def standardizeOrgNumberFormat(self, orgNum):
        orgNum = orgNum.replace("-", "")
        if len(orgNum) == 12:
            orgNum = orgNum[2:]
        return orgNum

    def checkThirdDigit(self, orgNum):
        thirdDigit = int(orgNum[2])
        if thirdDigit >= 2:
            return True
        raise Exception("ERROR: Input value \"{}\" has an invalid third digit".format(orgNum))

    def checkLastNumber(self, orgNum):
        if luhnsAlgorithm(orgNum) == int(orgNum[-1]):
            return True
        raise Exception("ERROR: Input value \"{}\" has an invalid last digit".format(orgNum))
