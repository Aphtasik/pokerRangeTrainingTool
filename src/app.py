import random
import matplotlib.pyplot as plt

# --- Global variables ---

ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
colors = ["h", "d", "c", "s"]
suited = ["s", "o"]
correct = 0
error = 0


def getAllPossibleHands():
    L = []
    for i in range(0, 13):
        for j in range(i, 13):
            if i == j:
                L.append(ranks[i] + ranks[j])
            else:
                for k in range(0, 2):
                    L.append(ranks[i] + ranks[j] + suited[k])


allPossibleHands = getAllPossibleHands()

# --- Functions ---


def randomHand():
    card1 = card2 = ""

    while card1 == card2:
        card1 = ranks[random.randint(0, 12)] + colors[random.randint(0, 3)]
        card2 = ranks[random.randint(0, 12)] + colors[random.randint(0, 3)]

    if card1[0] == card2[0]:
        return card1, card2, card1[0] + card2[0]
    else:
        return card1, card2, card1[0] + card2[0] + suited[random.randint(0, 1)]


def parseRange(input_string: str):
    hand_ranges = input_string.split(",")
    combinations = []
    for hand_range in hand_ranges:
        if "-" in hand_range:
            start, end = hand_range.split("-")
            start = start.strip()
            end = end.strip()

            if start[0] == start[1]:
                startIndex = ranks.index(start[0])
                endIndex = ranks.index(end[0])
                for i in range(endIndex, startIndex + 1):
                    combinations.append(ranks[i] + ranks[i])
            else:
                startIndex = ranks.index(start[1])
                endIndex = ranks.index(end[1])
                suite = start[2]
                for i in range(endIndex, startIndex + 1):
                    combinations.append(start[0] + ranks[i] + suite)
        else:
            combinations.append(hand_range.strip())

    return list(set(combinations))


def showHand(card1, card2):
    image1 = plt.imread("cards/card_" + card1 + ".png")
    image2 = plt.imread("cards/card_" + card2 + ".png")

    fig, (ax1, ax2) = plt.subplots(1, 2)

    ax1.imshow(image1)
    ax2.imshow(image2)
    plt.draw()


def result(randomCards, openingRange):
    global correct, error
    retry = True
    while retry:
        retry = False
        isOpened = input("Is " + randomCards + " in your range? (y/n): ")
        if isOpened == "y":
            if randomCards in openingRange:
                correct += 1
            else:
                error += 1
                print("Error: " + randomCards + " is not in your range")
        elif isOpened == "n":
            if randomCards in openingRange:
                error += 1
                print("Error: " + randomCards + " is in your range")
            else:
                correct += 1
        elif isOpened == "q":
            plt.close()
            return 1
        else:
            print("Invalid input ! Use y/n")
            retry = True
    plt.close()
    return 0


def main():
    openingRange = parseRange(input("Enter a range (Flopzilla format): "))
    if len(openingRange) == 0:
        print("Invalid range")
        return

    numberOfHands = input("Enter number of hands to play: ")
    if not numberOfHands.isdigit() or int(numberOfHands) <= 0:
        print("Invalid number")
        return

    plt.ion()
    for _ in range(int(numberOfHands)):
        randomCards = randomHand()
        showHand(randomCards[0], randomCards[1])
        res = result(randomCards[2], openingRange)
        if res == 1:
            break

    print("Congratulations!")
    print("Total Hands: " + numberOfHands)
    print(
        "Correct: " + str(correct) + " // ",
        str(correct / int(numberOfHands) * 100) + "%",
    )
    print("Error: " + str(error) + " // ", str(error / int(numberOfHands) * 100) + "%")


main()
