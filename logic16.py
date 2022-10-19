def main(a):
    """
    Given integer a,  check the following statement "The integer is a five-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    if (a>=10000 and a<=99999) or (a<=-10000 and a>=-99999):
        return True
    else:
        return False
print(main(-23445))