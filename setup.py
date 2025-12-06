from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='sphinx-molview',
    version='0.1.0',
    author='Jie Huang',
    author_email='your.email@example.com',
    description='A Sphinx extension for interactive 3D molecular visualization',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/huangchieh/sphinx-molview',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'sphinx_molview': ['static/*.js'],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Sphinx :: Extension',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Scientific/Engineering :: Chemistry',
        'Topic :: Scientific/Engineering :: Physics',
    ],
    python_requires='>=3.8',
    install_requires=[
        'sphinx>=4.0',
    ],
)
