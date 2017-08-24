# Flask API seed project

Scaffold for a Flask based REST API

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Install Python 2 and pip. Following this, install virtualenv for setting up
your Python virtual environment.

```
pip install virtualenv
```
If on Windows, also install the virtualenv wrapper for Windows

```
pip install virtualenvwrapper-win
```
Create a virtual environmen
```
mkvirtualenv flask-seed-venv
```
By default the virtual environment willl be activated after succesfull installation.

### Installing

Navigate to the project folder and install the Python package dependencies

```
pip install -r requirements.txt
```

Run the recreate_db.py script to create a test sqlite database.


## Running the app

```
python run.py
```

## Built With

* [Flask](http://flask.pocoo.org/) - The web framework used
