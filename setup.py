from setuptools import setup
from wj import __version__
setup(name='wj',
      version=__version__,
      description='Tool for adding to and querying plain text task tracking files.',
      url='https://github.com/tdm-dev/wj',
      scripts=['scripts/wj'],
      author='Matthew Downton',
      license='MIT',
      packages=['wj'])
      
