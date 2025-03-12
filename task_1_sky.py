import numpy as np
from tqdm import tqdm
import os

# Parameters
data_file = "./Opensky.bin"
carrier_frequency = 1575.42e6  # Hz
IF_frequency = 4.58e6  # Hz
sampling_frequency = 58e6  # Hz
data_format = np.int8  # 8-bit I/Q samples
data_length = 90  # seconds

# Ground Truth Coordinates (latitude, longitude)
ground_truth_coords = (22.328444770087565, 114.1713630049711)

# Load Data Function with progress bar
def load_data(file_path, data_format, data_length, sampling_frequency):
    sample_count = int(sampling_frequency * data_length)  # Total samples
    data = np.empty(sample_count, dtype=data_format)
    
    # Use tqdm to show progress while loading data
    with tqdm(total=sample_count, desc="Loading Data", ncols=100) as pbar:
        with open(file_path, 'rb') as f:
            for i in range(0, sample_count, 1024):  # Read in chunks of 1024 samples at a time
                chunk_size = min(1024, sample_count - i)
                data[i:i + chunk_size] = np.fromfile(f, dtype=data_format, count=chunk_size)
                pbar.update(chunk_size)
                
    return data

# Process I/Q Data (Basic)
def process_if_data(data, sampling_frequency, IF_frequency):
    # Reshape data to I/Q pairs (real, imaginary)
    iq_data = data.reshape(-1, 2)  # Assuming the data is interleaved I/Q pairs
    I = iq_data[:, 0]
    Q = iq_data[:, 1]

    # Frequency domain processing (example: FFT)
    N = len(I)
    fft_data = np.fft.fft(I + 1j*Q, N)
    freqs = np.fft.fftfreq(N, d=1/sampling_frequency)
    
    # Filter by IF frequency
    freq_range = np.logical_and(freqs >= IF_frequency - 1e6, freqs <= IF_frequency + 1e6)
    filtered_fft = fft_data[freq_range]

    return filtered_fft

# Main Processing
def main():
    print("Loading data...")
    data = load_data(data_file, data_format, data_length, sampling_frequency)
    print(f"Data loaded: {len(data)} samples")

    print("Processing I/Q data...")
    fft_results = process_if_data(data, sampling_frequency, IF_frequency)
    
    # Display progress bar for processing
    for i in tqdm(range(100), desc="Processing FFT", ncols=100):
        pass  # Placeholder for actual processing steps

    print("Initial acquisition results generated.")

    # Output the results (print or save to file)
    print("Filtered FFT Results (Initial Acquisition):")
    print(fft_results)

    # Optionally, save to a file for further analysis
    output_file = "acquisition_results.npy"
    np.save(output_file, fft_results)
    print(f"Results saved to {output_file}")

    return fft_results

if __name__ == "__main__":
    results = main()
