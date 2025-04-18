
ระบบตรวจจับจาก Raspberry Pi → ส่งข้อมูลไปยังเว็บ Flask ที่รันบนคอมพิวเตอร์

📌 ขั้นตอนใช้งาน:

1. ติดตั้งไลบรารีที่จำเป็น (บนทั้ง Pi และ คอม):
   pip install flask opencv-python-headless ultralytics requests

2. บนคอมพิวเตอร์ (PC):
   - ไปที่โฟลเดอร์ pc_server
   - รัน: python app.py ***** กุไม่รู้ใช้เอไอเลยบักเชฟ*******
   - เปิดเบราว์เซอร์ที่ http://localhost:5000

3. บน Raspberry Pi:
   - ไปที่โฟลเดอร์ raspi_client
   - แก้ไข pi_client.py: เปลี่ยน <PC-IP> เป็น IP address ของคอมที่รัน Flask
   - วางไฟล์ YOLO model (best.pt) ไว้ในโฟลเดอร์เดียวกัน
   - รัน: python pi_client.py

📂 โฟลเดอร์:
- raspi_client/       → ฝั่ง Raspberry Pi (จับภาพ + ส่งข้อมูล)
- pc_server/          → ฝั่งคอมพิวเตอร์ (รับข้อมูล + แสดงหน้าเว็บ)


******** ไม่รู้ใช้เอไอเลย น่าจะเสร็จวันเดียว ************* เขียนเว็ปให้แล้ว ไปแก้ข้อมูล data เบส เองนะ -*-

