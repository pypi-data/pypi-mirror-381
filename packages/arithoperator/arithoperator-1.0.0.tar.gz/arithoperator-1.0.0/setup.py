from setuptools import setup, find_packages

setup(
    name="arithop",
    version="1.0.0",
    author="Your Name",
    author_email="you@example.com",
    description="A simple Python package to perform arithmetic operations on multiple numbers.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "arithop = arithop.__main__:main"
        ]
    },
)
