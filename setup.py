
from setuptools import setup, find_packages

VERSION = '0.9.1'
DESCRIPTION = 'Warehouse Transport Simulation'
LONG_DESCRIPTION = 'simulates and visualizes transport of loadunits in a warehouse environment. '

setup(
    name='ftsim',
    version=VERSION,
    author="Gerhard Sachs",
    author_email="<g.w.sachs@gmx.de>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    url = "https://github.com/gerpark/ftsim",
    license='MIT',
    keywords = ['tkinter', 'sqlite', 'threading'],
    packages=find_packages(include=['ftsim', 'ftsim.*']),
    package_data = {
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.db', '*.xml'],
        },
    entry_points={
        #                :  script=dir.file:function
        'console_scripts': ['ftsim=ftsim.ftmain9:ftmain'],
        },
    classifiers=[
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6'
    ]
    )
