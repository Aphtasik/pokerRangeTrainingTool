import random
import matplotlib.pyplot as plt

allPossibleHandsString = [
    "22",
    "32o",
    "42o",
    "52o",
    "62o",
    "72o",
    "82o",
    "92o",
    "T2o",
    "J2o",
    "Q2o",
    "K2o",
    "A2o",
    "32s",
    "33",
    "43o",
    "53o",
    "63o",
    "73o",
    "83o",
    "93o",
    "T3o",
    "J3o",
    "Q3o",
    "K3o",
    "A3o",
    "42s",
    "43s",
    "44",
    "54o",
    "64o",
    "74o",
    "84o",
    "94o",
    "T4o",
    "J4o",
    "Q4o",
    "K4o",
    "A4o",
    "52s",
    "53s",
    "54s",
    "55",
    "65o",
    "75o",
    "85o",
    "95o",
    "T5o",
    "J5o",
    "Q5o",
    "K5o",
    "A5o",
    "62s",
    "63s",
    "64s",
    "65s",
    "66",
    "76o",
    "86o",
    "96o",
    "T6o",
    "J6o",
    "Q6o",
    "K6o",
    "A6o",
    "72s",
    "73s",
    "74s",
    "75s",
    "76s",
    "77",
    "87o",
    "97o",
    "T7o",
    "J7o",
    "Q7o",
    "K7o",
    "A7o",
    "82s",
    "83s",
    "84s",
    "85s",
    "86s",
    "87s",
    "88",
    "98o",
    "T8o",
    "J8o",
    "Q8o",
    "K8o",
    "A8o",
    "92s",
    "93s",
    "94s",
    "95s",
    "96s",
    "97s",
    "98s",
    "99",
    "T9o",
    "J9o",
    "Q9o",
    "K9o",
    "A9o",
    "T2s",
    "T3s",
    "T4s",
    "T5s",
    "T6s",
    "T7s",
    "T8s",
    "T9s",
    "TT",
    "JTo",
    "QTo",
    "KTo",
    "ATo",
    "J2s",
    "J3s",
    "J4s",
    "J5s",
    "J6s",
    "J7s",
    "J8s",
    "J9s",
    "JTs",
    "JJ",
    "QJo",
    "KJo",
    "AJo",
    "Q2s",
    "Q3s",
    "Q4s",
    "Q5s",
    "Q6s",
    "Q7s",
    "Q8s",
    "Q9s",
    "QTs",
    "QJs",
    "QQ",
    "KQo",
    "AQo",
    "K2s",
    "K3s",
    "K4s",
    "K5s",
    "K6s",
    "K7s",
    "K8s",
    "K9s",
    "KTs",
    "KJs",
    "KQs",
    "KK",
    "AKo",
    "A2s",
    "A3s",
    "A4s",
    "A5s",
    "A6s",
    "A7s",
    "A8s",
    "A9s",
    "ATs",
    "AJs",
    "AQs",
    "AKs",
    "AA",
]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
colors = ["h", "d", "c", "s"]
suited = ["s", "o"]
correct = 0
error = 0


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
        else:
            print("Invalid input ! Use y/n")
            retry = True


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
        result(randomCards[2], openingRange)

    print("Congratulations!")
    print("Total Hands: " + numberOfHands)
    print(
        "Correct: " + str(correct) + " // ",
        str(correct / int(numberOfHands) * 100) + "%",
    )
    print("Error: " + str(error) + " // ", str(error / int(numberOfHands) * 100) + "%")


main()
