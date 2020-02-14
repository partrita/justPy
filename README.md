# Learn justPy

[justPy official website](https://justpy.io/)

## Introduction

JustPy is an object-oriented, component based, high-level Python Web Framework that requires no front-end programming. With a few lines of only Python code, you can create interactive websites without any JavaScript programming. 

> The best way to understand JustPy is to follow the tutorial in which there are many examples

## Hello world!

```python
import justpy as jp

def hello_world():
    wp = jp.WebPage()
        d = jp.Div(text='Hello world!')
	    wp.add(d)
	        return wp

		jp.justpy(hello_world)
```

## Under the Hood

JustPy's backend is built using:

- starlette - "a lightweight ASGI framework/toolkit, which is ideal for building high performance asyncio services".
- uvicorn - "a lightning-fast ASGI server, built on uvloop and httptools".

JustPy's frontend (which is transparent to JustPy developers) is built using:

- Vue.js - "The Progressive JavaScript Framework"

The way JustPy removes the frontend/backend distinction is by intercepting the relevant events on the frontend and sending them to the backend to be processed.

## Installation

first, make sure that the version of python3 you have is 3.6 or higher: 

```bash
$ python --version
```

Create a virtual environment and pip install.

```bash
$ python -m venv venv
$ source venv/bin/activate
(venv) $ pip install justpy
```

## Running the program

Create a file in the directory called `test.py` that includes the code.

``bash
$ python test.py
```
