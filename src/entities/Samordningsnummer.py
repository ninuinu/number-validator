from src.entities.Personnummer import Personnummer


class Samordningsnummer(Personnummer):
    def __init__(self, number):
        Personnummer.__init__(self, number)

    def standardizeNumber(self, sn):
        sn = Personnummer.standardizeNumber(self, sn)
        day = str(int(sn[6:-4])-60)

        if int(day) < 1:
            raise Exception("ERROR: Input value \"{}\" has an invalid date \"{}\"".format(sn, day))

        if len(str(day)) == 1:
            day = "0"+str(day)

        sn = sn[:6] + day + sn[-4:]
        return sn
