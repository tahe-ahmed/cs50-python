from sys import exit


def main():
    credit_num = get_card_num()
    validate_card(credit_num)


def get_card_num():
    try:
        while True:
            credit = input("Credit card number : ")
            if len(credit) > 0 and int(credit):
                break
    except ValueError:
        print("ValueError : Credit card must be only a number ")
        exit(1)

    return credit


def validate_card(credit_num):
    if len(credit_num) > 16 or len(credit_num) < 13:
        print('INVALID CREDIT CARD NUMBER')
        exit(0)

    credit_num_length = len(credit_num)
    sum_str = '0'
    check_sum_int = 0

    if credit_num_length % 2 == 0:
        for i in range(0, credit_num_length, 2):
            sum_str += str(2*int(credit_num[i]))
        # sum the digits after it was multiplied by 2
        for i in range(len(sum_str)):
            check_sum_int += int(sum_str[i])

        for i in range(1, credit_num_length, 2):
            check_sum_int += int(credit_num[i])

    else:
        for i in range(1, credit_num_length, 2):
            sum_str += str(2*int(credit_num[i]))
        # sum the digits after it was multiplied by 2
        for i in range(len(sum_str)):
            check_sum_int += int(sum_str[i])

        for i in range(0, credit_num_length, 2):
            check_sum_int += int(credit_num[i])

    if(check_sum_int % 10 == 0):
        first_digit = int(credit_num[0])
        second_digit = int(credit_num[1])
        if first_digit == 3 and second_digit == 4 or second_digit == 7:
            print("AMEX")
        elif first_digit == 5 and 1 <= second_digit <= 5:
            print("MASTERCARD")
        elif first_digit == 4:
            print("VISA")
        else:
            print("INVALID")
        exit(0)
    else:
        print("INVALID")
        exit(0)


if __name__ == "__main__":
    main()
