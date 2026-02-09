# Practice Problems
# 1. How do you check the installed python version using shell & python:
# In shell use : python --version or python3 --version

# print the python version using python
import sys
print("Python version", sys.api_version)
print("Python version ", sys.version_info)
print("Python version ", sys.version)

# python version using os module
import os
print("python version", os.popen('python --version').read().strip())

print("*" * 50) # scalar multiplication


#2. In shell, print the current username (whoami), in python use os.getlogin()
import os
print("Current Username:", os.getlogin())
print("Current working directory:", os.getcwd())
print("Process ID:", os.getpid())
print("Parent Process ID:", os.getppid())


print("*" * 50) # scalar multiplication


#4.In Shell, to get cpu count we use nproc, Write a script using psutil

#vmstat
#top

import psutil
print("CPU Count:", psutil.cpu_count(logical=True))
print("Memory Infos:", psutil.virtual_memory())

#Using nproc
#print("CPU Count using nproc:", os.popen('nproc').read().strip())

# Utility function to convert boot time to readable format

print("*" * 50) # scalar multiplication


#5. In shell, print system uptime (uptime), In Python, use psutil.boot_time()
print("System Uptime (seconds since boot):", psutil.boot_time())

# convert boot time to readable format
import time
boot_time_timestamp = psutil.boot_time()
bt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(boot_time_timestamp))
print("System Boot Time:", bt)

#pustil.boot_time() executes the below code
"""
def boot_time():
    #Return the system boot time expressed in seconds since the epoch.
    global BOOT_TIME
    path = f"{get_procfs_path()}/stat"
    with open_binary(path) as f:
        for line in f:
            if line.startswith(b'btime'):
                ret = float(line.strip().split()[1])
                BOOT_TIME = ret
                return ret
        msg = f"line 'btime' not found in {path}"
        raise RuntimeError(msg)
"""
print("*" * 50) # scalar multiplication

# List all environment variables in shell(printenv) . Do Use same in Python using os.environ

import os
print("Environment Variables:", os.environ)


# os.environ calls the below function from os module or package
"""
def _createenviron():
    if name == 'nt':
        # Where Env Var Names Must Be UPPERCASE
        def check_str(value):
            if not isinstance(value, str):
                raise TypeError("str expected, not %s" % type(value).__name__)
            return value
        encode = check_str
        decode = str
        def encodekey(key):
            return encode(key).upper()
        data = {}
        for key, value in environ.items():
            data[encodekey(key)] = value
    else:
        # Where Env Var Names Can Be Mixed Case
        encoding = sys.getfilesystemencoding()
        def encode(value):
            if not isinstance(value, str):
                raise TypeError("str expected, not %s" % type(value).__name__)
            return value.encode(encoding, 'surrogateescape')
        def decode(value):
            return value.decode(encoding, 'surrogateescape')
        encodekey = encode
        data = environ
    return _Environ(data,
        encodekey, decode,
        encode, decode)
"""