# Webserver with Flask

A webserver is a program that handles HTTP requests and applies some logic if neccessary. I.e. a webserver could check if a user is athenticated to access a specific site. The webserver also populates a website with some data that is specific to a user. All this logic is usually done on the server with some templates. After pupulating the templates with the data, they are sent to the user in form of an HTML-document, which gets rendered by the browser.

A webserver can also just serve some data as JSON or XML. This data gets accessed via a URL that has a specific format. This is called a **REST-API**. This **REST-API** is usually the access for a user to some data that is stored in a database. This is an easy way to make your data accessible to other users and programms. It works the exact same way as opening a website. The user sends a request to a webserver, but instead of a HTML-document the user recieves a JSON-String. But before we implemnt a **REST-API**, we focus on serving a simple HTML page.

## Creating your own Webserver

To create and *publish* your own webserver, your can just use this repository and following the setup guide we describe here.

### Step 1: Fork the Repository

To work with this repository, you have to fork it and put it in your own account. You can find the fork button in the top right. Click it and the follow the steps until you have it in your own account.

### Step 2: Open in Gitpod

To work on the repository, you have to open it in **Gitpod**. To to this, just paste `https://gitpod.io#` in front of the url of your repository. Your repo should now open in Gitpod and you can start working on it.