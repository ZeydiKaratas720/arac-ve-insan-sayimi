from ultralytics import YOLO
import cv2

# YOLO modeli
model = YOLO("yolo11n.pt")

# Video
video = cv2.VideoCapture("traffic.mp4")

# COCO sınıfları
PERSON = 0
CAR = 2
MOTORCYCLE = 3
BUS = 5
TRUCK = 7

while True:

    ret, frame = video.read()

    if not ret:
        break

    # Nesne takibi
    results = model.track(
        frame,
        persist=True,
        tracker="bytetrack.yaml",
        classes=[PERSON, CAR, MOTORCYCLE, BUS, TRUCK],
        verbose=False
    )

    result = results[0]

    person_count = 0
    vehicle_count = 0

    if result.boxes.id is not None:

        boxes = result.boxes

        class_ids = boxes.cls.cpu().numpy()
        track_ids = boxes.id.cpu().numpy()

        for class_id, track_id in zip(class_ids, track_ids):

            class_id = int(class_id)
            track_id = int(track_id)

            # İnsan
            if class_id == PERSON:
                person_count += 1

            # Araç
            elif class_id in [CAR, MOTORCYCLE, BUS, TRUCK]:
                vehicle_count += 1

            # ID'yi ekrana yaz
            box = boxes.xyxy.cpu().numpy()

        # YOLO görüntüsünü oluştur
        annotated_frame = result.plot()

    else:
        annotated_frame = frame

    # Sayıları ekrana yaz
    cv2.putText(
        annotated_frame,
        f"People: {person_count}",
        (30, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.putText(
        annotated_frame,
        f"Vehicles: {vehicle_count}",
        (30, 90),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("People and Vehicle Counting", annotated_frame)

    # Q ile çık
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()