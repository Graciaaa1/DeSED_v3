import librosa
import numpy as np

def extract_features(audio_path):
    y, sr = librosa.load(audio_path, sr=None)
    pitch = librosa.yin(y, fmin=80, fmax=400)
    speech_rate = len(y) / sr

    mfccs = np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13), axis=1)
    return np.hstack([np.mean(pitch), speech_rate, mfccs])
