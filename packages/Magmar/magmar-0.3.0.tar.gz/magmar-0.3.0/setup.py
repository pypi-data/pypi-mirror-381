from setuptools import setup, find_packages

setup(
    name="Magmar",
    version="0.3.0",
    description = "Some cool tools to automate tasks in Tabular Data Analysis", 
    long_description= open("README.md").read(),
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "lightgbm",
        "scikit-learn",
        "tqdm"
    ],

    python_requires=">=3.7",
)