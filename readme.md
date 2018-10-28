# Comment Analyser

Simple API to to analyse comments with [Watson](https://www.ibm.com/watson/) [Tone Analyzer](https://console.bluemix.net/catalog/services/tone-analyzer) to determine whether positive or negative tone.

Built with Python3, Flask and [Watson Tone Analyzer API](https://watson-api-explorer.ng.bluemix.net/apis/tone-analyzer-v3).

## Requirements

-   Python 3.6
-   [Watson API key](https://watson-api-explorer.ng.bluemix.net/apis/tone-analyzer-v3)
-   Pytest

## Installation

### Clone Project

```sh
git clone https://github.com/taiyeoguns/comment-analyser.git
```

### Install Requirements

With a [virtualenv](https://virtualenv.pypa.io/) already set-up, install the requirements with pip:

```sh
pip install -r requirements.txt
```

### Add details in `.env` file

Create `.env` file from example file and maintain necessary details in it e.g. Watson API Username and Password

```sh
cp .env.example .env
```

### Start the server

Start the Flask web server by running:

```sh
python run.py
```

Server should usually be started at `http://localhost:5000`

### Tests

To run tests, in the command line run:

```sh
pytest
```

### Documentation

To view documentation, open the browser and navigate to `http://localhost:5000/api/ui`
