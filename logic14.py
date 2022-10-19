def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    x=a%10
    y=a//10
    if (x+y)%2==1:
        return True
    else:
        return False
print(main(33))