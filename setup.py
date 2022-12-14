from setuptools import setup
with open("README.md","r") as fh:
    long_description = fh.read()

setup(
    name='primosalonzo1',
    version='0.0.1',
    description='Enlista todos los primos desde 1 hasta un numero n',
    py_modules=["primosalonzo1"],
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Operating System :: OS Independent",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GermanAlonzo/ModuloPrimosAlonzo1",
    author="German Alonzo",
    author_emial="german.andres.alonzo@gmail.com",
)