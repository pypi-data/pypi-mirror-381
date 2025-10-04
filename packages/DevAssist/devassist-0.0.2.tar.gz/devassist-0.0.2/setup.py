from setuptools import setup, find_packages

setup(
    name="DevAssist",
    version="0.0.2",
    author="Tensor Py Ops",
    author_email="TensorPyOps@outlook.com",
    description="Auxiliary development tools or services",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/TensorPyOps/DevAssist",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[],
)