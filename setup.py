import setuptools

setuptools.setup(
    name="nbpawspublic",
    version='0.1.1',
    url="https://github.com/toolforge/nbpawspublic",
    author="Yuvi Panda",
    packages=setuptools.find_packages(),
    install_requires=[
        'notebook',
    ],
    package_data={'nbpawspublic': ['static/*']},
)

