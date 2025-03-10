# Welcome on Sport Insight

## Table of contents
<p align="center">
    <a href="#installation">Installation</a>
</p>

## Introduction

## Installation

Install Python 3.7 or higher : [Python](https://www.python.org/downloads/)

Install Git : [Git](https://git-scm.com/downloads)

Clone ``git clone https://github.com/SportInsightHub/SportInsight.git``

Go to the project directory : ``$ cd SportInsight``

If you not find package python3.11: ``sudo add-apt-repository ppa:deadsnakes/ppa`` Then ``sudo apt update``

Install python3.11 and other dependencies: ``apt install -y python3.11-venv python3.11-dev libpq-dev gcc``

Install Virtualenv : ``$ pip install virtualenv``

Create a virtual environment : ``$ virtualenv -p python3.11 .venv ``

On Linux you need to install python3.11 before create the virtual env

Activate the virtual environment (on windows): ``$ .\.venv\Scripts\activate``
Activate the virtual environment (on linux or macOS): ``$ source .venv/bin/activate``

Install Dependencies : ``$ (.venv) > pip install -r requirements.txt``

Start Application : ``$ (.venv) > py main.py``

## Usage

#### Swagger Docs:

/auth/login

/auth/refresh?refreshToken=&

/auth/new?username=

/art/post?&id_art=&img=buffer&content=

/art/delete?id_art=

/art/edit?&id_art=&(replace)

## Contributing

## License
