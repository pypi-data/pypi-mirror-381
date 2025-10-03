from setuptools import setup, find_packages

setup(
    name="florrcalc",  # Naam van je package
    version="26.0.0",
    author="The florrOS Project",
    author_email="florros.developing@gmail.com",
    description="A petal crafting calculator for florrr.io, now on PyPI!",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/cubinghater/florrcalc-python",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[],
    entry_points={
        "console_scripts": [
            "florrcalc=florrcalc.main:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
