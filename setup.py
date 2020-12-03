import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="evekillmail",
    version="0.0.1",
    author="evebreadcrumbs",
    description="Fetch and compress kill mails of eve online",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/evebreadcrumbs/evekillmail",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
