import numpy as np
from scipy.signal import find_peaks

# Gravity in m/s^2
g = 9.81

def apply_moving_average_filter(data, window_size=5):
    """
    Apply a simple moving average filter to smooth the data.
    """
    data = np.array(data)
    filtered = np.convolve(data, np.ones(window_size)/window_size, mode='valid')
    return filtered

def detect_repetitions(positions, timestamps, prominence=0.005):
    """
    Detect repetitions by identifying peaks and valleys in the vertical position data.
    This function assumes that a repetition starts at a valley, reaches a peak, and returns to a valley.
    
    Parameters:
      positions: Array-like of vertical positions (meters)
      timestamps: Corresponding timestamps (seconds)
      prominence: Minimum prominence for peak detection (adjust as needed)
      
    Returns:
      reps: A list of dictionaries with keys 'start', 'peak', and 'end' times.
    """
    positions = np.array(positions)
    timestamps = np.array(timestamps)
    
    # Detect peaks (assume these are the top of the movement)
    peak_indices, _ = find_peaks(positions, prominence=prominence)
    # Detect valleys (assume these are the bottom of the movement)
    valley_indices, _ = find_peaks(-positions, prominence=prominence)
    
    reps = []
    # For each peak, find the closest valley before and after it
    for peak in peak_indices:
        # Find valleys before the peak
        prev_valleys = valley_indices[valley_indices < peak]
        # Find valleys after the peak
        next_valleys = valley_indices[valley_indices > peak]
        if len(prev_valleys) > 0 and len(next_valleys) > 0:
            start = timestamps[prev_valleys[-1]]
            peak_time = timestamps[peak]
            end = timestamps[next_valleys[0]]
            reps.append({'start': start, 'peak': peak_time, 'end': end})
    
    return reps

def compute_derivatives(positions, timestamps):
    """
    Compute velocity and acceleration using numerical gradients.
    """
    positions = np.array(positions)
    timestamps = np.array(timestamps)
    
    velocities = np.gradient(positions, timestamps)
    accelerations = np.gradient(velocities, timestamps)
    return velocities, accelerations

def compute_power_output(positions, timestamps, mass):
    """
    Compute work done and average power output.
    Uses work = m * g * (max displacement) and average power = work / total time.
    """
    positions = np.array(positions)
    timestamps = np.array(timestamps)
    
    # Vertical displacement (assuming movement from lowest to highest point)
    h = np.max(positions) - np.min(positions)
    
    work = mass * g * h
    total_time = timestamps[-1] - timestamps[0] if timestamps[-1] != timestamps[0] else 1
    avg_power = work / total_time
    
    return work, avg_power

def compute_instantaneous_power(velocities, accelerations, mass):
    """
    Compute instantaneous power using:
        F(t) = mass * (acceleration + g)
        P(t) = F(t) * v(t)
    Returns an array of instantaneous power values.
    """
    velocities = np.array(velocities)
    accelerations = np.array(accelerations)
    
    # Instantaneous force in newtons
    force = mass * (accelerations + g)
    # Instantaneous power in watts
    inst_power = force * velocities
    return inst_power