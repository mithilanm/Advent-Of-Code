def slidingWindowData(data, slidingWindow):
    threeMeasurementWindowData = []

    for i in range(len(data) - slidingWindow + 1):
        threeMeasurementWindowData.append(data[i:i+slidingWindow])

    return threeMeasurementWindowData


def increasedThreeMeasurements(data):
    numOfIncreased = 0
    prev = sum(data[0])

    for i in data:
        if sum(i) > prev:
            numOfIncreased += 1
        prev = sum(i)

    return numOfIncreased

def main():
    with open('measurements.txt', 'r') as file:
        data = file.read().splitlines()

    data = [int(i) for i in data]

    reformedData = slidingWindowData(data, 3)

    print("The number of increased measurements is: " + str(increasedThreeMeasurements(reformedData)))

main()
