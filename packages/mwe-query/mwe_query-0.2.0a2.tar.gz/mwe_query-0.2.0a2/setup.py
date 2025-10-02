from setuptools import setup, find_packages

with open('README.md') as file:
    long_description = file.read()

setup(
    name='mwe-query',
    python_requires='>=3.9, <4',
    version='0.2.0a2',
    description='',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Martin Kroon / Jan Odijk / Research Software Lab, Centre for Digital Humanities, Utrecht University',
    author_email='digitalhumanities@uu.nl',
    url='https://github.com/CentreForDigitalHumanities/mwe-query',
    license='CC BY-NC-SA 4.0',
    include_package_data=True,
    packages=['mwe_query'],
    package_data={"mwe_query": ["py.typed"]},
    zip_safe=True,
    install_requires=[
        'alpino-query>=2.1.8', 'requests', 'BaseXClient', 'sastadev>=0.1.4', 'pivottablejs', 'pandas'
    ],
    entry_points={
        'console_scripts': [
            'mwe-query = mwe_query.__main__:main'
        ]
    })
