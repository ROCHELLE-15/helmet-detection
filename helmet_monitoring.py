import cv2
from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolov8n.pt")

# Open video file (change to 0 for webcam)
cap = cv2.VideoCapture("traffic.mp4")

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    results = model(frame)

    for result in results:
        for box in result.boxes:
            cls = int(box.cls[0])
            label = model.names[cls]

            if label in ["person", "motorcycle"]:
                x1, y1, x2, y2 = map(int, box.xyxy[0])

                cv2.rectangle(frame,
                              (x1, y1),
                              (x2, y2),
                              (255, 0, 0),
                              2)

                cv2.putText(frame,
                            label,
                            (x1, y1-10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.7,
                            (255, 0, 0),
                            2)

    cv2.imshow("Helmet Monitoring System", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
