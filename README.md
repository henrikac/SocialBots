# SocialBots

A collection of social media bots (only Instagram bot at the moment).

## Requirements:

+ Python 3.6+
+ Selenium

If you need help setting up selenium on your computer just follow this [simple guide](https://selenium-python.readthedocs.io/installation.html)

## Usage:

You need to create the database before running the app for the first time. To create the database simply navigate to the `src` folder and type the following commands in the Python interpreter:

```
> import models
> models.create_tables()
> exit()
```

Now you should be ready to run the app `python3 app.py` :-)
