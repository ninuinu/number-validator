import sys
from pathlib import Path
sys.path.insert(0, str(Path.cwd().parent))


from entities.Personnummer import Personnummer
from entities.Samordningsnummer import Samordningsnummer
from entities.Organisationsnummer import Organisationsnummer


LOGGING = True

def numberValidatorA():
    index=0
    for i in sys.argv:
        if index != 0:
            initial = "> \"{}\" is ".format(i)
            try:
                Personnummer(i)
                print(initial + "a valid personnummer")
            except Exception as err:
                print(initial + " not a valid personnummer due to the following error:")
                print(err)
            print("\n")
            try:
                Samordningsnummer(i)
                print(initial + "a valid samordningsnummer")
            except Exception as err:
                print(initial + " not a valid samordningsnummer due to the following error:")
                print(err)
            print("\n")
            try:
                Organisationsnummer(i)
                print(initial + "a valid organisationsnummer")
            except Exception as err:
                print(initial + " not a valid organisationsnummer due to the following error:")
                print(err)
            print("\n")

        index += 1

def numberValidatorB(i):
    try:
        Personnummer(i)
    except Exception as err:
        print(err)


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
            "189912299816",
            "9606109503",
            "0510054422"]


    test_personnummer_incorrect = [
        "",
        "abme-3251",
        "929302-12312",
        "960610-9502",
        "-9605039503",
        "19960610+9503",
        "0000100000"
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

    test_random=[
        "141206-2380",
        "201701702384",
        "16556601-6399"
    ]

    numberValidatorA()

if __name__ == "__main__":

    test()
