from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="behind-api-client",  # Change this to your unique package name
    version="1.0.663",
    author="Henry Fisher",
    author_email="henry.fisher.kundy@gmail.com",
    description="Generated API client for Behind API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hank/behind-api-client",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.31.0",
    ],
)