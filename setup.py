from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='pdfn2tex',
      version='0.0.00',
      description='A PDF into latex converter',
      author='Keith Murray',
      author_email='kmurrayis@gmail.com',
      license='MIT',
      packages=['pdfn2tex'],
      install_requires=[
      ],
      include_package_data=True,
      zip_safe=False)
