def increasedMeasurements(data):
    numOfIncreased = 0
    prev = data[0]

    for i in data:
        if i > prev:
            numOfIncreased += 1
        prev = i
    
    return numOfIncreased

def main():
    with open('measurements.txt', 'r') as file:
        data = file.read().splitlines()

    data = [int(i) for i in data]

    print("The number of increased measurements is: " + str(increasedMeasurements(data)))

main()