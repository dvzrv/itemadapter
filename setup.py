import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="itemadapter",
    version="0.8.0",
    license="BSD",
    description="Common interface for data container classes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Eugenio Lacuesta",
    author_email="eugenio.lacuesta@gmail.com",
    url="https://github.com/scrapy/itemadapter",
    packages=["itemadapter"],
    package_data={
        "itemadapter": ["py.typed"],
    },
    include_package_data=True,
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Framework :: Scrapy",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
