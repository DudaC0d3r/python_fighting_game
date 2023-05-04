listanum = []
mai = 0
men = 0
for num in range(0, 5):
    listanum.append(int(input(f"Digite um valor para a posição {num}: ")))
    if num == 0:
        mai = men = listanum[num]
    else:
        if listanum[num] > mai:
            mai = listanum[num]
        if listanum[num] < men:
            men = listanum[num]
print("=-" * 30)
print(f"Vc digitou os valores{listanum} ")
print(f"O maior valor digitado foi  {mai} nas posições ", end="")
for i, v in enumerate(listanum):
    if v == mai:
        print(f"{i}...", end="")
print()
print(f"O menor valor digitado foi {men} nas posições ", end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f"{i}...", end="")
print()