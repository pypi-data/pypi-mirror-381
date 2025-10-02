from setuptools import setup, find_packages

setup(
    name='data-clean-build-helper',
    version='0.0.1',
    author='Ashok ARC',
    author_email='ashok20akc@gmail.com',
    description='A helper library for building and managing data pipelines',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    python_requires='>3.6',
    install_requires=[
        'pandas',
    ],
)