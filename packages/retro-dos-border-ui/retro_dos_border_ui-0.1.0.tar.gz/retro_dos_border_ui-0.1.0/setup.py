from setuptools import setup, find_packages

setup(
    name="retro-dos-border-ui",
    version="0.1.0",
    author="Mark van der Puil",
    author_email="retro_dos_border_ui@markovanderpuil.nl",
    description="A retro DOS-style console UI library using curses.",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
