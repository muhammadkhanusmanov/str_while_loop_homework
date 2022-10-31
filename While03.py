def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a = """!()-[]{;:'"\,<>.}/?@#$%^&*_~"""
    n = 0
    i = 0
    j = 0
    while n<len(s):
        while j<len(a):
            if s[n]==a[j]:
                i+=1
            j+=1
        n+=1

    return i