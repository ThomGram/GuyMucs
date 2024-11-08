from setuptools import setup, find_packages

setup(
    name="guymucs",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "demucs",
        "PyQt5",
        "pytest"
    ],
    entry_points={
        "console_scripts": [
            "guymucs = guymucs.main:main"
        ]
    },
    description="Interface graphique pour la séparation audio avec Demucs",
)
