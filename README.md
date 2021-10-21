# Dash SCORE template

## Introduction

## Prerequisites

* git (on windows [git-scm](https://git-scm.com/))
* python3.8 and above

## Installation

* Get the template on your computer

```shell
$ git clone https://github.com/lab9k/dash-score-project-template.git mydashboard
$ cd mydashboard/
```

* We'll create a virtual environment to not pollute your python installation

```shell
$ python -m venv ./venv
$ source ./.venv/bin/activate
```

This assumes a bash shell is used, for instructions for other
platforms [go here](https://docs.python.org/3/library/venv.html).

* install the application dependencies

```shell
(.venv) $ pip install -r requirements.txt
```

Now everything is set to run the application.

## Run the application

```shell
(.venv) $ python index.py
```

## Usage instruction

For a detailed instruction on how to use this template, please see the [docs folder](./docs/0_index.md)
