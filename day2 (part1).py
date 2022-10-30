def calculatePosition(data):
    horizontalSum = 0
    depthSum = 0


    for i in data:
        if(i[0] == 'forward'):
            horizontalSum += int(i[1])
        elif(i[0] == 'down'):
            depthSum += int(i[1])
        elif(i[0] == 'up'):
            depthSum -= int(i[1])

    return horizontalSum * depthSum


def main():
    with open('measurements2.txt', 'r') as file:
        data = file.read().splitlines()

    data = [i.split() for i in data]

    print("The final horizontal position multiplied by the final depth is: " + str(calculatePosition(data)))

main()