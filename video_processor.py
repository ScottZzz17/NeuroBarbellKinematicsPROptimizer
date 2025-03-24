import cv2

def process_video(video_path, scale):
    cap = cv2.VideoCapture(video_path)
    positions = []
    timestamps = []
    
    ret, frame = cap.read()
    if not ret:
        print("Error: Cannot open video file.")
        return None, None

    # Let the user select the ROI for the marker
    roi = cv2.selectROI("Select Marker", frame, fromCenter=False, showCrosshair=True)
    cv2.destroyWindow("Select Marker")
    if roi == (0, 0, 0, 0):
        print("ROI not selected.")
        return None, None

    # Initialize tracker (CSRT works well for many cases)
    tracker = cv2.TrackerCSRT_create()
    tracker.init(frame, roi)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        success, box = tracker.update(frame)
        if success:
            x, y, w, h = [int(v) for v in box]
            # Use the bottom-center of the ROI as the marker position
            marker_y = y + h
            # Convert the pixel position to meters using the scale factor
            positions.append(marker_y * scale)
            # Get the timestamp in seconds
            timestamps.append(cap.get(cv2.CAP_PROP_POS_MSEC) / 1000.0)
            
            # For visualization: draw the bounding box and marker point
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.circle(frame, (x + w // 2, marker_y), 5, (0, 255, 0), -1)
        
        cv2.imshow("Tracking", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    return positions, timestamps