lis = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for n in range(0, 3):
    for c in range(0, 3):
        lis[n][c] = int(input(f"Digite um valo para [{n}, {c}]: "))
        
print('=-' * 30)
for n in range(0, 3):
    for c in range(0, 3):
        print(f"[{lis[n][c]:^5}]", end='')
    print()