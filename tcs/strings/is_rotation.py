def solve(s1,s2):
    if len(s1) != len(s2):
        return print("both string must be equal")
    
    s3 = s1+s1
    if s2 in s3:
        return True
    else:
        return False
    


print(solve("abcd","cdab"))


def solve2():
    s1 = list(map(str, input()))
    s2 = list(map(str, input()))
    
    if len(s1) != len(s2):
        print("False")
        return
    
    # join back to string for rotation check
    s1 = "".join(s1)
    s2 = "".join(s2)
    
    print(s2 in (s1 + s1))


solve2()