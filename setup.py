from distutils.core import setup

files = ["stuff/*"]

setup (
    name='FirstPythonPackage',
    version='0.2.4',
    packages=['firstpythonpackage',],
    package_data = {'firstpythonpackage' : files },    
#    data_files=[('/home/a',['bashy.sh'])],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.txt').read(),
)
