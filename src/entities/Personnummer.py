from datetime import datetime
from src.util.luhnsAlgorithm import luhnsAlgorithm
from src.util.validPatterns import personnummerPattern as validPatterns
import re


class Personnummer:
    def __init__(self, pn):
        assert (self.isValid(pn))
        self.pn = pn

    def isValid(self, pn):
        try:
            self.checkFormat(pn)
            processedPn = self.standardizeNumber(pn)
            self.checkDate(processedPn)
            self.checkLastNumber(processedPn)
            return True
        except Exception as err:
            raise err

    def checkFormat(self, pn):
        for value in validPatterns().values():
            if re.match(value, pn):
                return True
        raise Exception("ERROR: Input value \"{}\" has an invalid format".format(pn))

    def standardizeNumber(self, pn):

        pnYear = int(pn[:2])  # of format YY
        currentYear = int(str(datetime.now().year)[2:])  # of format YY

        if "+" in pn:
            pn = pn.replace("+", "")
            if pnYear > currentYear:
                pn = "18" + pn
            else:
                pn = "19" + pn

        elif "-" in pn:
            pn = pn.replace("-", "")
            if len(pn) == 10 and pnYear < currentYear:
                pn = "20" + pn
            elif len(pn) == 10:
                pn = "19" + pn

        else:
            if len(pn) == 10 and pnYear > currentYear:
                pn = "19" + pn
            elif len(pn) == 10 and pnYear < currentYear:
                pn = "20" + pn

        return pn

    def checkDate(self, pn):
        try:
            date = pn[:8]
            datetime.strptime(date, '%Y%m%d')
            return True
        except:
            raise Exception("ERROR: Input value \"{}\" has an invalid date".format(pn))

    def checkLastNumber(self, pn):
        if luhnsAlgorithm(pn) == int(pn[-1]):
            return True
        raise Exception("ERROR: Input value \"{}\" has an invalid last digit".format(pn))
