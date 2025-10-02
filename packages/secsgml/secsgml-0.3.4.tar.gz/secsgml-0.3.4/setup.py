from setuptools import setup, find_packages

setup(
    name="secsgml",
    version="0.3.4",
    author="John Friedman",
    author_email="johnfriedman@datamule.xyz",
    description="Parse Securities and Exchange Commission Standard Generalized Markup Language (SEC SGML) files",
    license="MIT",
    packages=find_packages(),
    python_requires=">=3.6",
)