from os.path import join, dirname, realpath
from setuptools import setup
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import sys

assert sys.version_info.major == 3 and sys.version_info.minor >= 6, \
    "The Spinning Up repo is designed to work with Python 3.6 and greater." \
    + "Please install it before proceeding."

with open(join("spinup", "version.py")) as version_file:
    exec(version_file.read())

"""pycolab PyPI package setup."""



try:
  import setuptools
except ImportError:
  from ez_setup import use_setuptools
  use_setuptools()
  import setuptools

# Warn user about how curses is required to play games yourself.
try:
  import curses
except ImportError:
  import warnings
  warnings.warn(
      'The human_ui module and all of the example games (when run as '
      'standalone programs) require the curses library. Without curses, you '
      'can still use pycolab as a library, but you won\'t be able to play '
      'pycolab games on the console.')

setup(
    name='spinup',
    py_modules=['spinup'],
    version=__version__,#'0.1',
    install_requires=[
        'cloudpickle==0.5.2',
        'gym[atari,box2d,classic_control]>=0.10.8',
        'ipython',
        'joblib',
        'matplotlib',
        'mpi4py',
        'numpy>=1.9',
        'pandas',
        'pytest',
        'psutil',
        'scipy',
        'seaborn==0.8.1',
	'six',
        'tensorflow>=1.8.0',
        'tqdm'
    ],
	
    description="Teaching tools for introducing people to deep RL.",
    author="Joshua Achiam",
)
