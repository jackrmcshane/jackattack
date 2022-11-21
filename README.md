# Jack Attack

<br>

A repository for the purposes of learning to create python libraries and implements the JackAttack class.
<br>
Methods for instantiation:
* Install through the Python Package Index
*  Cloning this repository directly


#### PyPi Installation
---
From your command line, run:
<br>
`pip install jackattack`

#### Cloning the Repo
---
In your working directory, use your command line to run:
<br>
`git clone https://github.com/jackrmcshane/jackattack.git`

#### Usage
---
```python
from jackattack import JackAttack

jack = JackAttack()
jack.attack()
...
jack.run()
```

#### Output
---
```
Jack attacks you.
Jack attacks you.
Jack attacks you.
You die.
...
You scare Jack.
He runs away.
```



<br> <br> <br>



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

**Step 3:** A rudimentary setup.py file will look like this. (**Note:** if you have pip installed, you already have setuptools as they ship together.)

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

* **Note 1:** If you do not see a version of this line, your wheel file is empty and the rest of the work you do from here will be moot. You must attempt to rebuild the package if this occurs
* **Note 2:** A wheel file contains a compressed version of your package and is what pip uses for distribution through the PyPi platform.

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

#### Sources
---
* The [Publishing (Perfect) Python Packages on PyPi](https://www.youtube.com/watch?v=GIF3LaRqgXo) video on YouTube
* [choosealicense.com](https://www.choosealicense.com)
