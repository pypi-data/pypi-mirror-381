from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='defuse',
    version='0.1.1',
    packages=find_packages(),
    description='Detect unused Python functions and generate usage reports',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Peter Sinkovicz',
    author_email='antsticky@gmail.com',
    url='https://github.com/antsticky/defuse',
    entry_points={
    'console_scripts': [
        'defuse=defuse.cli:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
    ],
    python_requires='>=3.6',
)
