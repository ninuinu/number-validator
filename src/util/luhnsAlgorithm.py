

def luhnsAlgorithm(ssn):
    try:
        if "+" in ssn:
            ssn = ssn.replace("+", "")
            ssn = ssn[:-1]
        elif len(ssn) == 12:
            ssn = ssn[2:-1]

        resulting_sum = 0
        print(ssn)
        for index, value in enumerate(ssn):
            print(value)
            if index % 2 == 0:
                temp_res = int(value) * 2
                if temp_res < 10:
                    resulting_sum += temp_res
                else:
                    for digit in str(temp_res):
                        resulting_sum += int(digit)
            else:
                resulting_sum += int(value) * 1

        print(resulting_sum)
        if resulting_sum % 10 == 0:
            return 0
        else:
            return (10 - (resulting_sum % 10)) % 10

    except Exception as e:
        print("ERROR")


print(luhnsAlgorithm("811218+9876"))
