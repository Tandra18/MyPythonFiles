def try_recursion(k):
    if(k > 0):
        result = k + try_recursion(k-1)
        print(result)
    else :
        return 0
    return result
print("\n\nRecursion example result ")
try_recursion(5)

# Step-by-Step Execution with try_recursion(5)
#
# Let's see how the function works when called with k = 5:
#
#     First Call: try_recursion(5)
#         k > 0 is True, so it makes the recursive call try_recursion(4).
#
#     Second Call: try_recursion(4)
#         k > 0 is True, so it makes the recursive call try_recursion(3).
#
#     Third Call: try_recursion(3)
#         k > 0 is True, so it makes the recursive call try_recursion(2).
#
#     Fourth Call: try_recursion(2)
#         k > 0 is True, so it makes the recursive call try_recursion(1).
#
#     Fifth Call: try_recursion(1)
#         k > 0 is True, so it makes the recursive call try_recursion(0).
#
#     Sixth Call: try_recursion(0)
#         k > 0 is False, so it returns 0.
#
# Unwinding the Recursive Calls
#
# Now the recursion starts to unwind, and we go back up the call stack:
#
#     Return to Fifth Call: try_recursion(1)
#         The result of try_recursion(0) is 0.
#         result = 1 + 0 which is 1.
#         It prints 1.
#         It returns 1.
#
#     Return to Fourth Call: try_recursion(2)
#         The result of try_recursion(1) is 1.
#         result = 2 + 1 which is 3.
#         It prints 3.
#         It returns 3.
#
#     Return to Third Call: try_recursion(3)
#         The result of try_recursion(2) is 3.
#         result = 3 + 3 which is 6.
#         It prints 6.
#         It returns 6.
#
#     Return to Second Call: try_recursion(4)
#         The result of try_recursion(3) is 6.
#         result = 4 + 6 which is 10.
#         It prints 10.
#         It returns 10.
#
#     Return to First Call: try_recursion(5)
#         The result of try_recursion(4) is 10.
#         result = 5 + 10 which is 15.
#         It prints 15.
#         It returns 15.