i = 1
while i <= 9:
    j = 1
    while j < i + 1:
        # print(str(j + 1) + " * " + str(i + 1) + " = " + str((j+1) * (i+1)), end="\t")
        print("%d * %d = %d" %(j, i, j * i), end="\t")
        j = j + 1
    print()
    i = i + 1