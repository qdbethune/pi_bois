import matplotlib.pyplot as plt
# import audioPassEnergy.py

def energyToMovingAvg(energyFilePath):

    # Open FFT spectral energy datafile
    with open(energyFilePath) as datafile:
        energyData = datafile.readlines()

    # Convert data to usable floats
    for i in range(len(energyData)):
        energyData[i] = float(energyData[i].strip())

    # Calculate moving averages
    N = 30
    cumsum, moving_aves = [0], []

    # Graph of unfiltered data
    plt.plot(energyData[:int(((10/140)*len(energyData)))], label='Unfiltered Data')

    # Enumerate generates moving averages based on cumulative sum
    for i, x in enumerate(energyData, 1):
        cumsum.append(cumsum[i-1] + x)
        if i>=N:
            moving_ave = (cumsum[i] - cumsum[i-N])/N
            energyData[i-15] = moving_ave

    # Truncate energy list down to 0.05-second intervals
    duration = open("./Evalues/fileDuration")
    T = int(round(float(duration.read().strip())))  # Total duration of relevant audio file
    X = len(energyData)                             # Total number of energy data entries
    t = 0.05                                        # Time interval length
    I = int(T / t)                                  # Number of time intervals in audio file
    timedEnergies = []

    for i in range(I):
        timedEnergies.append(energyData[(int(round(((t * i) / T) * X)))])
        print(timedEnergies[i])
    


    # Graph of moving averages
    plt.plot(energyData[:int(((10/140)*len(energyData)))], label='Moving Average Filter')
    plt.xlabel('Time')
    plt.ylabel('Energy')
    plt.title('Low Pass Data Filter over 10 seconds')
    plt.legend()
    plt.show()

def main():
    energyToMovingAvg('./Evalues/highOutput')

if __name__ == '__main__':
    main()