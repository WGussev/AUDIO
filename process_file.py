import matplotlib.pyplot as plt
import scipy.io.wavfile
from pathlib import Path
import numpy as np


def process_file(sample_path, template_path, out_path):
    freq_sample, sample = scipy.io.wavfile.read(sample_path)
    freq_template, template = scipy.io.wavfile.read(template_path)
    fig = convolve(sample, template)
    fig.savefig(Path(out_path, 'figure.png'))


def convolve(sample, template):
    # threshold = sum(template[:, 0] * template[:, 0])
    convolution = np.convolve(sample[:, 0], template[:, 0])
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(convolution)
    # ax.hlines(threshold, 0, len(convolution))
    return fig