str = "Neetesh"

def pali(a):
    a = list(a)
    left = 0
    right = len(a)-1
    while(left < right):
        temp = a[left]
        a[left] = a[right]
        a[right] = temp
        left+=1
        right-=1
    return ''.join(a)

print(pali(str))    