import sys
import os
from pathlib import Path
sys.path.insert(0, str(Path.cwd().parent))

from entities.Personnummer import Personnummer
from entities.Samordningsnummer import Samordningsnummer
from entities.Organisationsnummer import Organisationsnummer

def numberValidator():
    index=0
    for i in sys.argv:
        if index != 0:
            startingString = "> \"{}\" is ".format(i)
            try:
                Personnummer(i)
                print(startingString + "a valid personnummer")
            except Exception as err:
                print(startingString + " not a valid personnummer due to the following error:")
                print(err)
            print("\n")
            try:
                Samordningsnummer(i)
                print(startingString + "a valid samordningsnummer")
            except Exception as err:
                print(startingString + " not a valid samordningsnummer due to the following error:")
                print(err)
            print("\n")
            try:
                Organisationsnummer(i)
                print(startingString + "a valid organisationsnummer")
            except Exception as err:
                print(startingString + " not a valid organisationsnummer due to the following error:")
                print(err)
            print("\n")

        index += 1

if __name__ == "__main__":
    try:
        arg1 = sys.argv[1]
    except IndexError:
        print ("Missing input arguments. Please follow the following format: " + os.path.basename(__file__) + " <arg_1> <arg_2> <arg_3> ... <arg_n>")
        sys.exit(1)
    numberValidator()
