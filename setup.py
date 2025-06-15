import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="lulo",
    version="1.0",
    description="Lulo API Python client",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/spacesudo/lulo",
    author="Dave",
    author_email="loony12_haricot@icloud.com",
    
    license="MIT",
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
    ],
    packages=["lulo"],
    include_package_data=True,
    install_requires=["requests", "pydantic"],
    keywords='lulo, solana, development, staking',
    python_requires='>=3.6, <4',

    project_urls={
        "GitHub": "https://github.com/spacesudo/lulo",
        "Twitter": "https://twitter.com/neverdusted",  
        "Documentation": "https://dev.lulo.fi/",
    }
)
