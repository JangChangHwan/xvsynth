from distutils.core import setup
from distutils import msvc9compiler
msvc9compiler.VERSION = 10.0
from Cython.Build import cythonize

setup(
name = 'xvEngine App',
ext_modules = cythonize("_XVSynth.pyx"),
)
