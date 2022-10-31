def main(s):
    """
    A variable of type str is given. Find how many letters it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    n = 0
    i = 0
    while n<len(s):
        if s[n].lower()!=s[n].upper():
            i+=1
        n+=1
    return i