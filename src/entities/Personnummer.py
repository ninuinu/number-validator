from datetime import datetime
from src.util.luhnsAlgorithm import luhnsAlgorithm
from src.util.validPatterns import personnummerPattern as validPatterns
import re

class Personnummer:
    def __init__(self, number):
        assert (self.isValid(number))
        self.number = number

    def isValid(self, pn):
        try:
            self.checkFormat(pn)
            processed_pn = self.standardizePnFormat(pn)
            self.checkDate(processed_pn)
            self.checkLastNumber(processed_pn)
            return True
        except Exception as e:
            raise e

    def checkFormat(self, pn):
        for value in validPatterns().values():
            if re.match(value, pn):
                return True
        raise Exception("ERROR: Input value \"{}\" has an invalid format".format(pn))

    def standardizePnFormat(self, pn):
        if "+" in pn:
            pn = pn.replace("+", "")
            if int(pn[:2]) > int(str(datetime.now().year)[2:]):
                pn = "18" + pn
            else:
                pn = "19" + pn

        elif "-" in pn:
            pn = pn.replace("-", "")
            if len(pn) == 10 and int(pn[:2]) < int(str(datetime.now().year)[2:]):
                pn = "20" + pn
            elif len(pn) == 10:
                pn = "19" + pn

        elif len(pn) == 10:
            pn = "19" + pn

        return pn

    def checkDate(self, pn):
        try:
            date = pn[:8]
            datetime.strptime(date, '%Y%m%d')
        except:
            raise Exception("ERROR: Input value \"{}\" Incorrect date format".format(pn))

    def checkLastNumber(self, pn):
        if luhnsAlgorithm(pn) == int(pn[-1]):
            return True
        else:
            print(luhnsAlgorithm(pn))
            raise Exception("ERROR: Input value \"{}\" has an invalid last digit".format(pn))
