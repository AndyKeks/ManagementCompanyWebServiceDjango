<h1 align="center"> 
  ManagementCompanyWebServiceDjango
</h1>

# What is it?
The application is designed to facilitate the interaction of the management company with consumers via chat. 

# How to start ?
First, we need to upload the project to our local machine. To do this, in the command console, enter: 
```sh
https://github.com/AndrewErmakov/ManagementCompanyWebServiceDjango.git
```

Also you will have a `.env` file. This file must be in the same directory together `Dockerfile` and `manage.py`. You need to specify a nickname, mail and password for the administrator (ADMIN_LOGIN, ADMIN_EMAIL and ADMIN_PASS in `.env` file respectively).

**Alas, while it is still difficult to launch a project in docker, as there is an error, I will solve it in the near future! So for now, let's run the project using a virtual environment.**

Let's assume that python3 is installed on your local computer.

In the `ManagementCompanyWebServiceDjango/` directory, create a virtual environment by entering the commands:
```
  python3 -m venv venv
  source .venv/bin/activate
```

Virtual environment activated!

You need to start the server from the directory:
```
ManagementCompanyWebServiceDjango/management_company_interaction_project/
```
To install the required libraries to run the project, write a command in cmd:
```
pip install -r requirements.txt
```

It is necessary to make migrations by writing commands in cmd:

```
python manage.py makemigrations
python manage.py migrate
```

Also, you need to create an application administrator by typing the command in cmd:


```
python manage.py createsuperuser
```

Now you can start the server using the command:

```
python manage.py runserver
```

Everything, the server is running. Now you can go to the url `127.0.0.1:8000` to go to the home page of the site.

____
# Homepage

You went to url `127.0.0.1:8000`.

If you are not logged in, then on the main page you will be offered to log in (log in or register a new organization) by clicking on the necessary button. If authorized, you will be prompted to create new request or view active requests (pending or in progress).

____
# Registration

You went to url `127.0.0.1:8000/accounts/register`.

Everything is simple here: we enter the login and password for the organization, then we enter information about the organization itself. If a field is filled in incorrectly, for example a phone number, a hint is displayed after pressing the button that you entered the phone number incorrectly. An example of telephone input is shown below the input field. If you have successfully registered, you will be redirected to the login page.


____
# Login

You went to url `127.0.0.1:8000/accounts/login` (or redirected).

To log in, you need to specify the correct username and password. If you make a mistake four times, then your IP address will be blocked for 60 seconds: after this time, the blocking is removed, and you can try to log in again. After you successfully log in, you will be redirected to the page for creating request.


____
# Create request

You went to url `127.0.0.1:8000/request/new` (or redirected).

After you successfully log in, you will be redirected to the page for creating request.
This is where you fill out the basic information about the request and upload an image. If you do not upload an image, upload any file, but not an image or an invalid image (there is a footnote at the bottom about valid images), then after clicking on the buttons, a warning is displayed that you have uploaded an invalid image (or even a text file for example). In case of successful creation of the request, you will be redirected to the chat page for the request (let us create request number 1, then url : `127.0.0.1:8000/request/1`)

# Create worker of management company

Here we need to stop a little and separately create a user (s) who will respond to requests in the chat. To do this, go to url `127.0.0.1:8000/admin`. 
We go into the previously created administrator account. Next, add the user manually - you need to come up with a username and password for the manager yourself. Click save.
Next, he needs to set the role of the manager. To do this, next to the "selected groups" tab, click on the add button (green plus sign), then enter "manager" in the name field. Click save. Then click save again to add the manager's rights.
Next, we will deal with the chat page.

____
# Chat request

You went to url `127.0.0.1:8000/request/1` (or redirected).

*The user cannot view other people's chats - this is important!*

One client (the creator of the request) and many managers who can change the status of the request can communicate in the chat.
Customers have only a button for sending a text message, while the manager will display buttons on the page for changing the status of the request and sending system messages. Initially, the status of the request is "pending". The manager can immediately close this request.


____
# List requests

You went to url `127.0.0.1:8000/request/list`

Here you can view the list of open requests. By clicking on one of them, you will be taken to the chat for this request.
