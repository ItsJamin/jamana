import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav

def plot_waveform(wav_file):
    """
    This function takes a path to a wav_file and gives a quick visualization of the waveform.
    """
    # Read the .wav file
    sample_rate, audio_data = wav.read(wav_file)

    # Normalize if audio is stereo (convert to mono)
    if len(audio_data.shape) > 1:
        audio_data = np.mean(audio_data, axis=1)  # Convert stereo to mono

    # Create time array for X-axis
    duration = len(audio_data) / sample_rate  # Total duration in seconds
    time = np.linspace(0, duration, num=len(audio_data))

    # Plot waveform
    plt.figure(figsize=(12, 5))
    plt.plot(time, audio_data, label="Waveform", color="blue", linewidth=0.7)
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")
    plt.title(f"Waveform of {wav_file}")
    plt.legend()
    plt.grid()
    plt.pause(0.1)
    plt.show()


def plot_frequencies(wav_file):
    """
    This function takes a path to a wav_file and gives a quick visualization of the frequencies.
    """

    sample_rate, audio_data = wav.read(wav_file)

    # Convert stereo to mono if necessary
    if len(audio_data.shape) > 1:
        audio_data = np.mean(audio_data, axis=1)  # Average both channels

    # Compute FFT (Fast Fourier Transform)
    N = len(audio_data)  # Number of samples
    fft_output = np.fft.fft(audio_data)  # Compute FFT
    freqs = np.fft.fftfreq(N, d=1/sample_rate)  # Frequency axis

    # Keep only the positive half of frequencies (FFT is symmetric)
    half_N = N // 2
    freqs = freqs[:half_N]
    magnitude = np.abs(fft_output[:half_N])  # Get magnitude of frequencies

    # Plot frequency spectrum
    plt.figure(figsize=(12, 5))
    plt.plot(freqs, magnitude, color='blue', linewidth=0.7)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.title(f"Frequency Spectrum of {wav_file}")
    plt.xlim(0, sample_rate / 2)  # Only show relevant frequencies
    plt.grid()
    plt.show()

