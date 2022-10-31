def main1(a,n):
    if a[n].lower()=='a' or a[n].lower()=='i' or a[n].lower()=='e' or a[n].lower()=='o' or a[n].lower()=='u':
        i = 0
    else:
        i = 1
    return i
def main(s):
    t = 0
    a = 0
    while t<len(s):
        a+=main1(s,t) 
        t+=1
    return a


