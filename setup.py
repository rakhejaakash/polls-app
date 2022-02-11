from importlib.machinery import SourceFileLoader

import setuptools

with open("README.md", encoding="utf-8") as fp:
    readme = fp.read()


version = SourceFileLoader("version", "src/version.py").load_module().VERSION

setuptools.setup(
    name="polls-app",
    version=version,
    description="Polls App",
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=["django==3.2.12"],
    extras_require={"dev": ["pre-commit==2.7.1"]},
    python_requires=">=3.7",
)
