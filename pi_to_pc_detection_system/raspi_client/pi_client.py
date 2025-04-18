
import cv2
import requests
from ultralytics import YOLO
import base64
import time

model = YOLO("best.pt")
server_url = "http://<PC-IP>:5000/upload"

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    results = model(frame)
    for r in results:
        for box in r.boxes:
            label = model.names[int(box.cls[0])]
            _, buffer = cv2.imencode('.jpg', frame)
            image_b64 = base64.b64encode(buffer).decode('utf-8')
            
            data = {
                'label': label,
                'image': image_b64
            }
            try:
                requests.post(server_url, json=data)
                print(f"📤 ส่งข้อมูล: {label}")
            except:
                print("❌ ไม่สามารถเชื่อมต่อเซิร์ฟเวอร์ได้")

            time.sleep(2)
            break  /***************** อันนี้โค้ด นกอันเก่า*****************/
