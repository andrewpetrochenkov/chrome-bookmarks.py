import setuptools

setuptools.setup(
    name='chrome-bookmarks',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
