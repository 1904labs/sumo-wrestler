# sumo-wrestler
Sumo Wrestler quickly gets your reading opponents out of the ring.

## Getting Started

This project uses [Pipenv](https://pypi.org/project/pipenv/) for package and virtual environment management. 

From the root of this project

Install dependencies
```
pipenv install
```

Activate virtual environment (and apply environment variables from .env file)
```
pipenv shell
```

Deactivating virtual environment
```
exit
```
(`deactivate` will mess up pipenv)



## Config Map
OPENAI_API_KEY (str) - the api key you use to connect to OpenAI

## Running the app
### Pre-requisites
 - A Local PDF to summarize
 - Install the dependencies & run pipenv shell [Getting Started](#getting-started)

### Example Call

Run the script, passing in the path to the pdf
```
python summarize.py -f [filepath]
```
