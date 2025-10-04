from setuptools import setup, find_packages

setup(
    name="OT_knn",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "scanpy",
        "pandas",
        "ot",
        "anndata",
    ],
    python_requires='>=3.8',
)
