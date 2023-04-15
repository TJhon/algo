from setuptools import setup, find_packages

setup(
    name='NOMBRE_DEL_PAQUETE',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'NOMBRE_DEL_PAQUETE=NOMBRE_DEL_PAQUETE.main:main'
        ]
    },
    install_requires=[
        # Lista de las dependencias que tu paquete necesita
    ],
)