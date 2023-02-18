import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="p2pnetwork",
    version="1.2",
    author="Mckennah Palmer",
    author_email="mkpalm2006@gmail.com",
    description="peer-to-peer network application finder",
    url="currently not in github yet",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)