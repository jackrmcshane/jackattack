# Package Building for PyPi
*This notes section will follow my learning of the process for creating a library and having it hosted on the Python Package Index platform as well as document the sources I have used to that end.*
<br><br>

**Step 1:** Have a codebase that provides a useful function.
<br><br>
**Step 2:** Create a directory hierarchy that looks as similar to that below.

```
setup.py
/src/
  |-- codebase.py
```

<br>

**Step 3:** A rudimentary setup.py file will look like this. (_**Note:** if you have pip installed, you already have setuptools as they ship together._)

```python
from setuptools import setup

setup(
    name='codebase', """ This is what you 'pip install' """
    version='0.0.1',
    description='Purpose of codebase',
    py_modules=["codebase"], """ This is the name you use in import statement """
    package_dir={'': 'src'}, """ Gives package location. First string is path to package dir; second string is name of package dir. """
)
```

<br>

**Step 4:** From here, we build the package in our terminal!

First make sure you have the `wheel` package installed by running:

```
pip install wheel
```
or
```
pip3 install wheel
```

Now build the package:

```python
python setup.py bdist_wheel
```

The output in the terminal will be rather lengthy, but somewhere amongst the first third of the output, you should see a line similar to the following:

```
'copying src/codebase.py -> build/lib'
```

* _**Note 1:** If you do not see a version of this line, your wheel file is empty and the rest of the work you do from here will be moot. You must attempt to rebuild the package if this occurs._
* _**Note 2:** A wheel file contains a compressed version of your package and is what pip uses for distribution through the PyPi platform._
* _**Note 3:** The `bdist` portion of the command creates a *binary* version of the distribution. Later, we will also see that we can distribute the package as source code._

<br>

Following the build process, your working directory should look similar to the following:

```
/build/
   |-- /bdist.os_type-version-architecture/
   |-- /lib/
         |-- codebase.py
/dist/
   |-- codebase-0.0.1-python_version-none-any.whl
setup.py
/src/
   |-- /codebase.egg-info/
         |-- dependency_links.txt
         |-- PKG-INFO
         |-- SOURCES.txt
         |-- top_level.txt
   |-- codebase.py
```
<br>

**Step 5:** Testing our initial package distribution by installing it locally.
<br><br>
With a typical 'pip install <package_name>' call, the installed package is placed in your /site-packages/ folder amongst the rest of your installed python distribution. If we were to use something like that in this instance, we would end up with two versions of our code. The one that we are editing and the one that will be linked by our import statements. This will cause issues down the line.
<br><br>
*Solution:* Using the `-e` flag. The command `pip install -e .` links the newly built python library in our current working directory to our python distribution such that only one copy of our library is referenced and any changes made are immediately available for testing.

_**Note:** See the man-pages for pip-install for further documentation on the `-e` flag._

Run `pip install -e .` from your working directory.


<br>

**Step 6:** Testing

You should now be able to import your newly created library into your code anywhere on your system. Let's test that out.

In another directory, create a file named `main.py` that uses code from this repository:
```python
from jackattack import JackAttack

jack = JackAttack()
jack.attack()
```

After running `python main.py` in your terminal, you should get the following output:
```
Jack attacks you.
Jack attacks you.
Jack attacks you.
You die.
```

At this point, we could upload the code to PyPi.

<br>

**Step 7:** Obtaining a liscense for your module

