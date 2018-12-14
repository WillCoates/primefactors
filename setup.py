import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='primefactors',
    version='1.0.0',
    author='William Coates',
    author_email='me@willtc.uk',
    description='A library to find prime factors of integers',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/WillCoates/primefactors',
    packages=['primefactors'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
