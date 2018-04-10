from setuptools import setup

setup(name='plotgani',
      version='0.1',
      description='Personal plotting library in python',
      url='https://github.com/loungani/plotgani',
      author='David Loungani',
      author_email='davidcloungani@gmail.com',
      packages=['plotgani'],
      install_requires=[
          'numpy', 'pandas', 'matplotlib'
      ],
      zip_safe=False)