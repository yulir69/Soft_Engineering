owo = ['One','two','three']
with open ('input.txt', 'w') as f:
    for line in owo:
        f.write('\nCycle run ' + line)
    print('Готово.')
