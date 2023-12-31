from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in health_api/__init__.py
from health_api import __version__ as version

setup(
	name="health_api",
	version=version,
	description="Helth Api",
	author="IT Systematic",
	author_email="sales@itsystematic.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
