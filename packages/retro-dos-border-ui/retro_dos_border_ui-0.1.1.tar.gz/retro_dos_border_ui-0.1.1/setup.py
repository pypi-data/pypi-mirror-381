from setuptools import setup, find_packages

setup(
    name="retro-dos-border-ui",
    version="0.1.1",
    author="Marko van der Puil",
    url="https://github.com/markovanderpuil/retro-dos-border-ui",
    description="A retro DOS-style console UI library using curses.",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
