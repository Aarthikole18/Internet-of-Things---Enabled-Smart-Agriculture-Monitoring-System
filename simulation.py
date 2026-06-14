import random
import csv
import time

file = open("data/sensor.csv", "w", newline="")
writer = csv.writer(file)

# headers
writer.writerow(["temp", "humidity", "soil", "light", "pump"])

print("🌱 Smart Agriculture Simulation Started...\n")

for i in range(30):

    # fake sensor values
    temp = random.randint(20, 40)
    humidity = random.randint(40, 90)
    soil = random.randint(800, 2000)
    light = random.randint(200, 900)

    # 🌊 LOGIC (MOST IMPORTANT PART)
    if soil < 1200:
        pump = "ON"
    else:
        pump = "OFF"

    writer.writerow([temp, humidity, soil, light, pump])

    print(f"Temp:{temp} Hum:{humidity} Soil:{soil} Light:{light} Pump:{pump}")

    time.sleep(1)

file.close()

print("\n✅ Simulation Completed! Data saved in sensor.csv")