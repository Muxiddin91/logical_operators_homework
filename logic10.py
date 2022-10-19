def main(a):
    """
    Given integer a,  check the following statement "The integer is two-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    if a>=10 and a<=99:
        return True
    else:
        return False
print(main(32))