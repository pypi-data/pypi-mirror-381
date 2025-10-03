from setuptools import find_packages, setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name='calcyoulater2',
    version='2.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',
    description='A Flask-based calculator web app',
    url='https://github.com/M-Nwanze/calcyoulater-pkg',
    author='Mike',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)   
