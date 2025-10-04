from setuptools import setup, find_packages
setup(
    name='mcss_package',
    version='0.1.0',
    packages=find_packages(),
    install_requires=['numpy', 'pandas', 'PyYAML'],
    python_requires='>=3.8',
    author='Your Name',
    description='MCSS Clustering Analysis package',
    url='https://github.com/yourusername/mcss_package',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
