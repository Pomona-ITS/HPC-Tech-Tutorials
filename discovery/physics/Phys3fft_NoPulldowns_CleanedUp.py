
import os
import glob
import wave
import struct
import numpy
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


# def dependencies_for_fft():
# -------------------------------------------------------------------
#  Functions for reading the sound file and processing it.


def readSoundData():
    global soundData, soundTime, numPts2Xform, soundMax, soundMin
    powerOf2 = int(numpy.log(length)/numpy.log(2))
    numPts2Xform = int(2**powerOf2)
    print('power of 2 = ', powerOf2, 'number of points = ', numPts2Xform)

    soundData = numpy.zeros(numPts2Xform)
    leftChan = numpy.zeros(numPts2Xform)
    soundTime = numpy.zeros(numPts2Xform)
    soundMax = 0
    soundMin = 0

    for i in range(0, numPts2Xform):
        binaryData = soundFile.readframes(1)
    #        print('string binaryData = ',binaryData)
    #        print('length of string = ', len(binaryData))
    #       print('type of binary Data = ',type(binaryData))
        leftChan = binaryData[0:2]
    #        'leftChan = ',leftChan, 'length of leftChan = ',len(leftChan)
        if len(binaryData) == 4:
            rightChan = binaryData[2:4]
    #        print(int(leftChan))
    #        unpacked = struct.unpack("<h",binaryData)
        unpacked = struct.unpack("<h", leftChan)
    #         unpacked[0]
    #        print('type of unpacked = ',type(unpacked))
        soundData[i] = unpacked[0]
        soundTime[i] = float(i) / float(sampleFreq)
        if soundData[i] > soundMax:
            soundMax = soundData[i]
        elif soundData[i] < soundMin:
            soundMin = soundData[i]

    soundFile.close()
    findXform()
    return()


def findXform():
    global soundSpec, frequency, normSpec, lenXform, smoothSpec
    global ampl
    soundSpec = numpy.zeros(int(numPts2Xform/2))
    frequency = numpy.zeros(int(numPts2Xform/2))
    normSpec = numpy.zeros(int(numPts2Xform/2))
    smoothSpec = numpy.zeros(int(numPts2Xform/2))
    normSmooth = numpy.zeros(int(numPts2Xform/2))

    xForm = numpy.fft.fft(soundData)
    lenXform = len(xForm)
    norm = numpy.absolute(xForm[0])
    ampl = norm**(0.5)
    print('amplitude = ', round(ampl, 3))

    for j in range(0, int(lenXform/2) - 1):
        soundSpec[j] = numpy.absolute(xForm[j])
    offset = int((ptsSmoothed - 1)/2)
    for k in range(0, offset):
        smoothSpec[k] = soundSpec[k]
        smoothSpec[len(soundSpec) - 1 - k] = soundSpec[len(soundSpec) - 1 - k]
    for j in range(1, len(soundSpec)-offset):
        smoothSpec[j] = 0.0
        for k in range(1, ptsSmoothed):
            smoothSpec[j] = smoothSpec[j]+soundSpec[j+k-offset]
        smoothSpec[j] = smoothSpec[j]/ptsSmoothed

    normSpec[0] = 0
    frequency[0] = 0
    specMax = max(soundSpec)
    smoothMax = max(smoothSpec)

    for j in range(1, int(lenXform/2 - 1)):
        frequency[j] = j*float(sampleFreq)/float(lenXform)
        normSpec[j] = soundSpec[j]/specMax
        normSmooth[j] = smoothSpec[j]/smoothMax
    return


def spectrumPlot(fileName, plotNum, spectrum):
    plt.figure(2)
    plt.plot(frequency, spectrum)
    plt.axis([0, freqLimit, 0, 1])
    if plotNum == 1:
        titleText = 'Wave spectrum, normalized to strongest overtone\n' + currentDir + '\\' + fileName
        xText = ''
    else:
        titleText = fileName
        xText = 'Frequency (Hz)'
    plt.xlabel(xText)
    plt.ylabel('Normalized amplitude')
    plt.title(titleText)
    plt.draw()


