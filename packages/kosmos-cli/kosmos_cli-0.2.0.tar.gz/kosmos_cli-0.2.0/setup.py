from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="kosmos-cli",
    version="0.2.0",
    author="IndenScale",
    author_email="hfu7565ytru@gmail.com",
    description="A powerful CLI tool for interacting with Kosmos knowledge base system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/IndenScale/Kosmos",
    packages=find_packages(include=['cli', 'cli.*']),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Utilities",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.25.1",
        "python-dotenv>=0.19.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "isort>=5.0",
            "flake8>=3.9",
        ],
    },
    entry_points={
        "console_scripts": [
            "kosmos=cli.main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "cli": ["*.md", "*.txt"],
    },
)