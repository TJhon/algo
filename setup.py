from setuptools import setup, find_packages

setup(
    name='algo',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'algo=algo.main:main'
        ]
    },
    install_requires=[
        # Lista de las dependencias que tu paquete necesita
    ],
)