import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='dockingFormatter',
    version='0.3.0',
    description='A docking logs formatter',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/LSWarss/dockingFormatter',
    author='Łukasz Stachnik',
    author_email='ls.warss98@gmail.com',
    license='MIT License',
    packages=setuptools.find_packages(),
    install_requires=['openpyxl'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)