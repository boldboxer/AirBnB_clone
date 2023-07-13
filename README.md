# AirBnB clone - The console

This is the solution to the AirBnB clone - The console project for ALX high level programming language [ALX SWE](https://alxafrica.com). A team project to improve collaborations and problem solving skills amongst ALX students.

## Table of contents

- [Overview](#overview)
  - [The requirements](#the-requirements)
    - [Python Scripts](#python-script)
    - [Python Unit Tests](#python-unit-test)
  - [The challenge](#the-challenge) 
    -[First step](#first-step) 
    -[Command interpreter](#command-interpreter)
  - [Files and descriptions](#files-and-descriptions)
  - [Description of the command interpreter](#description-of-the-command-interpreter)
    - [How to start it](#how-to-start-it)
    - [How to use it](#how-to-use-it)
    - [Examples] (#examples)
  - [Execution](#execution)
  - [Our process](#our-process)
  - [Built with](#built-with)
  - [What we learned](#what-we-learned)
  - [Continued development](#continued-development)
  - [Useful resources](#useful-resources)
- [Authors](#authors)
- [Acknowledgments](#acknowledgments)

## Overview

### The requirements

#### Python Scripts

The general requirements for the project tasks were:

- Editors used: `vi`, `emacs`
- All files were interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All files ended with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project was created
- The code used the pycodestyle (version `2.8.*`)
- All files are executable
- The length of the files were tested using `wc`
- All modules had a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All classes had a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All functions (inside and outside a class) had a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A README with the description of the project was written
- An 'AUTHORS' file at the root of the project repository, listing all individuals having contributed content to the repository was created.

#### Python Unit Tests

- Editors used were: `vi`, `emacs`
- All files ended with a new line
- All test files were inside a folder `tests`
- The unittest module was used
- All test files were python files (extension: `.py`)
- All test files and folders started with `test_`
- All tests were executed by using this command: `python3 -m unittest discover tests`
- All modules had a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All classes had a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All functions (inside and outside a class) had a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)

### The challenge

#### First step

The first step of the project involved writing a command interpreter to manage the **AirBnB** objects. Each task was linked and helped achieved the following:

- A parent class was put in place (called `BaseModel`) that took care of the initialization, serialization and deserialization of future instances.
- A simple flow of serialization/deserialization was created: Instance <-> Dictionary <-> JSON string <-> file
- All classes used for AirBnB were created (`User`, `State`, `City`, `Place`, `Amenity`, `Review`) that inherited from `BaseModel`
- The first abstracted storage engine of the project was created: File storage.
- All unittests to validate all classes and storage engine were created.

#### Command interpreter
- A new object was created (ex: a new User and a new Place)
- An object was retrieved from a file, a database
- Operations on objects (count, compute, stats) were done
- Attributes of an object were updated
- An object was destroyed

### Files and descriptions

The files used to making the Airbnb project and their descriptions are thus:

| files           | Description                                                                               |
| --------------- | ----------------------------------------------------------------------------------------- |
| README.md       | Contains description of the project and the command interpreter                           |
| AUTHORS         | Listing all individuals having contributed content to the repository                      |
| base_model.py   | A file containing a class that defines all common attributes/methods for other classes    |
| file_storage.py | A class that serializes instances to a JSON file and deserializes JSON file to instances: |
| console.py      | A program that contains the entry point of the command interpreter                        |
| user.py         | A User class that inherits from BaseModel                                                      |
| state.py        | A State class that inherits from BaseModel                                                      |
| city.py         | A City class that inherits from BaseModel                                                      |
| amenity.py      | An Amenity class that inherits from BaseModel                                                      |
| place.py        | A Place class that inherits from BaseModel                                                      |
| review.py       | A Review class that inherits from BaseModel                                                      |

### Description of the command interpreter

#### How to start it
* Run the command `./console.py` in the command interpreter.

```
peter@eben:~/AirBnB$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
```

#### How to use it

```
peter@eben:~/AirBnB$ ./console.py
(hbnb) <args1> <args2> ... <options>
```

#### Examples

```
peter@eben:~/AirBnB$ ./console.py

(hbnb) all MyModel
** class doesn't exist **

(hbnb) show BaseModel
** instance id missing **

(hbnb) show BaseModel My_First_Model
** no instance found **

* Creating a new instance of the `BaseModel`
(hbnb) create BaseModel 49faff9a-6318-451f-87b6-910505c55907

* Displaying the attributes of all the available `BaseModels`
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]

* Display a specific `BaseModel` by adding an option of `id`
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}


(hbnb) destroy
** class name missing **

* Destroying a specific `BaseModel` by passing `id` as option
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907

(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
(hbnb)
```

### Execution

The shell worked like this in interactive mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

But also in non-interactive mode:

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

All tests also passed in non-interactive mode: `$ echo "python3 -m unittest discover tests" | bash`

## Our process

### Built with

The AirBnB clone - The console project, was built with `python` language. Testing of components was done using `unittest module`

### What we learned

....... What we learned will go right here ......

### Continued development

...... What we will like to improve on or work on based on this project .......

### Useful resources

[Code Blocks](https://docs.readme.com/rdmd) - The `rdmd` docs from this site helped us to write a well structured readme for this project, alongside proper formatting of inline codes and code blocks

[Stack Overflow](https://stackoverflow.com/) - This aided us to help find questions and appropraite answers to bugs we faced while doing the project.

[GitHub Docs](https://docs.github.com/en/get-started/) - GitHub Docs was used to create nicely formatted tables, markdown guidelines and proper usage of other tools.

[Geeks For Geeks](https://geeksforgeeks.org) - Geeks for geeks, a great place for well detailed technical articles encompassing several programming languages, this helped in getting several informations on how some of the functions works.

[Youtube Channels](https://youtube.com) - Combinations of several channels and videos was used to aid the completion of this project, I will suggest that anyone wanting to top their developing game, should use Youtube more often.

[Real Python](https://realpython.com) - Tonnes of articles as regarding general knowledge of python, integration and unit testing of python files and components, tutorials and many more other aids, were gotten from the real python official website.

[Google](https://google.com) - Google was the icing on the cake, as almost everything, started and ended with Google, a timely and accurate search can salvage one hours of debugging problems.

## Authors

This project was done by:

- Ebenezer Mose
- Peter Odo

## Acknowledgments

We are both super grateful for the opportunity ALX is offering to young Africans as regardsgrowing the technological atmosphere of the continent, we sure, will keep this flag flyinghigh, ALX to the world.
...... we can further add to this also ......