from setuptools import setup, find_packages

setup(
    name='algo',
    version='0.24',
    packages=["src"],
    install_requires=[
        # any dependencies required by your package
    ],
	package_dir={"": "src"},
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
