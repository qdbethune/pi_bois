
import essentia
from essentia.streaming import *

def audioPassEnergy ():  

    """Program to test the various audio processing capabilities of Essentia"""

    # Load audio in mono using MonoLoader default parameters
    print("Enter input audio file path:")
    loader = MonoLoader(filename=input())

    # Cuts audio into discrete frames 
    lowCutter = FrameCutter(frameSize = 1024, hopSize = 512)
    lowmidCutter = FrameCutter(frameSize = 1024, hopSize = 512)
    highmidCutter = FrameCutter(frameSize = 1024, hopSize = 512)
    highCutter = FrameCutter(frameSize = 1024, hopSize = 512)

    # Low Pass filter (cutoff > 256hz)
    lowFilter = LowPass(cutoffFrequency= 256)

    # Low-Mid Pass filter (256 - 1024hz)
    lowmidFilter = BandPass(cutoffFrequency= 256, bandwidth=768)

    # High-Mid Pass filter (1024 - 4096hz)
    highmidFilter = BandPass(cutoffFrequency= 1024, bandwidth=3072)

    # High Pass filter (cutoff < 4096hz)
    highFilter = HighPass(cutoffFrequency= 4096)

    # Fast Fourier Transform Magnitudes
    lowSpec = Spectrum()
    lowmidSpec = Spectrum()
    highmidSpec = Spectrum()
    highSpec = Spectrum()

    # Energy value
    lowEnergy = Energy()
    lowmidEnergy = Energy()
    highmidEnergy = Energy()
    highEnergy = Energy()

    # Files for data output
    lowout = FileOutput(filename = './Evalues/lowOutput')
    lowmidout = FileOutput(filename = './Evalues/lowmidOutput')
    highmidout = FileOutput(filename = './Evalues/highmidOutput')
    highout = FileOutput(filename = './Evalues/highOutput')

    # Duration of audio file in seconds
    duration = Duration()
    durationOut = FileOutput(filename= './Evalues/fileDuration')
    loader.audio >> duration.signal
    duration.duration >> durationOut

    # Data flow to low filter
    loader.audio >> lowFilter.signal
    lowFilter.signal >> lowCutter.signal
    lowCutter.frame >> lowSpec.frame
    lowSpec.spectrum >> lowEnergy.array
    lowEnergy.energy >> lowout

    # Data flow to lowmid filter
    loader.audio >> lowmidFilter.signal
    lowmidFilter.signal >> lowmidCutter.signal
    lowmidCutter.frame >> lowmidSpec.frame
    lowmidSpec.spectrum >> lowmidEnergy.array
    lowmidEnergy.energy >> lowmidout

    # Data flow to highmid filter
    loader.audio >> highmidFilter.signal
    highmidFilter.signal >> highmidCutter.signal
    highmidCutter.frame >> highmidSpec.frame
    highmidSpec.spectrum >> highmidEnergy.array
    highmidEnergy.energy >> highmidout

    # Data flow to high filter
    loader.audio >> highFilter.signal
    highFilter.signal >> highCutter.signal
    highCutter.frame >> highSpec.frame
    highSpec.spectrum >> highEnergy.array
    highEnergy.energy >> highout


    # Run statement
    essentia.run(loader)

def main():
    audioPassEnergy()
    
if __name__ == "__main__":
    main()
