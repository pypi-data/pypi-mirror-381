from setuptools import setup, find_packages
import os

# Read the contents of README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="ai-dbug",
    version="0.1.0",
    author="Jithu Baiju",
    author_email="jithubaiju124@gmail.com",
    description="AI-powered Python debugger that explains errors in plain English",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jithubaiju55/ai-dbug",
    project_urls={
        "Bug Tracker": "https://github.com/jithubaiju55/ai-dbug/issues",
        "Documentation": "https://github.com/jithubaiju55/ai-dbug#readme",
        "Source Code": "https://github.com/jithubaiju55/ai-dbug",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Debuggers",
        "Topic :: Education",
    ],
    python_requires=">=3.7",
    install_requires=[],
    extras_require={
        "color": ["rich>=10.0.0"],
        "full": ["rich>=10.0.0", "colorama>=0.4.4"],
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=22.0.0",
            "flake8>=5.0.0",
            "mypy>=0.990",
            "build>=0.10.0",
            "twine>=4.0.0",
        ],
    },
    keywords="debugging errors ai developer-tools traceback error-handling",
)