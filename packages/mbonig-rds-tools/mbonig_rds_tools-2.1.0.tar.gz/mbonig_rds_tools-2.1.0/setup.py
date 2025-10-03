import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "mbonig-rds-tools",
    "version": "2.1.0",
    "description": "A construct for working with RDS SQL servers",
    "license": "MIT",
    "url": "https://github.com/mbonig/rds-tools",
    "long_description_content_type": "text/markdown",
    "author": "Matthew Bonig<matthew.bonig@gmail.com>",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/mbonig/rds-tools.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "mbonig.rds_tools",
        "mbonig.rds_tools._jsii"
    ],
    "package_data": {
        "mbonig.rds_tools._jsii": [
            "rds-tools@2.1.0.jsii.tgz"
        ],
        "mbonig.rds_tools": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.9",
    "install_requires": [
        "aws-cdk-lib>=2.200.0, <3.0.0",
        "constructs>=10.0.5, <11.0.0",
        "jsii>=1.114.1, <2.0.0",
        "publication>=0.0.3",
        "typeguard>=2.13.3,<4.3.0"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Typing :: Typed",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
