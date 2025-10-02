from setuptools import setup, find_packages

setup(
    name="XVideoDownloader",
    version="0.1.0",
    description="Python wrapper for X (Twitter) video downloader API",
    author="0600011",
    packages=find_packages(),
    install_requires=[
        "requests>=2.0.0",
    ],
)