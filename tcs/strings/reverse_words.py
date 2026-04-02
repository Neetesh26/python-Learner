# "I love TCS"
#    ↓ split
# ['I', 'love', 'TCS']
#    ↓ reverse
# ['TCS', 'love', 'I']
#    ↓ join
# "TCS love I"

def solve(s1):
    return " ".join(reversed(s1.split()))
    # return " ".join(s1.split()[::-1])
print(solve("I love TCS"))