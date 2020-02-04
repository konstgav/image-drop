import matplotlib.pyplot as plt

pixelNumbers = []
with open('pixelNumbers.txt', 'r') as f:
	for line in f:
		pixelNumber = (int)(line)
		pixelNumbers.append(pixelNumber)

plt.plot(pixelNumbers)
plt.show()

