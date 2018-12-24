import setuptools

#  with open("README.md", "r") as fh:
#      long_description = fh.read()

setuptools.setup(
    name="twaddress",
    version="0.0.1",
    author="mlouie",
    author_email="git@louie.lu",
    description="A package to translate Chinese address to English, using Taiwanese postal office format.",
    #  long_description=long_description,
    #  long_description_content_type="text/markdown",
    url="https://github.com/mlouielu/twaddress",
    packages=setuptools.find_packages(exclude=('test',)),
    include_package_data=True,
    install_requires = ['python-slugify>=1.2.0'],
    classifiers=[
                "Programming Language :: Python :: 3",
                "License :: OSI Approved :: MIT License",
                "Operating System :: OS Independent",
            
    ],

)
