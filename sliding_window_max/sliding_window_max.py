'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


# def sliding_window_max(nums, k):
# runs in 200+ seconds (for large data test)

# max_list = []
# for i in range(len(nums)-k+1):
#     window = []
#     for j in range(k):
#         window.append(nums[j+i])
#     max_list.append(max(window))
# return max_list

# runs in 20+ seconds


# max_list = []
# window = []
# for i in range(len(nums)-k+1):
#     if i == 0:
#         window = nums[:k]
#     else:
#         window.append(nums[k+i-1])
#         window = window[1:]
#     max_list.append(max(window))
# return max_list

def sliding_window_max(nums, k):
    # runs in about 5 seconds
    max_list = []
    curr_max = nums[0]
    window = []
    for i in range(len(nums)-k+1):
        if i == 0:
            window = nums[:k]
            curr_max = max(window)
        else:
            window.append(nums[k+i-1])
            window = window[1:]
            if nums[i-1] == curr_max:
                curr_max = max(window)
            elif nums[k+i-1] > curr_max:
                curr_max = nums[k+i-1]
        max_list.append(curr_max)
    return max_list

# runs in 4 seconds

# max_list = []
# curr_max = nums[0]
# max_counter = 0
# window = []
# for i in range(len(nums)-k+1):
#     if i == 0:
#         window = nums[:k]
#         for j in range(len(window)):
#             if window[j] > curr_max:
#                 curr_max = window[j]
#                 max_counter = 1
#             elif window[j] == curr_max:
#                 max_counter += 1
#     else:
#         window.append(nums[k+i-1])
#         window = window[1:]
#         if nums[i-1] == curr_max:
#             max_counter -= 1
#             if max_counter == 0:
#                 curr_max = window[0]
#                 for j in range(len(window)-1):
#                     if window[j] > curr_max:
#                         curr_max = window[j]
#                         max_counter = 1
#                     elif window[j] == curr_max:
#                         max_counter += 1
#         if nums[k+i-1] == curr_max:
#             max_counter += 1
#         elif nums[k+i-1] > curr_max:
#             max_counter = 1
#             curr_max = nums[k+i-1]
#     max_list.append(curr_max)
# return max_list

# from eric


# def sliding_window_max(N, k):
#     current_max = max(N[:k])
#     max_list = [current_max]
#     for i in range(k, len(N)):
#         if N[i] > current_max:
#             current_max = N[i]
#         elif current_max == N[i-k]:
#             current_max = max(N[i-k+1:i+1])
#         max_list.append(current_max)
#     return max_list


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
