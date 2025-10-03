"""
Setup configuration for label-studio-sso package
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="label-studio-sso",
    version="1.0.0",
    author="Things-Factory Integration Team",
    author_email="admin@hatiolab.com",
    description="Generic JWT SSO integration for Label Studio - works with any JWT-based system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hatiolab/label-studio-sso",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Framework :: Django",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "Framework :: Django :: 4.1",
        "Framework :: Django :: 4.2",
    ],
    python_requires=">=3.8",
    install_requires=[
        "Django>=3.2",
        "PyJWT>=2.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-django>=4.5",
            "black>=22.0",
            "flake8>=4.0",
        ],
    },
    keywords="label-studio sso jwt things-factory authentication",
    project_urls={
        "Bug Reports": "https://github.com/hatiolab/label-studio-sso/issues",
        "Source": "https://github.com/hatiolab/label-studio-sso",
        "Documentation": "https://github.com/hatiolab/label-studio-sso/blob/main/README.md",
    },
)
