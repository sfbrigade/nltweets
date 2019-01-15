# Development Environment Setup
In this doc, we will go through things you need to install to get on the right "development environment" so that you can start contributing.

The instructions here mostly assume that you are working in a "Linux-like" environment. Without getting too much into the technical details, if you're using a Mac, then you should be fine without too much overhead.

If you're on a Windows, we highly recommend using [Bash on ubuntu on Windows](https://msdn.microsoft.com/en-us/commandline/wsl/about) which provides a Linux environment without needing to spin up an entire Linux virtual machine! (This will only work on Windows 10, if you're on a earlier version, we highly recommend upgrading to the latest version of Windows 10.) To install, follow the [installation guide](https://docs.microsoft.com/en-us/windows/wsl/install-win10). I also think working in a unix-like environment is great experience, especially in the tech world.

**Setting up Ubuntu on Windows**
1. Run powershell as Administrator.
2. In powershell run command: ```Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux```
3. Download/Install Ubuntu from the [windows store](https://www.microsoft.com/en-us/store/p/ubuntu/9nblggh4msv6?rtc=1) 

**Steps for Environment Setup**
The following things to be done in order are:

1. Installing Python via Anaconda
2. Clone the Repository
3. Set up Python Environment using Anaconda
4. Connect to our database/storing DB Creds
5. Installing Postgres locally
6. Testing your dev environment! 

## Installing Python
We use Anaconda
https://www.continuum.io/downloads

You should download the Python 3 version.

In **Windows** you will need to install Anaconda on Ubuntu after downloading:
1. Type ```pwd``` to view your path. It should be similar to: ``` /home/<username>```
2. Now type ```cd ../..```, and then ```ls```
    - You should see: ```bin  boot  dev  etc  home  init  lib  lib64  media  mnt  opt  proc  root  run  sbin  snap  srv  sys  tmp  usr  var```
3. Now type ```cd mnt/c```
    - If you do ```ls``` again, you will see the folders/files of your normal windows system.
4. From there, navigate to the folder that you downloaded Anaconda from.
5. Now type ```bash Anaconda....sh```
    - With ```Anaconda....sh``` being the anaconda downloaded file name

## Clone the Repository
Before cloning the repository, as an optional component, you can install Git Large File Storage. [Git Large File Storage](https://git-lfs.github.com/) is an open source Git extension for versioning large files. This can be a useful tool for storing large files using Git and for the time being we will be downloading and storing somewhat large source data files in our repository which we then will upload into our database. However, this is optional, if you won't be working directly with our ETL processing and processing raw files, you don't necessarily need to worry about this part.

### Installing Git Large File Storage (Optional)

To install visit their [home page](https://git-lfs.github.com/) and/or view the installation [wiki instructions](https://github.com/git-lfs/git-lfs/wiki/Installation).

For example, on MAC OS, you will need to run the following. In addition, you may need to install [Home Brew](https://brew.sh/).

```
brew update
brew install git-lfs
git lfs install
```

### Back to Cloning the Repository

Once you have installed Git Large File Storage (or even if you decided not to), clone the repository. 

By cloning the repository, you are creating a directory local on your machine that will be titled "datasci-congressional-data" (the same name as the reposistory). It's up to you where you want to put this directory, but personally I have created a direcotry named "git" in my home directory and store all my git repository directories within that "git" directory. If you wanted to do this then you can do:

```
# If using Mac
mkdir ~/git

# If using Windows/Ubuntu
mkdir /mnt/c/Users/USERNAME/git
```

Then, inside that "git" directory, clone the repo by running one of the following commands. We recommend using SSH since that'll allow you to push/pull without authenticating every time. If you don't already have your SSH keys set up see the instructions [here](https://help.github.com/articles/connecting-to-github-with-ssh/). However, if you don't want to do that cloning via HTTPS will be "easier" (no additional setup required), but each time you push to the repository you will have to re-enter your GitHub credentials (a minor annoyance).

```
# If using HTTPS
git clone https://github.com/sfbrigade/datasci-congressional-data.git

# If using SSH
git clone git@github.com:sfbrigade/datasci-congressional-data.git
```

## Setting Up Python Environment
Once you've installed Anaconda's distribution of Python, to clone and activate the appropriate python environment:

1. First, make sure in your terminal you are in the root directory of this git repository.
2. `conda env create -f environment.yml`
    1. This clones the appropriate python environment which should be named `datasci-congressional-data`.
    2. See https://conda.io/docs/using/envs.html#use-environment-from-file for more information.
3. `source activate datasci-congressional-data`
    1. This activates the conda python environment
    2. **Note you will need to activate the python environment every time you open a new terminal window** 
4. `conda env update -f environment.yml`
    1. In the future, if you need to update your environment run the above command.

For further information, here is a useful guide to conda environments: https://conda.io/docs/using/envs.html.

Note, the [environment.yml](../environment.yml) file must be kept up to date and is how we will ensure that every group member is on the same environment so any work we do on any machine is reproducible on any other machine.

If you have acitvated your python environment and recieve the following error, you may need to update your python environment using `conda env update -f environment.yml`as described above:<br>
```
ImportError: Couldn't import Django. 
Are you sure it's installed and available on you PYTHONPATH environment variable?
Did you forget to activate a virtual environment?
```

## Connecting to our database
In your `~/.bash_profile` you need to set up environment variables corresponding to the database credentials. Note that if you are using Windows/Ubuntu, you might not have a `~/.bash_profile`, instead you should add the following to your `~/.bashrc` file. Slack the #datasci-congressdata group for the appropriate credentials

### What is a .bash_profile and how do I add to it?
In short, a `~/.bash_profile` is a "hidden file" that is usually located in your home directory in your Linux environment. (`~` refers to the home directory, e.g. if you do `cd ~` you change directory into your home directory). This file is loaded before the Terminal loads your shell environment and contains all the startup configuration and preferences for your command line interface. For example, you can add environment variables, change the color of texts, and add aliases to functions you use on a frequent basis.

To add a line to your `~/.bash_profile`, you can use any text editor that you are familiar with (e.g. `emacs`, `vim`, `nano`). For those with limited experience working in Linux like environments a few quick Google Searches or asking your group members should work! Alternatively, you can also use something like the following to add directly into your `~/.bash_profile`:

```
echo "YOUR TEXT HERE" >> ~/.bash_profile
```

## Installing Postgres locally

### For Mac
The easy way to install Postgres locally if you have a Mac is to use Postgres.app: https://postgresapp.com and just click the download button.

After installing Postgres.app, you will need to update your PATH. Add the following to your `~/.bash_profile`.

```
export PATH=$PATH:/Applications/Postgres.app/Contents/Versions/latest/bin
```

Be sure to restart your terminal before testing `psql` command.

### For Windows/Ubuntu
Installing Postgres via Windows/Ubuntu is a bit harder. The instructions below are actually sourced from this [blog post](https://medium.com/@colinrubbert/installing-ruby-on-rails-in-windows-10-w-bash-postgresql-e48e55954fbf).

1. Download and install the latest stable version of PostgreSQL Windows binary. [PostgreSQL 9.6.2 provided by BigSQL: Download](http://oscg-downloads.s3.amazonaws.com/packages/PostgreSQL-9.6.2-2-win64-bigsql.exe)
2. Now that we have the PostgreSQL downloaded, lets begin to install it.
3. Follow along with the “Setup Wizard” leaving the defaults checked. If you want to install the additional packages you can but it’s not necessary and we don’t need the extra bloat.
4. Once you get to the “Password” section set up your password that you want for your postgres user account. I choose to just have my password be password for ease of use in my local environment. You can choose whatever password that you want but you will need to remember it later on in our work. DO NOT USE “PASSWORD” FOR YOUR PASSWORD IN YOUR PRODUCTION ENVIRONMENT!!!
5. Great we got that installed, we got our password set, lets do a quick sanity check to make sure that our Bash Linux Subsystem is connecting to our Windows installation of PostgreSQL. Run this command from your Bash terminal.

```
psql -p 5432 -h localhost -U postgres
```

If everything was installed properly you should get a response similar to this and the postgres shell prompt.

```
psql (9.5.6, server 9.6.2)
WARNING: psql major version 9.5, server major version 9.6.
         Some psql features might not work.
Type "help" for help.
postgres=#
```

## Verifying Your Development Environment
Congratulations! You've made it this far. At this point you should have completed the following steps:

1. Installing Python via Anaconda
2. Clone the Repository
3. Set up Python Environment using Anaconda
4. Connect to our database/storing DB Creds
5. Installing Postgres locally

If you are having trouble with any of the steps, please feel free to slack the #datasci-congressdata Slack channel.

At this point you should have also created an alias and an environment variable in your `~/.bash_profile` (or `~/.bashrc` if you're using Ubuntu/Windows). Inside your `~/.bash_profile` you should have something like

```
export CD_DWH='DB CREDS'

alias datascicongressionaldatadbwpass='psql "DB CREDS"'
```

Execute the content of your file `~/.bash_profile` or `~/.bashrc` to reflect
your new changes. For example:

```
source ~/.bash_profile
```

Instead of 'DB CREDS' above you should have the actual DB creds which are private, so if you don't have access to those you should ping the #datasci-congressdata Slack channel **and make sure you don't upload them to a public place like GitHub!!**. 

### Testing Postgres Installation

1. Close your current terminal window (just to start fresh) and reopen a new terminal window.
2. `cd` into the GitHub repository.
3. Type `datascicongressionaldatadbwpass` in your terminal and press ENTER:

If all goes well you should see something like this:

```
(datasci-congressional-data) vla@DESKTOP-5P8QQKP /mnt/c/Users/vla/git/datasci-congressional-data (master) $ datascicongressionaldatadbwpass
psql (9.6.4, server 9.6.6)
SSL connection (protocol: TLSv1.2, cipher: ECDHE-RSA-AES256-SHA384, bits: 256, compression: off)
Type "help" for help.

datascicongressionaldata=>
```

To play around, first type `\dn` which is a command in postgres to list all the schemas. If all goes well and you're actually in the right database, you should see:

```
datascicongressionaldata=> \dn
             List of schemas
     Name      |          Owner
---------------+--------------------------
 data_ingest   | datascicongressionaldata
 public        | azure_superuser
 stg_analytics | datascicongressionaldata
 trg_analytics | datascicongressionaldata
(4 rows)
```

Now, type `\d trg_analytics.candidate_contributions`. `\d` is a command in postgres that lists the details of the table that follows it. `trg_analytics.candidate_contributions` is the name of the table we're storing political contributions to candidates in our DB.

If all goes well you should get something like:

```
datascicongressionaldata=> \d trg_analytics.candidate_contributions

   Table "trg_analytics.candidate_contributions"
            Column            |  Type   | Modifiers
------------------------------+---------+-----------
 transaction_id               | text    | not null
 transaction_type             | text    |
 election_cycle               | text    |
 election                     | date    |
 primary_general_indicator    | integer |
 transaction_date             | date    |
 transaction_amount           | numeric |
 filed_date                   | date    |
```

In this case, the list of columns is pretty long, so you'll have to press a key to continue scrolling down. When you wish to exit, press "q" on your keyboard to quit and get back to the terminal.

If you were able to do the above, you've verified your installation of Postgres and storing the alias with DB creds in your `~/.bash_profile` (or `~/.bashrc` for Windows/Ubuntu users)!

### Testing Python Installation

1. Make sure you are in your root directory of the GitHub reposistory. For example, if you `ls` you should see:

```
(datasci-congressional-data) vla@DESKTOP-5P8QQKP /mnt/c/Users/vla/git/datasci-congressional-data (master) $ ls
circle.yml   data_scavenger_hunt  notebooks   pipeline                  README.md            specs  utilities
conftest.py  environment.yml      onboarding  PULL_REQUEST_TEMPLATE.md  reset_git_author.sh  src
```

2. Make sure your Anaconda Python environment is activated. To do this, type `source activate datasci-congressional-data`. Once you've done this the python environment should appear on the left side in parentheses in your command line, for example:
```
(datasci-congressional-data) vla@DESKTOP-5P8QQKP /mnt/c/Users/vla/git/datasci-congressional-data (master) $
```

Notice the parentheses (datasci-congressional-data) preceeding my command line to indicate I am within the conda environment datasci-congressional-data.

3. Now, type `jupyter notebook` on your command line.

With Mac, this should open up a Jupyter notebook in your default browser. With Windows/Ubuntu, you might see something like this:

```
(datasci-congressional-data) vla@DESKTOP-5P8QQKP /mnt/c/Users/vla/git/datasci-congressional-data (master) $ jupyter notebook
[I 23:10:31.692 NotebookApp] Serving notebooks from local directory: /mnt/c/Users/vla/git/datasci-congressional-data
[I 23:10:31.693 NotebookApp] 0 active kernels
[I 23:10:31.693 NotebookApp] The Jupyter Notebook is running at: http://localhost:8888/?token=b61c6d675a273c1e81a17d999e1b0eb4aa39dc4d713bed3d
[I 23:10:31.693 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[W 23:10:31.697 NotebookApp] No web browser found: could not locate runnable browser.
[C 23:10:31.697 NotebookApp]

    Copy/paste this URL into your browser when you connect for the first time,
    to login with a token:
        http://localhost:8888/?token=b61c6d675a273c1e81a17d999e1b0eb4aa39dc4d713bed3d
```

Copy and paste that long string: "http://localhost:8888/?token=b61c6d675a273c1e81a17d999e1b0eb4aa39dc4d713bed3d" into your browser and that will open up the Jupyter notebook.

Now, there is a template notebook in `datasci-congressional-data/notebooks/query_sql_template.ipynb`. In your Jupyter notebook application, click on "notebooks" and then "query_sql_template.ipynb". This should actually open up a Python notebook with some template code.

On the top right, click Kernel --> Restart and Run all. If all goes well, it should take about a minute to run but you should see the cells refresh and valid output. If you get an error the first thing to check is that you set an environment variable `$CD_DWH` with the correct DB credentials. If you need help, ping the #datasci-congressdata channel. If you get other errors, please see our [tips and tricks](./03_tips_and_tricks.md) doc (the next document in this onboarding directory). There is a section on common issues working with Jupyter notebooks.

## Tech Stack

Here are the technologies used in the project, along with some tutorials if you'd like to learn.

| Tech | Version | Purpose | Getting Started |
|------|---------|---------|-----------------|
| Git | 2.4+ | Version control | [Udacity course](https://classroom.udacity.com/courses/ud775), [good comprehensive online book](https://git-scm.com/book/en/v2) |
| Postgres | 9.6 | Database | [Tutorial](https://www.postgresql.org/docs/8.0/static/tutorial.html) |
| PostgreSQL | |  Language used for database queries | [Tutorial from Postgres site](https://www.postgresql.org/docs/9.6/static/tutorial.html) |
| Python | v3 | Data Analysis & Webserver | [Anaconda](https://www.continuum.io/downloads), [Python Language Tutorial](https://docs.python.org/3/tutorial/) |
| Mode Analytics| | Online Application for SQL/Python Reporting and Analyses | [The SQL Tutorial for Data Analysis](https://community.modeanalytics.com/sql/tutorial/introduction-to-sql/)
| SciPy | | Python packages for data analysis | [Intro to Pandas](http://pandas.pydata.org/pandas-docs/stable/10min.html), [NumPy Tutorial](https://docs.scipy.org/doc/numpy-dev/user/quickstart.html) |
| Jupyter | | Easily share Python analysis with code and results | [Quickstart guide](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/) |
| Django | 2.0 | Web server | [Tutorial](https://docs.djangoproject.com/en/2.0/intro/tutorial01/) |
| Django Rest Framework | 3.6 | API Glue | [Tutorial](http://www.django-rest-framework.org/tutorial/1-serialization/) |

As we move forward with the project, we will undoubtedly add Front End technologies as well. Add these in later!

| Previous | Next |
|:---------|-----:|
| [Exploring the Data](./01_exploring_the_data.md) | [Tips and Tricks](./03_tips_and_tricks.md) |

