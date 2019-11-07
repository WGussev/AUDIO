import matplotlib.pyplot as plt
import scipy.io.wavfile
from pathlib import Path


def process_file(file_path, out_path):
    freq, signal = scipy.io.wavfile.read(file_path)
    plt.plot(signal)
    plt.savefig(Path(out_path, 'figure.png'))