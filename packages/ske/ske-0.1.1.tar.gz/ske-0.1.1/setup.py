from setuptools import setup, find_packages

setup(
    name="ske",
    version="0.1.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "ske = ske.main:main",
        ],
    },
    author="sky",
    description="Simple XOR file encryptor (.ske)",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    python_requires='>=3.8',
)
