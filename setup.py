from distutils.core import setup

files = ["stuff/*"]

setup (
    name='FirstPythonPackage',
    version='0.2.1',
    packages=['firstpythonpackage',],
    package_data = {'package' : files },    
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.txt').read(),
)
