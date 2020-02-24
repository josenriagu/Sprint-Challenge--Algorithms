'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    '''
    PSEUDOCODE

    # base case: if word is empty or has just one letter, return 0
    # if the first two letters match 'th';
        #  - increment and recurse word with index 0 sliced off
    # if condition is not met;
        #  - simply increment and recurse word with index 0 sliced off
    '''
    if len(word) < 2:
        return 0
    if word[: 2] == "th":
        return 1 + count_th(word[1:])
    else:
        return count_th(word[1:])


# def count_th_first_pass(word):
#     count = 0

#     def helper(word):
#         nonlocal count
#         # base case
#         if len(word) < 2:
#             return 0
#         # if pair matches, increment count
#         if word[: 2] == "th":
#             count += 1
#             # recurse
#             return helper(word[1:])
#         else:
#             # recurse
#             return helper(word[1:])

#     helper(word)

#     return count
