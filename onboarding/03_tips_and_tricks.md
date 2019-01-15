# Tips and Tricks

## Working with Git and GitHub
Working with Git and GitHub might seem tricky at first, but I promise it gets much easier as you gain experience with it! Here are some basic instructions, but please feel free to ping the #university channel if you need help.

[Clone this repo locally](https://help.github.com/articles/cloning-a-repository/)
```
$ git clone https://github.com/sfbrigade/datasci-congressional-data.git
$ cd datasci-congressional-data
```
Create your own branch to start work:
```
$ git checkout -b <your-branch-name>
```
To change between branches: 
```
$ git checkout <branch-name>
```

Do some work:

For editing code, feel free to use whatever text editor you are comfortable with. However, we do recommend to use a **text editor** as opposed to a word processor (e.g. Microsoft Word) because a word processor will typically add markups which are not useful for code.

If you don't have an already preferred text editor, we recommend using [Sublime Text 3](https://www.sublimetext.com/3). You can download it for free with an "unlimited" trial period.

Once you've downloaded Sublime Text 3, it's usually helpful to be able to open Sublime Text 3 from the command line. This allows you to edit files much easier. To do this, add the following line to your `~/.bash_profile` (for Mac):

```
alias subl='/Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl'
```

For Windows/Ubuntu (Assuming you set up Bash on Ubuntu for Windows), you can do (this would be for the default installation location, yours may be different):

```
alias subl='"/mnt/c/Program Files/Sublime Text 3/subl.exe"'
```

Then, to open a text file using Sublime from the command line, you can do:

```
$ subl <some-files>
```

When you're ready, commit, [merge any upstream changes](https://help.github.com/articles/merging-an-upstream-repository-into-your-fork/), [deal with conflicts](https://help.github.com/articles/resolving-a-merge-conflict-from-the-command-line/), and push your branch
```
$ git add <edited-files>
$ git commit -m 'my awesome feature'
$ git push
```
[Create a Pull Request](https://help.github.com/articles/creating-a-pull-request/) from your pushed branch (compare branch) to the master branch

Another handy thing while working in terminal is to automatically show what branch you're working on in the command line. To do this, add the following to your `~/.bash_profile`

```
parse_git_branch() {
    git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}
export PS1="\u@\h \[\033[32m\]\w\[\033[33m\]\$(parse_git_branch)\[\033[00m\] $ "
```

## Using the Jupyter Notebook
To access the Jupyter notebook, on Mac OS:

```
$ jupyter notebook
```

On Windows :
```
$ jupyter notebook --no-browser
```

This may say "The Jupyter terminal is running at http://localhost:8888/sometoken." Copy the link and paste it in your browser. 

If you have a Windows computer and are using Bash on Ubuntu on Windows, you may also see an error message about a "dead kernel." [The fix](http://sdsawtelle.github.io/blog/output/bash-and-ipython-on-ubuntu-for-windows.html) is to type in Bash the following: ```$ conda install -c jzuhone zeromq=4.1.dev0```. To learn more about why this works, [click here.](http://sdsawtelle.github.io/blog/output/bash-and-ipython-on-ubuntu-for-windows.html)

Another common issue with using Jupyter and Anaconda Python environments, is that the Jupyter Kernel may not be set to the appropriate environment. This is discussed in [this Stack Overflow post](https://stackoverflow.com/questions/39604271/conda-environments-not-showing-up-in-jupyter-notebook) and the [official docs](http://ipython.readthedocs.io/en/stable/install/kernel_install.html#kernels-for-different-environments). To address this issue, you will need to run:

```
$ source activate datasci-congressional-data
$ python -m ipykernel install --user --name datasci-congressional-data --display-name "Python (datasci-congressional-data)"
```

Then in your Jupyter notebook, you will need to make sure you set your Kernel to the "Python (datasci-congressional-data)". If you have trouble with this, please ping the Slack Channel #datasci-congressdata and/or talk to a project lead.

Note, if you ever need to remove a kernel (which you should not generally have to do) you can run:

```
sudo jupyter kernelspec uninstall datasci-congressional-data
```

For example, if you were to leave the project (hopefully not!!) and don't want unused kernels lying around on your machine you can run the above to remove it.

## Querying tables in our database
There are at least two main ways to query tables in our database.

1. Mode Analytics: For quick querying and analysis, we use [Mode Analytics](https://modeanalytics.com/home/code_for_san_francisco) which is already connected to our database and allows users to use SQL or Python to query and analyze the data. As an example, here's a [report](https://modeanalytics.com/code_for_san_francisco/reports/fda5b308bbd1) that does some basic SQL querying and aggregations.
2. Using Jupyter Notebook: You can also use Python to query the data. A Jupyter notebook is a great way to run Python interactively for quicker results. Note that you will need to get access to our database credentials to query the database directly. If you do not have this already, ping the Slack channel at #datasci-congressdata or ask a project lead.

See https://github.com/sfbrigade/datasci-congressional-data/blob/master/notebooks/query_sql_template.ipynb as an example to query tables in the database

## Working with Git LFS
As part of the [Development Environment](./02_development_environment.md), you probably installed Git LFS which is an open source tool that allows us to put large files in Git. Without going too much into detail, Git LFS replaces large files with text pointers inside Git while storing the file contents in a remote server. This is great for day-to-day use as it keeps the size of the repo small. However, what if you actually need to work with the source CSV data files?

To get the CSV files back, all you need to do is type

```
git lfs pull
```

And this will re-download all the CSV files appropriately. 

## Educational Resources

- Git/GitHub - Free online course at Udacity: https://classroom.udacity.com/courses/ud775

- HTML and CSS - Free online course at Udacity: https://classroom.udacity.com/courses/ud304

- SQL and Python for Data Analyis at Mode Analytics: https://community.modeanalytics.com/sql/tutorial/introduction-to-sql/

- Tidy Data (A good guide for our data models): http://vita.had.co.nz/papers/tidy-data.pdf

| Previous | Next |
|:---------| ----:|
| [Development Environment](./02_development_environment.md) | [Developing Locally](./04_developing_locally.md)|
