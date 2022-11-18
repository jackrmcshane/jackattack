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
```
from jackattack import JackAttack

jack = JackAttack()
jack.attack()
```

<br> <br> <br>

## Notes on creating a Python library for PyPi
*This notes section will follow my learning of the process for creating a library and having it hosted on the Python Package Index platform as well as document the sources I have used to that end.*
<br><br>

**Step 1:** Have a codebase that provides a useful function.
<br>
**Step 2:** Create a directory hierarchy that looks as similar to that below

```
src
 |-- codebase.py
```


<br>

#### Sources
---
* The '[Publishing (Perfect) Python Packages on PyPi](https://www.youtube.com/watch?v=GIF3LaRqgXo)' video on YouTube
