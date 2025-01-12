from setuptools import setup, find_packages

setup(
    name="dice-roller",  # Package name
    version="1.0.0",  # Version
    description="A Python module for rolling dice with optional advantage or disadvantage.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Themadpunter",
    author_email="themadpunter@proton.me",
    url="https://github.com/familycomicsstudios/dice",  # Replace with your GitHub repo
    license="MIT",
    packages=find_packages(),
    install_requires=[],  # Add dependencies if needed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "dice=dice.dice:main",  # CLI tool
        ],
    },
)
