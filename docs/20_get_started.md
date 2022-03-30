# Get started

Follow the steps below to set up your Dash Data Dialogics app.
1. [Fork the base template](#1_fork)
2. [Clone the personal repository to your workstation](#2_clone)
3. [Run the application](#3_run)
4. [Create a new page](#4_createpage)
5. [Read and prepare data](#5_preprocess)
6. [Add layout structure](#6_grid)
7. [Add data visualizations](#7_visualize)
8. [Add interactivity](#8_callbacks)
9. [Customize style](#9_style)

## Prerequisites

To be able to use this template, you should have python3.6 installed. You can download the latest release [here](https://www.python.org/downloads/release/python-368/)

## 1. Fork the base template<a id='1_fork'></a>

* Fork the [Dash Data Dialogics base template](https://github.com/lab9k/dash-score-project-template) to a
personal github repository: [fork a repo](https://docs.github.com/en/get-started/quickstart/fork-a-repo#forking-a-repository).
* Optionally, if you plan to create multiple visualization apps for different use cases, you can create a branch for each use case:
[create a branch](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-and-deleting-branches-within-your-repository).

## 2. Clone the personal repository to your workstation<a id='2_clone'></a>

[Cloning your repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo#cloning-your-forked-repository)

* Choose a directory on your local workstation to create a local repository clone. Make this your current working directory.

```shell
$ cd <path to your local directory>
```

* Clone the Dash Data Dialogics template to your computer

To clone only a specific use case branch:
```shell
$ git clone --branch <branchname> https://github.com/<your github repository>/dash-score-project-template.git <mydashboard>
$ cd <mydashboard>
```

To clone the complete repository, including all branches (if there are any):
```shell
$ git clone https://github.com/<your github repository>/dash-score-project-template.git <mydashboard>
$ cd <mydashboard>/
```

For information about keeping local and remote repositories in sync:
[Pushing changes (Github Desktop)](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/making-changes-in-a-branch/pushing-changes-to-github)
[Pushing changes (command prompt)](https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository)
[Syncing your local repo (Github Desktop)](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/keeping-your-local-repository-in-sync-with-github/syncing-your-branch)
[Syncing a fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork)

## 3. Run the application<a id='3_run'></a>

* Create a virtual environment to not pollute your python installation

```shell
$ python -m venv ./venv
$ source./.venv/bin/activate
```
This assumes a bash shell is used. For windows, use

```shell
$ .\venv\Scripts\activate
```
For instructions for other platforms [go here](https://docs.python.org/3/library/venv.html).

* Install the application dependencies.

```shell
(.venv) $ pip install -r requirements.txt
```

* Now everything is set to run the application.

```shell
(.venv) $ python index.py
```

The app is now running on a local host indicated on the command prompt. For example: http://127.0.0.1:8050/.
Open the host url in your browser to use the app.

## 4. Create a new page<a id='4_createpage'></a>

* Create a copy of `/empty_pagegroup` in the `/pages directory` and rename it (no spaces allowed in folder name).
This will automatically create a top level page group that will show up in the main navigation bar at the top of the screen.
* Rename the `empty_page` folder or create copies to add extra subpages.
The sub level pages will appear automatically in the side navigation bar on the left.

For more information on pages and dynamic routes, [go here](./32_routes.md).

## 5. Read and prepare data<a id='5_preprocess'></a>

* Load and prepare data for visualization by adding code to `/data/preprocess.py`.
If local files are used instead of database connections or APIs, the data files can be stored in the `/data/localdata` folder.

* Import the preprocessed data in the `layout.py` file for visualization in that page layout.

```
from data.preprocess.py import <datavariable>
```

## 6. Add layout structure<a id='6_grid'></a>

Now you have your data ready to be visualized, you can start bulding the Dash app page in the `layout.py` file.

* Import the grid components `Row()` and `Column()`.

* Generate a layout by nesting `Row()` and `Columns` to create a [grid structure]([Layout](./33_layout.md).

The grid components generate a [Bootstrap Grid](https://getbootstrap.com/docs/4.0/layout/grid/).

* Use the argument `extra_classes` in the `Row()` and `Column()` functions to adjust the layout with optional Bootstrap classes.

```
Column(content=html.P('Column using 8/12 of the available width'), extra_classes=[' col-8'])
```

Example `layout.py` structure:
```
from dash import html
from layout.structure.grid import Column, Row
from components.tiles import pagetitletile, infotile, subtitletile, plottile

layout = Column(children=[
    Row(content=pagetitletile('First column - First row: pagetitle')),
    Row(content=infotile('First column - Second row: page info')),
    Row(children=[
        Column(children=[
            Row(content=subtitletile('Level 1 column 1 - Level 2 row 3 - Level 3 column 1 - Level 4 row 1')),
            Row(content=plottile(tiletitle='Add some visual here')),
            ], extra_classes=[' col-5']),
        Column(children=[
            Row(content=subtitletile('Level 1 column 1 - Level 2 row 3 - Level 3 column 2 - Level 4 row 1')),
            Row(content=plottile(tiletitle='Add some visual in the second column')),
            Row(content=plottile(tiletitle='Add another visual in the second column')),
            ], extra_classes=[' col-7']),
        ])
]).get_layout()
```

## 7. Add data visualizations<a id='7_visualize'></a>

* Create charts and maps using [Plotly](https://plotly.com/python/) and [Dash](https://dash.gallery/Portal/) components.
* Use the functions from `components.tiles` to embed the visualisations in preformatted tiles.
* Add the tiles as content to the rows and columns.
```
Row(content=mytile())
```

See `pages\demo\demo_page\layout.py` for examples.

## 8. Add interactivity<a id='8_callbacks'></a>

To create user-interaction, Dash uses [callback functions](https://dash.plotly.com/basic-callbacks): functions that are
automatically called by Dash. Whenever an input component property of the callback function changes, the callback updates some property
in another component specified as the output.

* Add callback functions to `callbacks.py`

* If needed, use the function `add_memory_store()` from `storage.container` to generate
a [dcc.Store](https://dash.plotly.com/dash-core-components/store).
Store elements are used to share data between callbacks.

```
from storage import container as storage_container

storage_container.add_memory_store('test_input_store')
```

See `/pages/demo/demo_page/callbacks.py` for examples.
For more info on sharing data between callbacks, [go here](https://dash.plotly.com/sharing-data-between-callbacks).


## 9. Customize style<a id='9_style'></a>

Dash Data Dialogics uses [Bootstrap](https://getbootstrap.com/) for responsive layout styling.
With bootstrap you can easily customize your app style by adding Bootstrap classes to html elements.

Dash Data Dialogics comes with a customized [Bootstrap theme](https://getbootstrap.com/docs/4.0/getting-started/theming/).
If you want to change the theme, follow the instructions below.

* Override the default Bootstrap theme in `/styles/custom/custom.scss`. Check [Bootstrap Theming](https://getbootstrap.com/docs/4.0/getting-started/theming/) for more info.

The customized .scss in `/styles` must be converted to .css in `/assets` using Sass (https://sass-lang.com/guide).
* Install Sass (https://sass-lang.com/install)

For Windows:
* Download sass package for your operating system [here](https://github.com/sass/dart-sass/releases/tag/1.49.9).
* Unpack it on your computer (f.ex. `C:\Program Files\Sass\dart-sass`) and add the directory to the [PATH variable](https://katiek2.github.io/path-doc/).
* Compile the .scss files to .css files before running your application.

```shell
(.venv) $ sass styles/main.scss assets/style.css
```












