from datetime import datetime
import re

class Personnummer:
    def __init__(self, number):
        if self.isValid(number):
            self.number = number
            self.delimiter = None
            self.pre = None
            self.post = None
            self.patterns = [
                "(\d{6})-(\d{4})"
            ]

    def isValid(self, pn):
        try:
            return self.isValidFormat(pn)
            #self.isValidYear(pn)
            #self.isValidMonth(pn)
            #self.isValidDay(pn)
            #self.isValidFodelsenummer(pn)
            #self.isValidLastDigit(pn)

        except Exception as e:
            print(e)


    def isValidFormat(self, pn):

        ## gör om detta till en switch elelr något sen
        six_hyphen_four = re.match("(\d{6})-(\d{4})", pn)
        eight_hyphen_four = re.match("(\d{8})-(\d{4})", pn)
        ten_digits = re.match("(\d{10})", pn)
        twelve_digits = re.match("(\d{12})", pn)

        # kanske bestäm en attribut på objektet här som säger vilken typ det är?

        if six_hyphen_four:
            print("{} is valid and of type six_hyphen_four".format(pn))
            return True

        if eight_hyphen_four:
            print("{} is valid and of type six_hyphen_four".format(pn))
            return True

        if ten_digits:
            print("{} is valid and of type ten_digits".format(pn))
            return True

        if twelve_digits:
            print("{} is valid and of type twelve_digits".format(pn))
            return True

        else:
            print("{} is NOT valid".format(pn))
            return False
    #
        # if "-" in pn:
        #     [pre, post] = pn.split("-")
        #     if len(pre) == 6 or 8 and len(post) == 4:
        #         self.delimiter = "-"
        #         self.pre = pre
        #         self.post = post
        #         return True
        #
        # elif "+" in pn:
        #     [pre, post] = pn.split("+")
        #     if len(pre) == 6 and len(post) == 4:
        #         self.delimiter = "+"
        #         self.pre = pre
        #         self.post = post
        #         return True
        #
        # elif len(pn) == 12 or 10:
        #     self.post = pn[:4]
        #     self.post = pn[:-4]
        #     return True

        return False


    def isValidYear(self, pn):
        if self.delimiter == "+":
            return isinstance(int(self.pre), int)

        if self.delimiter == "-":
            if len(self.pre) == 6:
                year = "19" + self.pre[:2]
                return int(year) <= datetime.now().year

        else:
            year = int(self.pre)
            return year <= datetime.now().year





