from setuptools import setup, find_packages

setup(
    name="ubicoders-vrobots-msgs",                 # PyPI name (must be unique)
    version="2.0.0",                     # update as needed
    description="Message definitions for VROBOTS in Python",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Elliot Lee",
    author_email="info@ubicoders.com",
    license="MIT",
    url="https://github.com/ubicoders0/vrobots_msgs",  # update if hosted
    packages=find_packages(where="."),   # discovers vrobots_msgs/
    package_dir={"": "."},               # package root is current folder
    python_requires=">=3.8",
    install_requires=[
        "numpy>2.0.0",
        "flatbuffers==23.5.26"
    ],
    
)
