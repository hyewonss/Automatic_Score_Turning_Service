import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display

filename = 'p1.wav'
y, sr = librosa.load(filename)
# trim silent edges
p1, _ = librosa.effects.trim(y)
librosa.display.waveshow(p1, sr=sr)

n_fft = 2048
D = np.abs(librosa.stft(p1[:n_fft], n_fft=n_fft, hop_length=n_fft+1))
plt.plot(D)