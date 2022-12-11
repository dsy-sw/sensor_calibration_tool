import platform

def create_virtual_env(env_name:str):
    pass

def pre_exe_linux():
    os.popen('list').read()
    pass

def pre_exe_windows():
    subprocess.call("")
    pass

if __name__ == "__main__":
    os_platform = platform.system()
    if os_platform == "Windows":
        import os
        pre_exe_windows()
    elif os_platform == "Linux":
        import subprocess
        pre_exe_linux()