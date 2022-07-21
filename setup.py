import setuptools
 
with open("README.md", "r") as fh:
    long_description = fh.read()
 
setuptools.setup(
    name="process_pcap",
    version="0.0.1",
    author="Cliff Duffey",
    author_email="cliff.duffey@pm.me",
    description="Package to process PCAP files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['pypcapkit', 'ipaddress', 'requests'],
    python_requires='>=3.7',
)