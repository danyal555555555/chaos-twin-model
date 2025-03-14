import numpy as np
import mne
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# Load EEG data (Example: CHB-MIT Dataset)
file_path = 'your-edf-file'  # Example file from CHB-MIT EEG dataset
raw_data = mne.io.read_raw_edf(file_path, preload=True)

# Select EEG channel
eeg_data = raw_data.get_data()[0]  # Select the first channel
time = np.arange(0, len(eeg_data)) / raw_data.info['sfreq']

# Bandpass filter (0.5 - 50 Hz) for noise reduction
def bandpass_filter(data, lowcut=0.5, highcut=50.0, fs=256, order=4):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    return filtfilt(b, a, data)

filtered_eeg = bandpass_filter(eeg_data)

# Plot original vs filtered EEG signal
plt.figure(figsize=(12, 6))
plt.plot(time, eeg_data, label='Original EEG Signal', alpha=0.5)
plt.plot(time, filtered_eeg, label='Filtered EEG Signal', color='red')
plt.title('EEG Signal (Original vs Filtered)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (µV)')
plt.legend()
plt.grid(True)
plt.show()
# Chaos Twin detection algorithm
def detect_chaos_twin(signal, threshold_factor=2):
    errors = np.abs(np.diff(signal))
    mean_error = np.mean(errors)
    std_error = np.std(errors)
    threshold = mean_error + threshold_factor * std_error

    # Identify chaos twin points
    chaos_twin_indices = np.where(errors > threshold)[0]
    return chaos_twin_indices

# Detect and plot Chaos Twin points
chaos_twin_points = detect_chaos_twin(filtered_eeg)

plt.figure(figsize=(12, 6))
plt.plot(time, filtered_eeg, label='Filtered EEG Signal')
plt.scatter(time[chaos_twin_points], filtered_eeg[chaos_twin_points],
            color='red', label='Chaos Twin Points')
plt.title('Chaos Twin Detection in EEG Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (µV)')
plt.legend()
plt.grid(True)
plt.show()
