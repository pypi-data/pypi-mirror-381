import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='WebHelpersToPython',
    version='2.0',
    author='vova2f',
    author_email='vovk4756@gmail.com',
    description='помощники для пайтон',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/vova1f/WebHelpersToPython',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',
    install_requires=[
        'colorama==0.4.6',
        'requests==2.32.5'
    ]
)