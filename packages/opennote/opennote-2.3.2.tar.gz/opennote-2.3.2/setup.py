import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="opennote",
    version="2.3.2",
    author="Opennote, Inc.",
    license="MIT",
    author_email="devtools@opennote.me",
    description="Opennote Python SDK",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/opennote-dev/api-sdk-python",
    packages=setuptools.find_packages(),
    install_requires=[
        "requests",
        "pydantic",
        "httpx"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
