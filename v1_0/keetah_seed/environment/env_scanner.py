import sys
import platform
import os

def scan_environment():

    env = {}

    env["python_version"] = sys.version
    env["platform"] = platform.system()
    env["working_directory"] = os.getcwd()
    env["files"] = os.listdir()

    return env