Others cannot copy, modify, nor use your code library unless you have an appropriate liscense attached to it. A website that will help you determine the liscense that is best for your purposes and intentions is: [choosealicense.com](https://www.choosealicense.com)

This repository has been released under the [MIT Liscense](https://choosealicense.com/licenses/mit/).

<br>

**Step 8:** Classifiers - the tags under which your package can be searched on PyPi

Classifiers are the tags that can be used to search and/or find your package on the PyPi platform. A list of valid classifiers can be found at [pypi.org/classifiers](https://pypi.org/classifiers)

You can add these classifiers to your `setup.py` file in this fashion:
```python
from setuptools import setup

setup(
        ...
        classifiers=[ # tags used to search the library on PyPi
            "Development Status :: 3 - Alpha",
            "License :: OSI Approved :: MIT License",
            "Natural Language :: English",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3"
        ],
)
```

_**Note:** Re-run `pip install -e .` every time you modify your `setup.py` file from here on out! This ensures that the package still installs properly. Re-run it!_

<br>

**Step 9:** Using README.md as PyPi project description

Because our `setup.py` file is, in fact, a python file, we can add code as below.

```python
with open("README.md", "r") as f:
    long_description = f.read()
    
setup(
        ...
        long_description=long_description,
        long_description_content_type="text/markdown",
)
```

Using the python context manager, we read in the README.md file associated with the project, and set that as the PyPi project description using our `setup.py` file.

_**Note:** Re-run `pip install -e .`!_

<br>

**Step 10:** Adding dependencies to setup.py

You should add a list of your libraries dependencies to your setup.py file and this can be done in this oh so familiar fashion:

```python
setup(
    ...
    install_requires = [
        "numpy ~= 1.23.5",
    ],
)
```

The `install_requires` parameter in our `setup.py` file is a replacment for the often used `requirements.txt` file that is part of many projects.

_**Note:** Re-run `pip install -e .` This should now pull down the dependencies listed._

<br>

**Step 11:** Adding Development dependencies

Development dependencies can be added in a similar way to the installment requirements above:
```python
setup(
    ...
    extras_require = {
        "dev":[
            "pytest>=3.7",
        ],
    },
)
```

Installation of these dependencies (for the purposes of further testing and development of the project) can be done by inputing the following command at your terminal prompt:

```bash
pip install -e .[dev]
```

_**Note:** These instructions can also be found in the README.md_


<br>

**Step 13:** Building the Source Distribution

In your terminal, run:
```bash
python setup.py sdist
```

This command generates a tar file of the souce code for the library that can be distributed through the PyPi platform. This can be useful for many reasons, least of which is allowing users of the platform to verify the code they will be running themselves.

If you have followed this walkthrough to this point, you will likely see the following warnings after running the `python setup.py sdist` command:
```
running sdist
...
warning: check: missing required meta-data:
warning: check: missing meta-data: either (author and author_email) or (maintainer and maintainer_email) must be supplied
...
```
You can fix this by adding the information to the `setup.py` file as shown below:
```python
...
url = "https://github.com/username/repository_name",
author = "Author Name",
author_email = "your.email@address.com",
```

Run `python setup.py sdist` once again. This time you should see no errors.

Assuming no errors, you can now run `tar tzf dist/package_name-version_number.tar.gz` from your command line to view a list of the files that will be included in the source distribution for your package.

_**Note:** Notice that from among the files, our LICENSE file and any test files that you have are not apart of the source distribution! We want these files to be included because they are already a part of the binary distribution._

**Step 14:** Using a Manifest file to fix the sdist problem

Run the following commands in your terminal:
```bash
pip install check-manifest
check-manifest --create
git add MANIFEST.in
```
You can now re-run: `python setup.py sdist` to rebuild your source distribution. When you rerun `tar tzf dist/package_name-version_number.tar.gz`, you should now see your LICENSE file and any testing files as part of the source distribution.

<br>

**Step 15:** FINALLY, Finally, finally...

You now have a complete package to publish to PyPi! But, before you do, make sure you dot your i's and cross your t's:

1. Rebuild your distributions with `python setup.py bdist_wheel sdist`.  
2. Test installation with `pip install -e .`
3. Run `ls dist/`. You should see both a wheel file and a tar file, corresponding to your binary and source distributions repectively.
4. Verify the appropriate files are a part of your source distribution with `tar tzf dist/package_name-version_number.tar.gz`.

Install the python `twine` package to assist the  uploading:
```
pip install twine
```

Finally, upload your distribution to PyPi.
```
twine upload dist/*
```
Done!


<br>

#### Sources
---
* [Publishing (Perfect) Python Packages on PyPi](https://www.youtube.com/watch?v=GIF3LaRqgXo) - YouTube
* [What Are Python Wheels and Why Should You Care?](https://realpython.com/python-wheels/)
* [choosealicense.com](https://www.choosealicense.com)
* [pypi.org/classifiers](https://pypi.org/classifiers)

