from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Package to get data from animepahe including download links'
LONG_DESCRIPTION = 'This api can retrieve data about animes such as episode counts, release, scores, and download links for individual episodes.'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="weebAPI", 
        version=VERSION,
        author="Jonathan Shanmuganantham",
        author_email="<jshan9078@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['requests','re'], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'scraper'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Anime Watchers",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)