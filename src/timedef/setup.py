from setuptools import setup, find_packages

setup(
    name='timedef',
    version='0.0.1',
    description='This package provides a decorator function `timedef` that can be used to measure the execution time of other functions in Python.',
    author='Cleyton Pedroza',
    author_email='cleytonpedroza@gmail.com',
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)
