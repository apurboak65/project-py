def index_iter(text):
    prev_char = ' '
    for i, char in enumerate(text):
        if prev_char == ' ' and char != ' ':
            yield i
        prev_char = char


s = input()
indices = index_iter(s)
print(list(indices))
