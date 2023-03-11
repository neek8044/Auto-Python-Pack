import os
try:
    from colorama import Fore, Style
except ImportError:
    print("Module 'colorama' is not available. Run 'pip3 install colorama' to install it.")

F = Fore # Changes the foreground color of the text (F.COLOR)
SR = Style.RESET_ALL # Resets any color applied to the text

if __name__ == '__main__':
    # installing and/or upgrading wheel and setuptools via pip
    print(f'{F.CYAN}--> Updating libraries...{SR}')
    os.system('pip3 install wheel setuptools >nul')
    os.system('pip3 install wheel --upgrade >nul')
    os.system('pip3 install setuptools --upgrade >nul')

    # building tar package with sdist
    print(f"{F.CYAN}--> Building packages with 'setup.py'...{SR}")
    os.system('python3 setup.py sdist')
    print(f"{F.CYAN}--> Created tar file{SR}")

    # building whl package with bdist_wheel
    os.system('python3 setup.py bdist_wheel')
    print(f"{F.CYAN}--> Created whl file{SR}")

    print(f"\n{F.CYAN}Building complete. Files can be found under the local 'dist/' folder{SR}")

else:
    print(f"{F.CYAN}--> Script 'build.py' was called but not run as 'main'{SR}")
    
input(f'{F.CYAN}Press ENTER to exit.{SR}')
