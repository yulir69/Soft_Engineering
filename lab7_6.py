with open('input.txt', 'a+') as f:
    f.write('\n Ugh Ugh, Get out!')

with open('input.txt', 'r') as f:
    result = f.readlines()
    print(result)
