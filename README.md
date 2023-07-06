# sumo-wrestler
Sumo Wrestler quickly gets your reading opponents out of the ring.


### Pre-requisites
 - A Local PDF to summarize
 - Install the dependencies & run pipenv shell [Getting Started](#getting-started)
 - OpenAI API key in a .env file
 - 
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

## Running the app

Call the app from the pipenv shell `pipenv shell`.
```
python summarize.py -f [path to file, i.e. /results/summarize/2210.03629.pdf/2210.03629.pdf]
```

## Config

 This project uses a .env file. (Pipenv will automatically run .env on startup of the shell). 

 There is a .env.sample which should have all environment variables and sample values, copy this into a file called `.env` at the root of the project. This filename is in the .gitignore. Standard WARNING about sharing your api key.
 
### Config Map
OPENAI_API_KEY (str) - the api key you use to connect to OpenAI