# WAP that takes server name and IP as input and prints: "Server {name} is running at {IP}"
server_name = input("Enter Server name: ")
server_ip = input("Enter Server IP: ")
print(f"Server {server_name} is running at {server_ip}")
print("#" * 50)

# Format a string to print CPU usage, Memory usage and Disk Usage in a tabular way.
cpu_usage = input("Enter CPU Usage (%): ")
memory_usage = input("Enter Memory Usage (%): ")
disk_usage = input("Enter Disk Usage (%): ")
print(f"{'Resource':<10} {'Usage (%)':<10}")
print(f"{'CPU':<10} {cpu_usage:<10}")
print(f"{'Memory':<10} {memory_usage:<10}")
print(f"{'Disk':<10} {disk_usage:<10}")

print("#" * 50)

# Given a username and environment(dev/stage/prod), format a string to print "Deploying app as {user} on {env}"
username = input("Enter the username: ")
environment = input("Enter the environment (dev/stage/prod): ")
print(f"Deploying app as {username} on {environment}")
print("#" * 50)

#Use f-string to format log messages: "Timestamp:{time}, Status: {status}, Response Time:{ms} ms"
import datetime
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
status = "200 OK"
response_time_ms = 150
print(f"Timestamp: {timestamp}, Status: {status}, Response Time: {response_time_ms} ms")
print("#" * 60)

# WAP that prints the top 3 running processes with aligned columns(PID,Name,CPU%)
import psutil

# Get all processes with pid, name, cpu usage
processes = []
for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
    processes.append(proc.info)

# Sort by CPU usage (descending)
top_processes = sorted(
    processes, key=lambda x: x['cpu_percent'], reverse=True
)[:3]

# Print table
print(f"{'PID':<8}{'Name':<25}{'CPU (%)':>10}")
print("-" * 45)

for p in top_processes:
    print(f"{p['pid']:<8}{p['name']:<25}{p['cpu_percent']:>10}")

print("#"*50)

#WAP that displays API status:"Endpoint {url} returend {status_code} in {time:.2f} seconds"
api_url = input("Enter the Endpoint api url: ")
status_code = int(input("Enter the status code: "))
time_of_response = float(input("Enter the response time of ms: "))
print(f"Endpoint  {api_url} returned {status_code} in {time_of_response}")
print("#"*50)

#WAP that aligns log levels (INFO, WARNING, ERROR) into a formatted column view.
log_levels = [
    ("INFO", "Server started"),
    ("WARNING", "High memory usage"),
    ("ERROR", "Pod crashed")
]
for level, message in log_levels:
    print(f"{level:<10} | {message}")

print("#"*50)

#WAP that takes deployment duration and formats it as "Deployment took {minutes}m {seconds}s"
duration = int(input("Enter deployment duration in seconds: "))
minutes = duration//60
seconds = duration % 60
print(f"Deployment took {minutes}m {seconds}s")
print("#"*50)

#WAP that prints disk usage with 3 decimal precision: "Disk used: {used:.2f}GB/{total:.2f}GB"
def print_disk_usage(used, total):
    percent = (used / total) * 100
    print(f"Disk used: {used:.3f}GB/{total:.3f}GB ({percent:.2f}%)")

print_disk_usage(125.45678, 256.98765)