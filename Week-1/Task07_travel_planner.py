Destination = input("Enter your destination: ")
Distance_in_km = float(input("Enter the distance in kilometers: "))
Average_speed_in_km_per_hour = float(input("Enter the average speed in kilometers per hour: "))

Time = Distance_in_km / Average_speed_in_km_per_hour
hours = int(Time)
minutes = round((Time - hours) * 60)

if minutes == 60:
    hours += 1
    minutes = 0
    
print(f"Destination: {Destination}")
print(f"Distance: {Distance_in_km:.2f} km")
print(f"Average speed: {Average_speed_in_km_per_hour:.2f} km/h")
print()

print(f"Estimated Travel Time: {hours} hours and {minutes} minutes")
