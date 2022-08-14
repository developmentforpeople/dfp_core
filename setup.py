from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in dfp_core/__init__.py
from dfp_core import __version__ as version

setup(
	name="dfp_core",
	version=version,
	description="DFP Core Tools",
	author="DFP",
	author_email="developmentforpeople@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
