import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import correlate
from tqdm import tqdm
import os

# Constants
CARRIER_FREQUENCY = 1575.42e6  # MHz
IF_FREQUENCY = 4.58e6  # MHz
SAMPLING_FREQUENCY = 58e6  # Hz
DATA_LENGTH = 90  # seconds
GROUND_TRUTH = (22.328444770087565, 114.1713630049711)
FILENAME = './Opensky.bin'  # Adjust the path to your .bin file

# Parameters for DLL (example values, these would be tuned in practice)
DLL_SAMPLES = 1000  # Number of samples per iteration
CARRIER_WAVEFORM = np.cos(2 * np.pi * IF_FREQUENCY * np.arange(DLL_SAMPLES) / SAMPLING_FREQUENCY)  # Carrier for DLL

# Function to read binary data with progress bar
def read_bin_data(file_path, chunk_size=1e6):
    data = []
    total_size = os.path.getsize(file_path)
    with tqdm(total=total_size, unit='B', unit_scale=True) as pbar:
        with open(file_path, 'rb') as file:
            while True:
                chunk = file.read(int(chunk_size))
                if not chunk:
                    break
                data.append(np.frombuffer(chunk, dtype=np.int8))
                pbar.update(len(chunk))
    return np.concatenate(data)

# Function to perform DLL tracking and generate correlation plot
def tracking_loop(iq_data, samples_per_iteration=DLL_SAMPLES):
    num_samples = len(iq_data)
    corr_peaks = []

    # Loop over the data with sliding window (simulate DLL tracking)
    for i in range(0, num_samples - samples_per_iteration, samples_per_iteration):
        # Extract a window of I/Q samples
        window = iq_data[i:i + samples_per_iteration]
        I_samples = window[::2]  # Extract I samples (real part)
        Q_samples = window[1::2]  # Extract Q samples (imaginary part)
        
        # Compute the correlation with the carrier signal
        signal = I_samples + 1j * Q_samples  # Create complex signal
        correlation = correlate(signal, CARRIER_WAVEFORM, mode='same')

        # Store the peak correlation value
        corr_peaks.append(np.max(np.abs(correlation)))

        # Visualize correlation plot
        plt.plot(np.abs(correlation))
        plt.title('Correlation Plot')
        plt.xlabel('Sample')
        plt.ylabel('Correlation Magnitude')
        plt.show()

    return corr_peaks

# Simulate urban interference (example: adding noise to the signal)
def add_urban_interference(iq_data, noise_level=0.1):
    noise = np.random.normal(0, noise_level, len(iq_data))  # Gaussian noise
    return iq_data + noise

# Main function to process the data
def main():
    print("Loading dataset...")
    iq_data = read_bin_data(FILENAME)

    print("Processing data with DLL tracking...")
    corr_peaks = tracking_loop(iq_data)

    # Visualizing correlation peaks
    plt.plot(corr_peaks)
    plt.title('Correlation Peaks over Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Peak Correlation Magnitude')
    plt.show()

    # Simulate and visualize urban interference
    print("Simulating urban interference...")
    iq_data_with_interference = add_urban_interference(iq_data)

    print("Processing data with urban interference...")
    corr_peaks_interference = tracking_loop(iq_data_with_interference)

    # Visualizing correlation peaks with interference
    plt.plot(corr_peaks_interference)
    plt.title('Correlation Peaks with Urban Interference')
    plt.xlabel('Time (s)')
    plt.ylabel('Peak Correlation Magnitude')
    plt.save()
    #plt.show()

if __name__ == '__main__':
    main()
