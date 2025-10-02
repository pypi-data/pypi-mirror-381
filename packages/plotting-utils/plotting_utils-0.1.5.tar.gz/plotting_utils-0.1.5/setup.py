from setuptools import setup, find_packages

# Read the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='plotting_utils',
    version='0.1.5',
    author='andrecossa5',
    description='Elegant wrappers around matplotlib and seaborn for scientific plotting',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/andrecossa5/plotting_utils',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'seaborn',
        'matplotlib',
        'statannotations',
        'textalloc',
        'joblib',
        'scikit-learn'
    ],
)