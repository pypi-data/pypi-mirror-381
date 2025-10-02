from setuptools import setup, find_packages

setup(
    name="ske",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "ske = ske.main:main",
        ],
    },
    author="sky",
    description="XOR ENCRYPTOR",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/twoj_repo/ske",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
