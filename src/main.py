from entities.Personnummer import Personnummer

def numberValidator(args):
    Personnummer(args)

def test():
    print("testing")
    test = ["141206-2380",
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

    for i in test:
        numberValidator(str(i))

if __name__ == "__main__":
    test()
