# NBA Fantasy Analyzer

This system was designed to analyze and predict NBA fantasy scores.

# How it was designed



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

This will build and run the container, which will be accessed via the api in the localhost at port 8000. 

# How to test

Just run 
```bash
make test
```
after having build the application. Test coverage as of now is 95%. 


