inpu = "onino"


def is_palindrome(string):

    if len(string) <= 1:
        print('get!',string[0], string[-1])
        return True

    if string[0] != string[-1]:
        print('false!!', string[0], string[-1])
        return False

    # if len(string) <= 2:
    #     return
    return is_palindrome(string[1:-1])


print(is_palindrome(inpu))
