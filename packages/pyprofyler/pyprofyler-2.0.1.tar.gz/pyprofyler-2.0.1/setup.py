from os.path import exists
from setuptools import setup
setup(
	name='pyprofyler',
	version='2.0.1',
	author='Aly Shmahell',
	url='https://github.com/AlyShmahell/PyProfyler',
	description='a simple memory/perf profiler for python programs.',
	long_description=(open('README.md', encoding='utf-8').read() if exists('README.md')
                        else ''),
    long_description_content_type='text/markdown',
	packages=['pyprofyler'],
	install_requires=[
			  "psutil==7.1.0",
			  "numpy==2.3.3"
			],
    python_requires='>=3.12.9',
	classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)