from setuptools import setup, find_packages

setup(
    name="cmessage",
    version="0.2.5",
    packages=find_packages(),
    description="Simple ctypes-based MessageBox wrapper for Windows",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    url="https://github.com/yourusername/cmessage",  
    python_requires=">=3.4",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
        "License :: OSI Approved :: MIT License",
        "Topic :: Utilities",
    ],
)
