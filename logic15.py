def main(a):
    """
    Given a three-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    x=a%10
    y=a%100//10
    z=a//100
    if (x+y+z)%2==1:
        return True
    else:
        return False
print(main(335))