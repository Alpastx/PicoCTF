# Numbers to alphabet mapping 

data = [16, 9, 3, 15, 3, 20, 6, '{', 20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14, '}']

for numb in data:
    if isinstance(numb, int):
        print(chr(numb + 96), end="")
    else:
        print(numb, end="")

print() # 