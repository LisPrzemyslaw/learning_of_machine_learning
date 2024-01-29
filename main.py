import site
import sys


def main():
    _SITE_PACKAGES_INDEX = 1 if sys.platform == "win32" else 0
    _VENV_PATH = site.getsitepackages()[_SITE_PACKAGES_INDEX]


if __name__ == '__main__':
    main()
