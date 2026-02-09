#convert a list of server IPs into a tuple and explain why immutability is preferred
#input
server_ips_list = ["10.10.10.1", "10.10.10.2", "10.10.10.3"]

#Driving Factor
server_ips_tuple = tuple(server_ips_list)

# output
print("Server ips tuple:",server_ips_tuple)
print("#" * 50)

# Given a dictionary of {service:port}, convert it into a string
# scenrio-1
#input
dict_service_port = {"service_1":8000, "service_2":3000, "service_3":4000}


# driving factor
dict_to_str_service_port = ", ".join(f"{service}:{port}" for service,port in dict_service_port.items())
#output 
print("dict to str:", dict_to_str_service_port)

# scenrio-2
import json
res = json.dumps(dict_service_port)
print("dict to str:", res)

print("#" * 50)

# Parse a string "80, 443,22" into a list of integers

#input
str_obj = "80,443,22"

# Driving Factor
str_obj_to_list = [int(x) for x in (str_obj.split(','))]

#output
print("str to list:", str_obj_to_list)
print("#" * 50)

# Convert CPU usage from string "78.5" to a float and compare a threshold (e.g 80)

def is_cpu_over_threshold(cpu_str, threshold=80):
    return float(cpu_str) >= threshold

print(is_cpu_over_threshold("78.5"))  # False
print(is_cpu_over_threshold("85.2"))  # True

# Given a list of pod names, convert them into a set to remove duplicates
def pod_names_list(pod_list):
    return set(pod_list)

print(pod_names_list(["Pod1","Pod2","Pod3","Pod1","Pod2"]))

print("#" * 50)

#convert a YAML like dictionary {"server":"app01","port":"8080"} so that port becomes an integer
def convert_Port_num(yaml_port):
    yaml_port["port"] = int(yaml_port["port"])
    return yaml_port
print(convert_Port_num({"server":"app01","port":"8080"}))

print("#" * 50)

# Given a list of strings ["10", "20", "30"], convert all items to integers and calculate the sum.
def convert_list_to_int_sum(list_str):
    res =0
    for i in list_str:
        res+=int(i)
    return res
print(convert_list_to_int_sum(["10","20","30"]))

print("#" * 50)
# Convert a boolean string "True/False" into a Python boolean.

def convert_Str_bool(str):
    return str.strip().lower() == "true"
print(convert_Str_bool("True"))
print(convert_Str_bool("False"))
print("#" * 50)

#Access the first 3 server IPs from a list using slicing
# example ["10.10.10.1", "10.10.10.2","10.10.10.3", "10.10.10.4"][:3]
def first_3_server_ips(list_item):
    return list_item[:3]
print(first_3_server_ips(["10.10.10.1", "10.10.10.2","10.10.10.3", "10.10.10.4"]))
print("#" * 50)

# Extract the last 2 pod names from a list of pods
def last_2_pod_list(list_pod):
    return list_pod[-2:]
print(last_2_pod_list(["Pod1","Pod2","Pod3","Pod4"]))
print("#" * 50)

# From a log message string "ERROR: Pod Creashed at 10:00", slice to get only "ERROR".
def extract_str_message(str):
    return str.split(":")[0]
print(extract_str_message("ERROR: Pod Creashed at 10:00"))
print("#" * 50)

# Extract every alternate and reverse service name from a list of services
# services = ["nginx", "mysql", "redis","kafka","elasticsearch","prometheus","grafana"]
def reverse_service(list_service):
    return list_service[::2][::-1]
print(reverse_service(["nginx", "mysql", "redis","kafka","elasticsearch","prometheus","grafana"]))
print("#"*50)

#From a string log"2025-09-08T10:20:30Z", slice out only the date "2025-09-08"
def date_str_fun(str_date):
    return str_date.split("T")[0]
print(date_str_fun("2025-09-08T10:20:30Z"))

print("#" * 50)
#Given a list of ports [22, 80,443, 3306,8080], slice the middle three ports
def middle_list_ports(list_ports):
    return list_ports[1:4]
print(middle_list_ports([22, 80,443, 3306,8080]))
print("#"*50)

#From a long command string "kubectl get pods --namespace=prod", slice to extract only "get pods"
def long_command_str(command_str):
    return " ".join(command_str.split()[1:3])
print(long_command_str("kubectl get pods --namespace=prod"))