def main(a):
    """
    Given a five-digit integer a,  check the following statement "All digits of the number are in ascending order".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    q=a%10
    w=a%100//10
    e=a%1000//100
    r=a%10000//1000
    t=a//10000
    if q>w>e>r>t:
        return True
    else:
        return False
print(main(24688))