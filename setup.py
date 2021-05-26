import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="writefull",
    version="0.0.0",
    author="Writefull",
    author_email="support@writefull.com",
    description="A Python library for the Writefull API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/writefull/writefull-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)