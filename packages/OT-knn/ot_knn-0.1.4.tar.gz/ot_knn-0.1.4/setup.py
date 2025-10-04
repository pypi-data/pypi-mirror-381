from setuptools import setup, find_packages

setup(
    name="OT_knn",
    version="0.1.4",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "scanpy",
        "pandas",
        "pot",
        "anndata",
    ],
    python_requires='>=3.8',
)
