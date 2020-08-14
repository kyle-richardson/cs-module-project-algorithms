'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # first pass

    # non_zero = [x for x in arr if x != 0]
    # zero = [x for x in arr if x == 0]
    # merged = non_zero + zero
    # return merged

    # optimize attempt

    new_arr = arr[:]
    for i in new_arr:
        if i == 0:
            new_arr.remove(i)
            new_arr.append(0)
    return new_arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
