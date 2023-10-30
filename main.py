N = int(input("N: "))
P = int(input("P: "))

nArray = [int(x) for x in str(N)]
newNum = 0

newArray = []
for i in range(len(nArray)):
    newArray.append(0)


digitP = nArray[len(nArray)-P]
digitP = int(digitP)

for i in range(P):
    newNum = digitP + int(nArray[i])
    if newNum > 9:
        newArray[i] = newNum-10
    else:
        newArray[i] = newNum

newArray[P-1] = digitP

for i in range(len(nArray)-P):
    count = (i+P)
    newDigitP = nArray[count]
    difference  = newDigitP-digitP
    if difference < 0:
        difference = difference*-1
        newArray[count] = difference
    else:
        newArray[count] = difference

for i in (newArray):
    print(i, end = "")
