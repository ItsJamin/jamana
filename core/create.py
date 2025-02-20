import numpy as np
import wave
import struct


def create_wav(path : str, sample_rate : int = None, waveform : np.ndarray = None):
    """
    Creates a simple .wav file for a given wave_form

    Arguments:
    - path: path/to/audio.wav
    - sample_rate: how many samples are taken per second
    - wave_form: describes audio wave over the duration
    """

    # Example of a simple sine wave
    if not sample_rate:
        print("[JMN] Missing arguments, defaulting to simple sine wave.")
        sample_rate, waveform = create_signal([440], [0.2], 2.0, sample_rate = 44100)

    with wave.open(path, 'w') as wav_file:
        num_channels = 1  # Mono
        sampwidth = 2  # 2 bytes (16-bit audio)
        framerate = sample_rate
        num_frames = len(waveform)
        comptype = "NONE"
        compname = "not compressed"

        wav_file.setparams((num_channels, sampwidth, framerate, num_frames, comptype, compname))
        
        # Write frames as binary data
        for sample in waveform:
            wav_file.writeframes(struct.pack('<h', sample))
        
        print(f"[JMN] Succesfully created file at {path}.")

def create_signal(frequencies : list[int], amplitudes : list[int], duration : float, sample_rate : int = 44100) -> tuple[int, np.ndarray]:
    """
    Creates a sine-wave-signal timeline for all given frequencies with the given amplitude/loudness.
    """

    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    amplitude = 32767  # Max amplitude for 16-bit audio
    waveform = np.zeros_like(t)

    # Generate waveform by summing sine waves with different amplitudes
    for freq, amp in zip(frequencies, amplitudes):
        waveform += amp * np.sin(2 * np.pi * freq * t)  # Apply amplitude scaling

    # Normalize to 16-bit range (-32768 to 32767)
    max_amplitude = 32767  # 16-bit max value
    waveform = (waveform / np.max(np.abs(waveform)) * max_amplitude).astype(np.int16)
    
    return sample_rate, waveform
    