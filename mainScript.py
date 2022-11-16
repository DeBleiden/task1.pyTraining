import os
import platform


def showOSName():
    print(os.name, "|", platform.release(), "|", platform.version())


showOSName()
