def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits of the number are the same".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    x=a%10
    y=a//10
    if x==y:
        return True
    else:
        return False
print(main(88))