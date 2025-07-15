import random


def count11(seq):
    countOf11 = 0
    i = 0
    while i < len(seq) - 1:
        if seq[i] == 1 and seq[i + 1] == 1:
            countOf11 += 1
            i += 1
        else:
            i += 1
    return countOf11
   # define this function and return the number of occurrences as a number
   
def generateCoinFlip():
    arrOfCoinFlips = []
    i = 0
    for i in range(100):
        arrOfCoinFlips.append(random.randint(0, 1))
        i += 1
    return arrOfCoinFlips

def main():
    coinFlips = generateCoinFlip()
    print("Generated Coin Flips: ", coinFlips)
    count = count11(coinFlips)
    print("Count of consecutive 1s: ", count) 

main()
