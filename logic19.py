def main(x):
    """
    Given an integer x, return true if x is palindrome integer.
    An integer is a palindrome when it reads the same backward as forward.

    Args:
        x(int): parameter x
    Returns:
        bool: answer
    """
    x=str(x)
    a=x[::]
    b=x[::-1]

    return a==b

print (main (1235321))