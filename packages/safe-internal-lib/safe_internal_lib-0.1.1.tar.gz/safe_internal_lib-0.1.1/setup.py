from setuptools import setup, find_packages

setup(
    name="safe_internal_lib",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "safe-hello=safe_internal_lib:hello",
        ],
    },
)

