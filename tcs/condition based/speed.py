dist = int(input("Enter distance in meters: "))
time = int(input("Enter time in seconds: "))

if dist <=0 or time <=0 and time <=60:
    print("Invalid input. Distance and time must be positive.")
else:
    speed =  dist / time

    speedorg = speed * (18/5)
    print(f"Speed (km/h): {round(speedorg, 2)} km/h")