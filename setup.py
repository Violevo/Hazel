from setuptools import setup, find_packages

setup(
    name="lofty",
    version="0.1",
    packages=find_packages(),
    install_requires=[],  # List dependencies here
    author="Oliver Fisher",
    description="A python library focused on providing up to date insights and information on Hazel Lofty",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Violevo/Hazel",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
