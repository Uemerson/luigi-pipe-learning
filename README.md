# About
Learning how to create a pipeline using Luigi

# How to run

First of all, you need to install [Python](https://www.python.org/), and after that, you can use [pip](https://pypi.org/) to install all dependencies contained in the `requirements.txt`.

Run the `hello world` pipeline on the local system:

```
PYTHONPATH='.' luigi --local-scheduler HelloWorld --module hello_world
```

Run the `count letters` pipeline on the local system:

```
PYTHONPATH='.' luigi --local-scheduler CountLetters --module count_letters
```
