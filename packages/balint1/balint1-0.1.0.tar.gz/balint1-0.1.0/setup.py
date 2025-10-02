from setuptools import setup, find_packages

setup(
    name='balint1',                       # Csomag neve
    version='0.1.0',                      # Verzió
    packages=find_packages(),             # Automatikus csomaggyűjtés
    description='Páros vagy páratlan szám eldöntő modul',
    author='A TE NEVED',
    author_email='te@email.com',
    install_requires=[],                  # Függőségek, ha vannak
)