def waveformPlot(fileName, plotNum, waveform, harmList):
    #    fundFirstFit = harmList[0]
    #    period = 1/fundFirstFit
    waveMean = numpy.mean(waveform)
    waveStdDev = numpy.std(waveform)
    #    print(( 'Mean value of waveform = ', round(waveMean,2)))
    #     ( 'Standard deviation = ',round(waveStdDev,2))
    #    print(( 'Fundamental from fit = ',round(fundFirstFit,2))
    timeSpan = 0.02
    startTime = 0.1
    #    startTime = soundTime[len(soundTime)-1]/2.0
    waveMax = round(max(waveform) + 3*waveStdDev)
    waveMin = round(min(waveform) - 3*waveStdDev)
    plt.figure(1)
    plt.plot(soundTime, waveform)
    plt.axis([startTime, startTime + timeSpan, waveMin, waveMax])
    if plotNum == 1:
        titleText = 'Waveform vs. time\n' + currentDir + '\\' + fileName
        xText = ''
    else:
        titleText = fileName
        xText = 'Time (sec)'
    plt.title(titleText)
    plt.xlabel(xText)
    plt.ylabel('Amplitude (arbitrary units)')
    plt.draw()


def semilogSpecPlot(fileName, plotNum, spectrum):
    logSpectrum = numpy.zeros(len(spectrum))
    plt.figure(3)
    for j in range(1, len(spectrum)):
        if spectrum[j] == 0:
            logSpectrum[j] = -47
        else:
            logSpectrum[j] = numpy.log10(spectrum[j])

    plt.plot(frequency, logSpectrum)
    plt.axis([0, freqLimit, -6, 1])
    if plotNum == 1:
        titleText = 'Semilog plot of spectrum\n' + currentDir + '\\' + fileName
        xText = ''
    else:
        titleText = fileName
        xText = 'Frequency (Hz)'
    plt.xlabel(xText)
    plt.ylabel('log10(Normalized amplitude)')
    plt.title(titleText)
    plt.draw()

    #  -------------------------------------------------------------------
    # Main routine

OPTIONS = glob.glob('*.wav')
defaultSmth = 3
defaultFreq = 10000
currentDir = os.getcwd()
print(currentDir)

maxNumFiles = 20
fileList = []
numFiles = 0
for file in glob.glob("*.wav"):
    print(file)
    numFiles = numFiles + 1
    fileList.append(file)
print('number of .wav files = ', numFiles)
for i in range(numFiles):
    print(i+1, fileList[i])
fileIDNum = int(input('Type number from the list above for the file you want, followed by Enter key: '))
fileName = fileList[fileIDNum - 1]
print(fileName)

fileRoot = fileName[0:len(fileName)-4]
# 'Root of file name is ', fileRoot
plotFileName = fileRoot + '.pdf'
# resultsFileName = fileRoot + '.txt'
# spectrumFileName = fileRoot + 'Spec.txt'
ptsSmoothed = defaultSmth
freqLimit = defaultFreq

soundFile = wave.open(fileName, 'rb')
numChan,sampleWidth,sampleFreq,length,compType,compID = soundFile.getparams()
print('Sampling frequency = ', sampleFreq)
print('Number of channels = ', numChan)
print('Number of points in file = ', length)
readSoundData()

waveform = soundData
max1 = soundMax
min1 = soundMin
spectrum = normSpec

harmFreqsList = []

freqEst = 300.0
harmFreqsList.append(freqEst)

plots = PdfPages(plotFileName)

plotNum = 1


waveformPlot(fileName, plotNum, waveform, harmFreqsList)
plots.savefig(1)
spectrumPlot(fileName, plotNum, spectrum)
plots.savefig(2)
semilogSpecPlot(fileName, plotNum, spectrum)
plots.savefig(3)

print('Close all plotting windows to exit the program.')
print('Your plots are not lost but have been saved to the file ', fileName, '.pdf')

plt.show()
plots.close()
