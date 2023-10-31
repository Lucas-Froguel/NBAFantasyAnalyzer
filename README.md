# NBA Fantasy Analyzer

This system was designed to analyze and predict NBA fantasy scores. 

# Architecture

This system ingest, process and displays data. We ingest data from the NBA API and from the ESPN Fantasy API. 
This data is stored in a data lake, built in mongodb. This data is later processed and stored in a mini data-warehouse,
that is also hosted on the same mongodb (there is no need for nothing more, given the scale of this application for now). 

We ingest daily and historical data of NBA players from the teams of your Fantasy League and analyze them. Given the ESPN data
we are able to make broad estimates of matchup results, given the estimated (average) and projected (given by espn) scores. 

We also use the historical data to train and evaluate ML models to estimate individual player performance and, thus, 
of each roster. This enables more precise estimations and the core idea is to beat the ESPN projections in terms of 
accuracy. 

The data is shown to the user via a Telegram Bot. Later maybe a web panel.

There are recurrent jobs to ingest and process data, orchestrated by APScheduler, a python framework designed for this. 
Again, this is possible because of the current scale of the app. 

## Alternative Architecture

An alternative is to setup an airflow instance that triggers jobs in the cloud, through serverless functions. In this 
context, one should also host the database in the cloud as well and separate the data lake from the data warehouse. 

# How to run

In order to run the application, you only need three commands. First,
```bash
cp .env.template .env
```
However, this still requires you to manually insert the values for the keys, which will lead to some odd behavior if not
set appropriately. In light of this, together with the link to this application, the actual `.env` used by me will
also be sent. In this case, you can skip the above command. Then
```bash
make build
```
And also
```bash
make run
```

This will build and run the container, which will start to run its processes and send you regular messages in Telegram.

# How to test

Just run 
```bash
make test
```
after having build the application.


