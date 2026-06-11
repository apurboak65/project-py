def shift(s, flag, n):
    if flag not in ['L', 'R'] or n > len(s):
        return -1
    
    if n == 0 or n == len(s):
        return s
    
    if flag == 'L':
        return s[n:] + s[:n]
    else:
        return s[-n:] + s[:-n]


s = input()
flag, n = input().split(',')
flag = flag.strip()
n = int(n.strip())
result = shift(s, flag, n)
print(result)