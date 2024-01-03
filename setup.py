from setuptools import setup, find_packages

setup(
    name='dataanalysistoolkit',
    version='0.2',
    packages=find_packages(),
    description='The `DataAnalysisToolkit` project is a Python-based data analysis tool designed to streamline various data analysis tasks. It allows users to load data from CSV files and perform operations such as statistical calculations, outlier detection, data cleaning, and visualization.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Thaddeus Thomas',
    author_email='thaddeus.r.thomas@gmail.com',
    url='https://github.com/thomasthaddeus/dataanalyzer',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.8',
)
