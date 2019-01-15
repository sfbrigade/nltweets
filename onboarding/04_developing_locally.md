# Developing Locally

There will be times where as you develop, you may want a local replica of the DB (as to not mess with our production DB hosted on Microsoft Azure). There are two ways of doing this

1. Use `pg_dump` to dump the contents of the production DB. Then, load to your local DB.
2. Run the [pipeline_runner.py](../pipeline/pipeline_runner.py) to parse the data and run all the SQL/Python tasks against your local DB.

Note that you will also need a local instance of Postgres running. See the "(Installing Postgres locally)[./02_development_environment]" for more info on this.

Also note that Option 2 (using the pipeline_runner) is mostly documented in this [README.md](../pipeline/README.md) file. The rest of this doc will go over the steps for using `pg_dump`.

## Using `pg_dump`

`pg_dump` is a utility used for backing up databases: https://www.postgresql.org/docs/9.6/static/app-pgdump.html. You can use `pg_dump` to output the entire contents of a database into a single SQL file. This single SQL file contains everything it takes to recreate the state of the Database at the time it is dumped. You will first need to use `pg_dump` to dump the contents of the DB into a SQL file. Then, you will need to load the contents of that SQL files, but this time, into your local DB.

### Dumping the Production Database
The general command is
```
pg_dump -d datascicongressionaldata --host=hostname --username=username --port=5432 > pg_dump_output.sql
```

In our case, it will look like:

```
pg_dump -d datascicongressionaldata --host=c4sf-sba.postgres.database.azure.com --username=datascicongressionaldata@c4sf-sba --port=5432 > pg_dump_output.sql
```

You will then be prompted for the password. If you need the appropriate DB creds, please message us on Slack!

This will dump the contents of the Database into the file `pg_dump_output.sql`

### Loading Contents to Local DB
To load the contents of `pg_dump_output.sql` into your local DB, on your command line, run:

```
psql $LOCALDBURI < pg_dump_output.sql
```

where $LOCALDBURI is the local connection string to your local Postgres Database.

### Some common problems
In this section, we'll list common problems and how to debug them.

If you run into an error that looks like the following:
```
pg_dump: server version: 9.6.2; pg_dump version: 9.5.7
pg_dump: aborting because of server version mismatch
```

You need to update your version of `pg_dump`. In this case, my `pg_dump` version was 9.5, but the Postgres server version was 9.6. The following is a solution: https://github.com/laradock/laradock/issues/778 (Confirmed that this works on Bash on Ubuntu for Windows. On Mac OS, instead of `apt-get` you will likely use `brew`.)

```
sudo apt-get update
sudo apt-get install wget
sudo add-apt-repository "deb http://apt.postgresql.org/pub/repos/apt/ xenial-pgdg main"
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update
sudo apt-get install postgresql-client-9.6
pg_dump -V
```

This might not actually update the default version of `pg_dump`. What this does is that it installs the updated version of postgresql (in this case 9.6). So if you look for the versions of `pg_dump` using:

```
(datasci-congressional-data) vla@DESKTOP-5P8QQKP /mnt/c/Users/vla/git/datasci-congressional-data (master) $ find / -name pg_dump -type f 2>/dev/null
/usr/lib/postgresql/9.5/bin/pg_dump
/usr/lib/postgresql/9.6/bin/pg_dump
```

One solutions would be to just point the right version of `pg_dump`, for example

```
/usr/lib/postgresql/9.6/bin/pg_dump -d postgres --host=hostname --username=username --port=5432 -s > schema.sql
```

An alternative solution is to use the `--cluster' switch, for example

```
pg_dump --cluster 9.6/main -d postgres --host=hostname --username=username --port=5432 -s > schema.sql
```


You can also just remove the old version of postgresql. In this case, the old version was 9.5, so you can do
```
sudo apt-get remove postgresql-client-9.5
```

| Previous | Next |
|:---------|-----:|
| [Tips and Tricks](./03_tips_and_tricks.md) | [Running the webapp](./04_01_running_the_webapp.md) |
