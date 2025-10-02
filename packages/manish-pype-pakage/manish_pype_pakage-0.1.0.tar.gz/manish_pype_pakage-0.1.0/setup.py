from setuptools import setup, find_packages

setup(
    name="manish_pype_pakage",  # package name (pip install accidentrisk)
    version="0.1.0",
    author="manish",
    description="A simple python pakage for sigmoid function",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
   # GitHub repo (optional)
    packages=find_packages(),
    install_requires=[
        "numpy>=1.21.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
