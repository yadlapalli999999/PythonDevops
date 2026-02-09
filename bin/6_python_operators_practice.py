# 1. Use the arithmetic operators to calculate the sum, average CPU load given 
cpu_loads = [40,60,80]
total_loads = sum(cpu_loads)
average_loads = total_loads/len(cpu_loads)
print("Length cpu loads:", len(cpu_loads))
print("Total loads:", total_loads) 
print("Average CPU loads:", average_loads)

#2. Use the modulus operator % to check if a build number is even or odd(build_id % 2)
build_id = int(input('enter build id'))
if build_id % 2 == 0: 
    print(f"build id {build_id} even ")
else:
    print(f"build id {build_id} is odd")
    

#3. Use the floor division // to divide total log lines into chunks of 1000 for processing.
total_log_lines = 12040
chunk_size = 1000
res_chunk = total_log_lines/chunk_size
print("Number of chunks of 1000 log lines:", res_chunk)


#4. Use comparison operators to check if disk usage is above 80%
disk_usage_input = int(input("Enter the disk usage Percentage"))
if disk_usage_input >= 80:
    print("Above 80 disk usage")
else:
    print("below 80 disk usage ")

#5. Use logical operators(and, or, not) to check if (CPU> 70 and Memory >80)
cpu = int(input("Enter CPU percentage: "))
memory = int(input("Enter Memory percentage: "))
if cpu > 70 and memory > 80:
    print("ALERT: Both CPU and Memory are high!")
elif cpu > 70 or memory > 80:
    print("WARNING: Either CPU or Memory is high")
else:
    print("System is healthy")

if not (cpu > 90):
    print("CPU is acceptable")

#6. Use assignment operators(+=) to incrementally add network packet counts
packet_count = 0
packet_batches = [100, 250, 150, 300]
for batch in packet_batches:
    packet_count += batch
print(f"Total packets received: {packet_count}")

#7. Use the identity operator is to check if two service config reference the same object un memory
config_a = {"port": 8080, "host": "localhost"}
config_b = config_a
config_c = {"port": 8080, "host": "localhost"}
if config_a is config_b:
    print("config_a and config_b reference the same object")
else:
    print("config_a and config_b are different objects")

if config_a is config_c:
    print("config_a and config_c reference the same object")
else:
    print("config_a and config_c are different objects (same content)")

#8. Use the membership operator in to check if"nginx" is in running_services 
running_services = ["nginx", "mysql", "redis"]
if "nginx" in running_services:
    print("nginx service is running")
else:
    print("nginx service is NOT running")


#9. Simulate auto-scaling: if current_replicas < desired_rplicas, scale up by 1
current_replicas = 2
desired_replicas = 5
while current_replicas < desired_replicas:
    current_replicas += 1
    print(f"Scaling up: current replicas = {current_replicas}")
print(f"Target reached: {current_replicas} replicas running")

#10. Use ternary operator: status= "ALERT" if cpu > 90 else "OK"
cpu = 85
status = "ALERT" if cpu > 90 else "OK"
print(f"CPU Status: {status}")

#11. Combine multiple comparison operators: 50 < cpu <90
cpu = 75
if 50 < cpu < 90:
    print(f"CPU {cpu}% is in normal range (50-90)")
elif cpu <= 50:
    print("CPU is low")
else:
    print("CPU is critical")

#12. Use not in to ensure "debug" flag is not present in prod settings.
prod_settings = {"environment": "production", "log_level": "error", "timeout": 30}
if "debug" not in prod_settings:
    print("Production settings are secure - debug flag not present")
else:
    print("WARNING: Debug flag found in production settings!")

#13. Use augmented assignment (*=) to double retry timeout every failed attempt.
retry_timeout = 1  # seconds
attempts = 0
max_attempts = 4
while attempts < max_attempts:
    attempts += 1
    print(f"Attempt {attempts}: timeout = {retry_timeout}s")
    retry_timeout *= 2  # double timeout
print(f"Max timeout reached: {retry_timeout}s after {attempts} attempts")

#14.Write a program that prompts the user to enter their height and weight, and then calculates and prints their body mass index (BMI)
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))
bmi = weight / (height ** 2)
print("Your BMI is:", bmi)

#15. WAP that calculates 
# a): Addition of two numbers.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum_result = num1 + num2
print("Sum of two numbers:", sum_result)

# b): Average of three values.
val1 = int(input("Enter first value: "))
val2 = int(input("Enter second value: "))
val3 = int(input("Enter third value: "))
average = (val1 + val2 + val3) / 3
print("Average of three values:", average)

#16. WAP that prompts the user to enter the radius of a circle and calculate then print the area and circumference of the circle.
radius = float(input("Enter the radius of the circle: "))
Area = 3.14 * (radius * radius)
Perimeter = 2 * 3.14 * radius
print("Area of the circle:", Area)
print("Circumference of the circle:", Perimeter)

#17. WAP that prompts the user to enter the length and width of a rectangle, and then calculates and prints the area and perimeter of the rectangle.
Length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
perimeter = 2 * (Length + width)
Area = Length * width 
print("Area of the rectangle:", Area)
print("Perimeter of the rectangle:", perimeter)
