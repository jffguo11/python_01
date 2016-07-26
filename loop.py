abc = [3, 34, 78.33, 234, 5]

deg = [3251, 1345, 68, 132509]

hij = ["captain", "super", "wonder", "iron"]

for x in abc:
    if x >= 50:
        print x
    else:
        print(str(x) + " " + "is not greater than or equal to 50")


def counter(topv):
    for x in range(1,(topv + 1)):
        print x

counter(5)