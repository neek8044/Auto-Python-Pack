import os
from colorama import Fore, Style

F = Fore # Changes the foreground color of the text (F.COLOR)
SR = Style.RESET_ALL # Resets any color applied to the text

if __name__ == '__main__':
    os.system('cls >nul')

    # installing and/or upgrading wheel and setuptools via pip
    print(f'{F.CYAN}--> Updating libraries...{SR}')
    os.system('pip install wheel setuptools >nul')
    os.system('pip install wheel --upgrade >nul')
    os.system('pip install setuptools --upgrade >nul')

    print(f"{F.CYAN}--> Building packages with 'setup.py'...{SR}")
    # building tar package with sdist
    os.system('python setup.py sdist')
    print(f"{F.CYAN}--> Created tar file{SR}")

    # building whl package with bdist_wheel
    os.system('python setup.py bdist_wheel')
    print(f"{F.CYAN}--> Created whl file{SR}")

    print("")
    print(f"{F.CYAN}Building complete. Files can be found under the local 'dist/' folder{SR}")

    input(f'{F.CYAN}Press ENTER to exit.{SR}')
else:
    print(f"{F.CYAN}--> Script 'build.py' was called but not run as 'main'{SR}")
    input(f'{F.CYAN}--> Press ENTER to exit.{SR}')