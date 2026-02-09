# WAP that takes a server's cpu usage (0-100) as input  
# and primts status: 90-100=critical, 80-89=high, 70-79=warning,60-69=moderate,
# below 60= normal

# input
#cpu_usage = 75 # Example CPU usages percentages
cpu_usage = int(input("Enter CPU Usage (0-100): "))
# Drive Factor
# Mutiple conditions

# condition 1: 90-100: Critical
if cpu_usage>=90 and cpu_usage<=100:
    status = "Critical"

# condition 2: 80-89: High
elif cpu_usage>=80 and cpu_usage<=89:
    status = "High"

# condition 3: 70-79: Warning
elif cpu_usage>=70 and cpu_usage<=79:
    status = "Warning"

# condition 4: 60-69: Moderate
elif cpu_usage>=60 and cpu_usage<=69:
    status="Moderate"

# condition 5: below 60: Normal
else:
    status="Normal"


#Executed output
# CPU usage message
print(f"CPU Usage: {cpu_usage}% - status: {status}")

print("#" * 60)

# WAP that takes the number of running containers as input and prints whether it is odd or even

# input
num_containers = int(input("Enter the number of running containers: "))
# Drive Factor
if num_containers % 2 == 0:
    container_status = "even"
else:
    container_status = "odd"

#Executed output
# container weather even or odd print
print(f"The number of container running {num_containers} is {container_status}")
print("#" * 60)

#WAP that calculates the disk usage percentage of a server and printus 
# status:<18.5=Low usage, 18.5-24.9= Normal Usage, 25-29.9= High Usage, >30=Critical(simmulate BMI Logic)

# input
disk_usage = float(input("Enter Disk Usage in Percentage: "))

# Drive Factor
#Multiple disk Usgae factors

# condition 1: <18.5: Low Usage
if disk_usage <18.5:
    disk_status= "Low Usage"
#condition 2: 18.5-24.9 : Normal Usage
elif disk_usage >18.5 and disk_usage <24.9:
    disk_status = "Normal Usage"
# condition 3: 25-29.9: High Usage
elif disk_usage>25 and disk_usage<29.9:
    disk_status = "High Usage"

# condition 4: >=30 : critical Usage
else:
    disk_status = "Critical Usage"

# Executed output
print(f"Disk Usage: {disk_usage}% - status: {disk_status}")
print("#" * 60)

# WAP that takes a deployment status code (200,400,500) and prints whether deployment
# was successful, failed, or needs investigation

#input
deployment_status_code = int(input("Enter Deployment Status Code: "  ))

# Driving Factors
# condition 1: 200- successful
if deployment_status_code == 200:
    deployment_status= "Successful"

# condition 2: 400 - failed
elif deployment_status_code == 400:
    deployment_status = "Failed"

# condition 3: 500 - invesigation
else:
    deployment_status ="Invesigation"
    
# Expected output
print(f"Deployment Status code {deployment_status_code}: {deployment_status}")
print("#" * 60)

#WAP that checks if a service is active and prints "Running" if True else "Stopped"
# input
service = input("Enter the Service :" )

# Driving Factor
if service == "true":
    service_status = "Running"
else:
    service_status ="Stopped"

#Expected output
print(f"service {service}:  {service_status}")

print("#" * 60)


# WAP that accepts port number and prints wether it is in the 
# well-known range (0-1022), registered range (1024-49151), or dynamic range(49152-65535)

#input
port_number = int(input("Enter the Port Number: " ))

# Driving Factor
# condition 1 : 0-1022 - well-known range
if port_number >0 and port_number < 1022:
    port_status = "Well Known Range"
# condition 2: 1024 - 49151 - registered range
elif port_number > 1024 and port_number < 49151:
    port_status = "Registered Range"
# condition 3: 49152-65535 - dynamic range
elif port_number> 49152 and port_number< 65535:
    port_status = "Dynamic Range"
else:
    port_status= "not range"

# Expected output
print(f"port number {port_number} - port status {port_status}")

print("#" * 60)


# WAP that takes RAM usage (%) and prints whether memory is "Healthy", "Warning", or "Critical"
#input
ram_usage = int(input("Enter RAM Usage in Memory : "))

#Driving factor
# condition 1: < 70: Healthy
if ram_usage < 70:
    ram_status = "Healthy"
# condition 2 : > 70 & < 90: Warning
elif ram_usage > 70 and ram_usage < 90:
    ram_status = "Warning"

# condition 3:  > 90 : Critical
else: 
    ram_status = "Critical"

#Expected output
print(f"Ram Usage {ram_usage} - Status {ram_status}")

print("#" * 60)


# WAP that takes a file extension and prints "Log File", "Config File", or "Other File"
file_ext = input("Enter file extension: ").strip().lower()

if file_ext == "log":
    file_status = "Log File"
elif file_ext in ("cfg", "conf", "ini", "yaml", "yml"):
    file_status = "Config File"
else:
    file_status = "Other File"
print(f"File Extention {file_ext} file_status {file_status}")

#WAP that takes a HTTP status code and prints: 200=Success, 400=Client Error, 500= Server Error
# input
http_code = int(input("Enter HTTP Status Code"))
#Driving Factor
# condoition 1 : 200 - Success
if http_code == 200:
    http_status = "Success"
    
# condition 2 : 400 - Client Error
elif http_code == 400:
    http_status = "Client Error"

# condition 3: 500 - Server Error
elif http_code == 500:
    http_status= "Server Error"
else:
    http_status="No Http Code"

#Expected output
print(f"HTTP status code {http_code} - http status is {http_status}")

# WAP that accepts a git branch name and prints weather it is "main", "develop", or "featurebranch"
# input
git_branch_name = input("Enter git branch name:"  )

#Driving Factor
# condition 1: main
if git_branch_name == "main":
    git_status ="Main Branch"
elif git_branch_name == "develop":
    git_status = "Develop Branch"
else:
    git_status = "Feature Branch"

print(f"Git Branch Name {git_branch_name} - git branch status {git_status}")

#Expected output
# WAP that takes number of active users and prints "Low Load", "Medium Load", "High Load"
# input
active_users = int(input("Enter Active Users Numbers:"  ))

#Driving Factor
if active_users < 50:
    load_balance= "Low Load"
elif active_users >50 and active_users < 75:
    load_balance = "Medium Load"
elif active_users > 75 and active_users < 100:
    load_balance = "High Load"
else: 
    load_balance = "Unknown Load"


#Expected output
print(f"Active Users {active_users} - Load of Users {load_balance}")