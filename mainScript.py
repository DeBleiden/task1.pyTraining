import os
import platform


def showOSName():
    print(os.name, "|", platform.system(), "|", platform.release(), "|", platform.version())
    print(platform.uname())


showOSName()
