from setuptools import setup, find_packages

setup(
    name='Ferrum',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    author="David Ikeda",
    author_email="dev.literalgargoyle@gmail.com",
    description="Easy to use project package manager",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/literal-gargoyle/Francium",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
    ],
)