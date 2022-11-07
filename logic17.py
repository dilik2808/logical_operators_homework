def main(a):
    """
    Given a five-digit integer a,  check the following statement "All digits of the number are in ascending order".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    x1= a%10
    x2= a%100//10
    x3= a%1000//100
    x4= a%10000//1000
    x5= a//10000
    if x5>x4:
        if x5>x3:
            if x5>x2:
                if x5>x1:
                    return True
                else: return  False
    if x4>x3:
        if x4>x2:
            if x4>x1:
                return True
            else: return False
    if x3>x2:
        if x3>x1:
            return True
        else: return False
    if x2>x1:
        return True
    else: return False


print (main(54321))