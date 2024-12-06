import os
import cv2
import time
import uuid


# Generate image datasets from webcam
IMAGES_PATH = os.path.join("data", "images")
number_images = 30

cap = cv2.VideoCapture(0)
for img_num in range(number_images):
    print("Collecting image{}".format(img_num))
    ret, frame = cap.read()
    img_name = os.path.join(IMAGES_PATH, f"{str(uuid.uuid1())}.jpg")
    cv2.imwrite(img_name, frame)
    cv2.imshow("frame", frame)
    time.sleep(0.5)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
