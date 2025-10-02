import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "aws-cdk.cli-lib-alpha",
    "version": "2.1029.4.a0",
    "description": "AWS CDK Programmatic CLI library",
    "license": "Apache-2.0",
    "url": "https://github.com/aws/aws-cdk",
    "long_description_content_type": "text/markdown",
    "author": "Amazon Web Services",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/aws/aws-cdk-cli"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "aws_cdk.cli_lib_alpha",
        "aws_cdk.cli_lib_alpha._jsii"
    ],
    "package_data": {
        "aws_cdk.cli_lib_alpha._jsii": [
            "cli-lib-alpha@2.1029.4-alpha.0.jsii.tgz"
        ],
        "aws_cdk.cli_lib_alpha": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.9",
    "install_requires": [
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
        "Development Status :: 7 - Inactive",
        "License :: OSI Approved",
        "Framework :: AWS CDK",
        "Framework :: AWS CDK :: 2"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
