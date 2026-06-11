line = input().strip()
line = line.replace(',', ' ').replace('(', '').replace(')', '')
n, m = map(int, line.split())

count = 0

for f in range(1, m + 1):
    if m % f == 0:
        min_a = max(1, f - n)
        max_a = (f - 1) // 2
        
        if min_a <= max_a:
            count += max_a - min_a + 1

print(count)