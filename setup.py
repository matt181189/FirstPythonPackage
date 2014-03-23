from distutils.core import setup

files = ["stuff/*"]

setup (
    name='FirstPythonPackage',
    version='0.2.2',
    packages=['firstpythonpackage',],
    package_data = {'firstpythonpackage' : files },    
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.txt').read(),
)
