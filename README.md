# Data Dialogics with Dash

## About
This library provides a **basic [Dash](https://dash.plotly.com "Dash Documentation and User Guide") app structure** which allows data analysts and data scientists to do what they do best: load, manipulate, combine, visualize and analyze data. With this app structure data experts will spend less time on app development and more time on data analytics and the data dialogue with domain experts and decision makers. 
 
The goal of Dash Data Dialogics is to **facilitate the analytical process to get from noisy uncertainty to clear insights**. The essence of this analytical process is not the data, the algorithms or the visualization tools. It is the human thought flow of the domain experts and decision makers. This means domain experts and decision makers are not just consumers of the results, they should be involved at the center of the analytical process. 
 
With Dash Data Dialogics a data scientist or data analyst (who is not afraid of code) can facilitate the exchange of thoughts by adding an extra layer to the dialogue: the data visualizations. Just like the human thought flow, the data visualizations must continuously evolve and adapt to enrich the conversation. 

Python, with its rich ecosystem of data analytics libraries, offers almost endless possibilities to handle and analyze data. [Dash (by Plotly)](https://dash.plotly.com "Dash Documentation and User Guide") allows to put complex Python analytics in the hands of business users. The Dash Data Dialogics framework adds more **flexibility and speed to adapt data visualizations to the rhythm of the dialogue.** 

## Application installation and usage

### Prerequisites

* git (on windows [git-scm](https://git-scm.com/))
* python3.8 and above

### Installation

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

### Run the application

```shell
(.venv) $ python index.py
```

### Usage instruction

For a detailed instruction on how to use this template, please see the [docs folder](./docs/0_index.md)

## Copyright and license

## Background

### History
Dash Data Dialogics started as a proof of concept at the City of Ghent and was adopted as a working group challenge in the SCORE project. 

### SCORE (Smart Cities + Open Data Re-use)
SCORE is a project that aims to increase efficiency and quality of public services in cities through smart and open data-driven solutions. 
	
SCORE is a European Union funded project with nine cities and three universities participating: Amsterdam, Aarhus, Aberdeen, Bergen, Bradford, Dordrecht, Ghent, Gothenburg, Hamburg, University of Amsterdam, Aarhus University and University of Bradford.
	
The partners develop innovative solutions based on open data and focus on sharing insights and methodologies for developing better public services. For instance in the shape of better management of sustainable mobility, improving air quality, monitoring flooding and furthering crowd management.

