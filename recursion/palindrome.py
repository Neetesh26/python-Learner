def isPalindrome(i, text):
    s= text.upper()
    if i >= (len(s)//2):
        return True
    
    if s[i] != s[len(s)-i-1]:
        return False
    
    return isPalindrome(i+1,s)

print(isPalindrome(0,"mADaM"))