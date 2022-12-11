import shutil
import sys
import os

class Loader:

    def __init__(self):
        self.site_packages = os.path.dirname(os.path.realpath(sys.executable)) + "\\Lib\\site-packages"

    def fix_libs(self):
        for root, dirs, files in os.walk("LibFixer"):
            for file in files:
                full_path = os.path.join(root, file)
                relative_path = full_path.replace("LibFixer\\", "")
                destination = self.site_packages + "\\" + relative_path
                print("Copying " + file)
                shutil.copy(full_path, destination)
                
