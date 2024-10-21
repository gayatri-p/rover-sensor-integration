from ultralytics import YOLO
import cv2
import math

cap = cv2.VideoCapture(0)

cap.set(3, 640)
cap.set(4, 480)

# model
model = YOLO(r"/home/smlab/Rover/ObjectDetect/runs/detect/train2/weights/best.pt")

# Export the model
model.export(format="engine")

# Load the exported model
trt_model = YOLO(r"/home/smlab/Rover/ObjectDetect/runs/detect/train2/weights/best.engine")

# object classes
classNames = ["cylinders", "Joshna"
              ]

#REAL TIME DETECTING STUFF. Link in bio : https://dipankarmedh1.medium.com/real-time-object-detection-with-yolo-and-webcam-enhancing-your-computer-vision-skills-861b97c78993
#Press q to end.

while True:
    success, img = cap.read()
    results = trt_model(img, stream=True)

    # coordinates
    for r in results:
        boxes = r.boxes

        for box in boxes:
            # bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # convert to int values

            # put box in cam
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

            # confidence
            confidence = math.ceil((box.conf[0]*100))/100
            print("Confidence --->",confidence)

            # class name
            cls = int(box.cls[0])
            print("Class name -->", classNames[cls])

            # object details
            org = [x1, y1]
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 1
            color = (255, 0, 0)
            thickness = 2

            cv2.putText(img, classNames[cls], org, font, fontScale, color, thickness)

    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Load a model
#model = YOLO(r"/home/smlabRover/ObjectDetect/runs/detect/train2/best.pt")  # load a pretrained model (recommended for training)

# Train the model
#results = model.train(data=r"/home/smlabRover/ObjectDetect/Dataset/Dataset half 2/data.yaml", epochs=50, imgsz=640)

#Predict on a dataset
#model.predict(r"C:\Users\beast\Downloads\shnapes.jpg", save=True)
