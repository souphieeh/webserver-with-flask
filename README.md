# Webserver with Flask

A webserver is a program that handles HTTP requests and applies some logic if neccessary. I.e. a webserver could check if a user is athenticated to access a specific site. The webserver also populates a website with some data that is specific to a user. All this logic is usually done on the server with some templates. After pupulating the templates with the data, they are sent to the user in form of an HTML-document, which gets rendered by the browser.

A webserver can also just serve some data as JSON or XML. This data gets accessed via a URL that has a specific format. This is called a **REST-API**. This **REST-API** is usually the access for a user to some data that is stored in a database. This is an easy way to make your data accessible to other users and programms. It works the exact same way as opening a website. The user sends a request to a webserver, but instead of a HTML-document the user recieves a JSON-String. But before we implemnt a **REST-API**, we focus on serving a simple HTML page.

## Creating your own Webserver

To create and *publish* your own webserver, your can just use this repository and following the setup guide we describe here.

### Step 1: Fork the Repository

To work with this repository, you have to fork it and put it in your own account. You can find the fork button in the top right. Click it and the follow the steps until you have it in your own account.

### Step 2: Open in Gitpod

To work on the repository, you have to open it in **Gitpod**. To to this, just paste `https://gitpod.io#` in front of the url of your repository. Your repo should now open in Gitpod and you can start working on it.

### Step 3: Check if everything is Setup correctly

When you opened the repository with **gitpod** you should inspect the different files that are there. The most important one it the `run.py` file. Open this file and read through it very quickly. This file has a lot of unknown syntax and new functions that you don't know yet. Just try to make sense of the ones your already know. Some should look familiar from the templating with **Jinja2**.

This is exactly what we do here. We just load a template and give it some data to render it. We then return the HTML that is produced to the user that is calling this route.

## Routes in Flask

In **Flask** and other webservers, a route is the part of the URL that follows the first `/` after the domain name. Here we have `@app.route("/")`, which means that we want to access the root of this webserver. Usually we serve the index page from this route.

> **Note:**
>
> `@app.route()` is a so called decorater. We need these decorators in **Flask** to tell it that we implement the logic for this route inside of the function just below it. The name of the function does not have to match the route name, but it helps to make things more readable.

### Step 4: Run the Webserver

If everything is setup correctly, you should be able to run the webserver directly from the script. Open the file `run.py` and you should see a play button in the top right of the editor window. Click this button to start your webserver. **Gitpod** should ask you to open the website as preview or with the browser. You should choose browser and then put the browser tabs next to each other.

Congratulations! You just *published* your own webserver!

### Step 5: Stop the Server

To further develop the webserver, you first have to stop it. Just navigate to the terminal that should have opened at the bottom of your screen, and hit `Ctrl+C`. This should stop the server and you can make some changes to it.

### Step 6: Create a new Branch

Whenever you develop something new, you should always start a new branch in your repository. In the bottom left you can find a button with `master` written on it. Click it and a popup dialog opens. Select `create new branch` from this menu and name your new branch. You can also press `Ctrl+Shift+P` to open up the command palette and search for `Create Branch` and hit `Enter`.

Now you have a new branch to work in, which means you can also just try out stuff. If it does not work, you can always discard your changes with `git reset --hard master`.