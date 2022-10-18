# OpenWeather Exercise

This git repository has everything you need to start working on your OpenWeather
tasks.  Before beginning the tasks, please check to verify that you have everything
you need to run this code.

### Requirements

To do the exercises, you will need the following three items:
 * Python 3
 * The Python Requests library
 * An OpenWeather API key

**Python 3 and Python Requests**
You will need Python 3 installed and the Python requests library.  If you're on
a normal Linux distribution, it's highly recommended that you install
python3-requests from your distribution repositories.

If you're not running Linux or python3-requests is not available, first install
Python 3, and then you can install requests using `pip install requests` or
`pip3 install requests`.

**OpenWeather API key**
You will be provided with an OpenWeather API key.  The scripts will use the
`OPENWEATHER_API_KEY` environmental variable to access the key, so either export
it or set it to when running the commands.

Test your setup by running (replacing `<key>` with the actual OpenWeather API
key):
```
$ OPENWEATHER_API_KEY=<key> python3 test.py
Skibbereen: Clouds - overcast clouds
```
You should see the above output

### File structure

This repository has two files, `openweather.py`, which is a simple python library
for accessing the OpenWeather API and `test.py`, which is a basic test using the
openweather library to check the current weather in Skibbereen.

### The exercise

Before starting your tasks, please checkout a new branch in git by running
`git checkout -b exercise`.

Now you can complete the tasks that were assigned to you.  When they are complete,
commit the changes to your branch.

Then run:
```
$ git format-patch main
```

This will create a file, starting with `0001-`.  Please reply-all to your
original email, attaching this file.
