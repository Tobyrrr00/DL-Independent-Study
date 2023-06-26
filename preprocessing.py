import librosa, librosa.display
import matplotlib.pyplot as plt
import numpy as np

file = "blues.00000.wav"

#waveform
signal, sr = librosa.load(file, sr = 22050) #sr * T -> 22050 * 30
librosa.display.waveplot(signal, sr = sr)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.show()

#fft -> spectrum
fft = np.fft.fft(signal)

magnitude = np.abs(fft)
frequency = np.linspace(0, sr, len(magnitude))
plt.plot(frequency, magnitude)
plt.xlabel("Frequency")
plt.ylabel("Magnitude")
plt.show()

#stft -> spectogram
n_fft = 2048

stft = librosa.core.stft(signal)

# MFCCs
    
