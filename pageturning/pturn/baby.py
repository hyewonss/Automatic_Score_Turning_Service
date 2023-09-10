import librosa
import librosa.display

import matplotlib.pyplot as plt

audio_path = 'baby(po.wav)'
y, sr = librosa.load("C:/Users/WHO A U/Desktop/baby.wav")

print('sr:', sr, ', audio shape:', y.shape)
print('length:', y.shape[0]/float(sr), 'secs')

plt.figure(figsize = (10,5))
librosa.display.waveshow(y, sr=sr)
plt.ylabel("Amplitude")
plt.xlim([0,5])
plt.show()
