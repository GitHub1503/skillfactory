def check_palindrome(s):
    s1 = s.lower()
    s1 = s1.replace(' ', '')
    s_l = s1[::-1]
    if s1 == s_l:
        return True
    else:
        return False

print(check_palindrome('teet'))