# Auto-Python-Pack
A tiny tool that converts python code to packages (modules) using your setup.py file

Go to [releases](https://github.com/neek8044/Auto-Python-Pack/releases) and download the latest version

## Use
### Step 1
**Create a setup.py**
<br>
Example:
```
from setuptools import setup, find_packages

NAME = 'Local folder to pack'
AUTHOR = 'Your full name'
URL = 'https://github.com/your_username/your_repo'

VERSION = '0.2.5' 
DESCRIPTION = 'A python package'
LONG_DESCRIPTION = 'A longer description of the python package'

##############################
# Leave the following as is: #
setup(
        name = NAME, 
        version = VERSION,
        author = AUTHOR,
        url = URL,
        description = DESCRIPTION,
        long_description = LONG_DESCRIPTION,
        packages = find_packages(),
        
#                            #
##############################

# You may want to change those:

        classifiers = [
            "Development Status :: Alpha",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3"
        ]
)
```

### Step 2
Place pack.exe in the same folder as setup.py
<br>
setup.py should be under the root of the project to locate the folder as said above in the example.

### Step 3
Launch pack.exe
It may show a warning that it is malware/virus or similar stuff. It is completely safe though. If you still do not trust it, you can inspect pack.py and after being sure it is safe, copy it in the same folder as setup.py, then run it.

## Now what?
In the folder you are currently at, there sould have been created three more folders: dist, build, and egg-info.
<br>
To find your packages, go under dist and you sould see two files: a '.whl' (wheel) and a '.tar.gz' (compressed)

**You can now publish your pack to [pypi.org](https://pypi.org/)**
