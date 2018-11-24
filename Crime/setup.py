"""
try:
    from setuptools import setup
    from setuptools import Extension
	from Cyto
except ImportError:
    from distutils.core import setup
    from distutils.extension import Extension
"""

from setuptools import setup
from Cython.Build import cythonize

setup(
	ext_modules = cythonize("mycriteria.pyx")
)