![dact logo](https://raw.githubusercontent.com/ayushmankumar7/dact/main/extras/dact.png)

# dact

dact is a CLI Package in Python focusing towards decreasing development setup time while working with React + Django Full Stack Development. 
dact setup the whole, ready to work, Django project with React in just a single line command. 
It handles all the urls, views, webpack, loaders, babel,etc. for the user in just a single command. Using dact, a developer can start writing their React code and see it render on their Django Web App. 


## Installing dact 

`pip install dact`

![dact_succesfull_installation](https://github.com/ayushmankumar7/dact/blob/main/extras/install.gif)


## Django + React

1. Start a Django Project with default Frontend app name 
`dact myproject`

2. Start Django Project with custom Frontend app name 
`dact myproject appname`


## Requirements 

1. You must have [npm](https://nodejs.org/en/) installed in your system. 
2. You must have [Python](https://www.python.org/) installed in your system. 
3. Python and pip or pip3 must be added to your environment.

## How to install this Package(for Development)

1. Clone this Repo 
2. `cd dact`
3. `pip3 install -e .`


On successfull setup of your project, you should see something like this:


![dact_succesfull_installation](https://github.com/ayushmankumar7/dact/blob/dev/extras/dact-opening.jpg)

## How to work with dact 

### To start the Server
`cd myproject` <br/>
`python manage.py runserver`

### To start working on the frontend 

1. Start watching the changes using 
`dact-watch`
Let `dact-watch` run in a different terminal. Make sure you run `dact-watch` in the same directory as `manage.py`.

2. Edit your React Front-end at :
`reactfrontend > static > src > App.js`

3. Make your changes and save your file. 

4. Refresh your page.



