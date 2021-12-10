from setuptools import setup

with open("requirements.txt", "r") as fh:
   requirements = fh.readlines()

setup(name='pyjsta',
      version='0.1',
      description='Mostly some rstats clone functions',
      url='http://github.com/jsta/pyjsta',
      author='jsta',
      author_email='stachl2@msu.edu',
      license='MIT',
      packages=['pyjsta'],
      install_requires=[req for req in requirements if req[:2] != "# "],
      zip_safe=False)
