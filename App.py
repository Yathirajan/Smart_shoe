import serial
import mysql.connector
import time

# Serial port configuration (update COM port or /dev/ttyUSB0 for Linux)
ser = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2)  # allow Arduino to reset

# MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",       # your MySQL username
    password="your_password",
    database="smart_shoe"
)
cursor = db.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS sensor_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    weight FLOAT,
    distance FLOAT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

print("Listening for Arduino data...")

try:
    while True:
        line = ser.readline().decode('utf-8').strip()
        if line:
            try:
                weight, distance = line.split(",")
                weight = float(weight)
                distance = float(distance)

                # Insert into MySQL
                cursor.execute("INSERT INTO sensor_data (weight, distance) VALUES (%s, %s)", (weight, distance))
                db.commit()

                print(f"Inserted -> Weight: {weight} g, Distance: {distance} cm")

            except ValueError:
                print("Invalid data:", line)

except KeyboardInterrupt:
    print("Stopped by user.")

finally:
    cursor.close()
    db.close()
    ser.close()
