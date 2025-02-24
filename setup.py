from setuptools import setup, find_packages

# Read dependencies from the requirements.txt file
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

# Configuration of setup.py
setup(
    name="hw02",
    version="0.1.0",
    packages=find_packages(),
    install_requires=requirements,
    description="Dictionary Generatione",
    author="Iñigo Exposito, Deepak Malik, Enzo Infantes",
    author_email="inigo.exposito@bse.eu, eepak.malik@bse.eu, enzo.infantes@bse.eu",
    url="https://github.com/Enzo280100/textmining_hw02",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)

