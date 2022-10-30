with open('measurements.txt', 'r') as file:
    data = file.read().splitlines()

data = [int(i) for i in data]

threeMeasurementWindowData = []



for i in range(len(data) - 3 + 1):
    threeMeasurementWindowData.append(data[i:i+3])

#print(threeMeasurementWindowData)

numOfIncreased = 0
prev = sum(threeMeasurementWindowData[0])

for i in threeMeasurementWindowData:
    if sum(i) > prev:
        numOfIncreased += 1
    prev = sum(i)

print(numOfIncreased)