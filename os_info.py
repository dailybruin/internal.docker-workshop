import os

os_info =  os.uname()
print(f"Operating System: {os_info.sysname}, {os_info.release}")
print(f"Current Directory: {os.getcwd()}")
print("Contents:")
for f in os.listdir(os.getcwd()):
    print(f"- {f}")



