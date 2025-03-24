import video_processor
import analysis

def main():
    video_path = input("Enter the path to your bench press video: ")
    
    # Calibration: provide a known distance (in meters) corresponding to a measured pixel distance.
    known_distance = float(input("Enter a known distance in meters (for calibration): "))
    known_pixels = float(input("Enter the pixel length corresponding to that distance: "))
    scale = known_distance / known_pixels  # Conversion factor: meters per pixel
    
    # Input the weight mass (kg) that you're lifting
    weight_mass = float(input("Enter the mass of the weight (in kg): "))
    
    # Input biomechanical data (arm segment lengths in meters)
    shoulder_to_elbow = float(input("Enter your shoulder-to-elbow distance (in meters): "))
    elbow_to_wrist = float(input("Enter your elbow-to-wrist distance (in meters): "))
    
    print("Select the region of interest (ROI) on the first frame that contains the marker (e.g., bottom of the plate).")
    positions, timestamps = video_processor.process_video(video_path, scale)
    
    if positions is None or timestamps is None:
        print("Error processing the video. Exiting.")
        return

    # Apply a moving average filter to smooth the position data
    filtered_positions = analysis.apply_moving_average_filter(positions, window_size=5)
    # Note: timestamps might need to be trimmed accordingly
    filtered_timestamps = timestamps[4:]  # since 'valid' mode shortens the array by window_size-1

    # Detect repetitions based on peaks (top of the lift) and valleys (bottom)
    reps = analysis.detect_repetitions(filtered_positions, filtered_timestamps)
    print(f"Detected {len(reps)} repetitions.")
    for i, rep in enumerate(reps, 1):
        print(f"Rep {i}: start={rep['start']:.2f}s, peak={rep['peak']:.2f}s, end={rep['end']:.2f}s")

    # Compute velocity and acceleration from the filtered position data
    velocities, accelerations = analysis.compute_derivatives(filtered_positions, filtered_timestamps)
    
    # Compute work and average power output for the overall movement
    work, avg_power = analysis.compute_power_output(filtered_positions, filtered_timestamps, weight_mass)
    print(f"Estimated total work done: {work:.2f} Joules")
    print(f"Estimated average power output: {avg_power:.2f} Watts")
    
    # Compute instantaneous power using force-velocity relationships
    inst_power = analysis.compute_instantaneous_power(velocities, accelerations, weight_mass)
    print(f"Maximum instantaneous power: {max(inst_power):.2f} Watts")
    
    # Use biomechanical data (simple integration): e.g. effective lever arm length
    lever_arm = shoulder_to_elbow + elbow_to_wrist
    print(f"Estimated effective lever arm length: {lever_arm:.2f} meters")
    
if __name__ == "__main__":
    main()