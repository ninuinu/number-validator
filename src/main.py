from entities.Personnummer import Personnummer
from entities.Samordningsnummer import Samordningsnummer
from entities.Organisationsnummer import Organisationsnummer

def numberValidator(args):
    Personnummer(args)
    #Samordningsnummer(args)
    #Organisationsnummer(args)

def test():
    print("testing")
    test_personnummer = ["141206-2380",
            "201701102384",
            "20080903-2386",
            "7101169295",
            "198107249289",
            "19021214-9819",
            "190910199827",
            "191006089807",
            "192109099180",
            "4607137454",
            "194510168885",
            "900118+9811",
            "189102279800",
            "189912299816"]

    test_personnummer_incorrect = [
        "",
        "abme-3251",
        "929302-12312",
        "960610-9502"
    ]

    test_samordningsnummer = ["141266-2380",
            "201701702384",
            "20080963-2386",
            "7101769295",
            "900178+9811"]

    test_organisationsnummer = ["556614-3185",
            "16556601-6399",
            "262000-1111",
            "857202-7566"]


    for i in test_personnummer_incorrect:
        numberValidator(str(i))

if __name__ == "__main__":
    test()
