import setuptools 

with open("C:/Users/Miles/AppData/Local/Programs/Python/Python311/texttoolspy/README.md", "r") as fh: 
    long_description = fh.read() 

    setuptools.setup(  
	name="texttoolspy", 
	version="0.0.7",  
	author="MilesWK", 
	author_email="your_name@example.com",
        description="A tool that allows you to create responsive tools in text",
	long_description=long_description, 
	long_description_content_type="text/markdown",  
	packages=setuptools.find_packages(), 

        install_requires=[ 
            "termcolor", 
            "colorama", "readchar","cursor"
        ], 
  
	license="MIT", 

	# classifiers like program is suitable for python3, just leave as it is. 
	classifiers=[ 
		"Programming Language :: Python :: 3", 
		"License :: OSI Approved :: MIT License", 
		"Operating System :: OS Independent",
                "Development Status :: 5 - Production/Stable"
	], 
) 
