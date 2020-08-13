

'''
Input: an integer
Returns: an integer
'''


def eating_cookies(n, cache={}):
    # base case
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif n in cache:
        return cache[n]
    else:
        # 3 recursive calls
        value = eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
        cache[n] = value
        return value


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
