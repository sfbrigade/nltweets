# Welcome to Django!

This tutorial is designed for windows user as an additional method to learn Django based on two different sources. 
The first part of the tutorial guides users to creating a local environment, and the second portion is Django’s official tutorial. 
There are additional notes as you progress through it.

Source: [https://djangobook.com/installing-django/](https://djangobook.com/installing-django/)

This Django installation tutorial for Windows offered step by step instructions. It is also available here too.

https://docs.google.com/document/d/15l7eCFeMGns81QyVyYkPxoBJFQEd1j5A0QSQgQieMHM/edit?usp=sharing


##### If you ready to jump into the deep end and have Django experience, then this is a good reference.

https://djangobook.com/advanced-database-management/

 "Installing and configuring a database is not a task for a beginner – luckily, Django installs 
 and configures SQLite automatically, with no input from you, so we will be using SQLite throughout this book. 
 If you would like to work with a “large” database engine like PostgreSQL, MySQL, or Oracle, see Chapter 21."


##### From there, return to the djangoproject.com tutorial 1 – proceed to let’s look at what startproject created: 

*	While examining the file contents, the directory structure is Windows format, so it will look a little different from the tutorial.
*	Use File Explorer to navigate to the file’s location, and a simple text editor, like notepad++, is needed to write to the .py files.
*	Read over the descriptions of the mysite file contents to gain familiarity.

Restart local Django  - Run cmd  as to begin at the command prompt. Change directory(cd)  to the file location and 
start the localized environment variables with  env_mysite\scripts\activate.

For example:
<br>

<code>
C:\Users\<user>\Desktop\django_project>env_mysite\scripts\activate</code><br>
<code>
(env_mysite) C:\Users\<user>\Desktop\django_project></code><br><br>



Double check Python is properly installed.
<br>
<code>
(env_mysite) C:\Users\<user>\Desktop\django_project>python</code><br>

<code>
Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32</code><br>
<code>
Type "help", "copyright", "credits" or "license" for more information.</code><br>
<code>
>>> import django</code><br>
<code>
>>> django.get_version()</code><br>
<code>
'2.0'</code><br>
<code>
>>>exit()</code><br>

From this point, it is up to you as how far you would like to go. 
Also, the first three sections of the Django tutorial should help you to familiarize yourself with it. 

#### Good Luck!!


| Previous | Next |
|:---------|-----:|
| [Machine Learning – Hello World](./06_machine_learning_hello_world.md) | [README](./README.md) |
