

def luhnsAlgorithm(num):
    try:
        num = num[:-1]
        resulting_sum = 0

        for index, value in enumerate(num):

            if index % 2 == 0:
                temp_res = int(value) * 2
                if temp_res < 10:
                    resulting_sum += temp_res
                else:
                    for digit in str(temp_res):
                        resulting_sum += int(digit)
            else:
                resulting_sum += int(value) * 1

        if resulting_sum % 10 == 0:
            return 0
        else:
            return (10 - (resulting_sum % 10)) % 10

    except Exception as e:
        print("ERROR")
        print(e)


