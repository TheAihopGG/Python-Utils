from setuptools import setup, find_packages


setup(
    name="python_utils",
    version="1.0.0",
    author="theaihopgg",
    author_email="theaihopgg@gmail.com",
    description="Python utils",
    long_description=open("./README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],
    keywords="utils versions python",
    python_requires=">=3.12",
)
