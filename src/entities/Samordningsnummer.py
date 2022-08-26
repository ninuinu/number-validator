from src.entities.Personnummer import Personnummer


class Samordningsnummer(Personnummer):
    def __init__(self, number):
        Personnummer.__init__(self, number)

    def standardizeNumber(self, pn):
        pn = Personnummer.standardizeNumber(self, pn)

        day = str(int(pn[6:-4])-60)
        if len(str(day)) == 1:
            day = "0"+str(day)

        pn = pn[:6] + day + pn[-4:]

        return pn
