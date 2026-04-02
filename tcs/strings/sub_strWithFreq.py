def all_chars_with_freq(s, sub):
    from collections import Counter
    
    s_count = Counter(s)
    sub_count = Counter(sub)
    
    for ch in sub_count:
        if s_count[ch] < sub_count[ch]:
            return False
    
    return True


# print(all_chars_with_freq("hello world", "lo"))  # True
print(all_chars_with_freq("hello world", "woo")) # False
print(all_chars_with_freq("listen", "silent")) # True
print(all_chars_with_freq("listen", "wlnt")) # False


# s1 = "listen"
# s2 = "silent"