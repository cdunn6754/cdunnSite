# My Personal Website

There are two apps within this project:
1. `content`:
   This houses the post models themselves as well as post topic models.

2. `blogUser`:
   This is very much still a work in progress. Originally I had a traditional
   blog structure where anyone could sign up and post content. I realized as
   I progressed that I wanted it to be my personal portfolio site so had
   to make some changes. Currently this app is not used but I may
   incoporate it in the future to allow people to leave comments on posts.


This is the development version of the site. I have deployed this to elastic
beanstalk temporarily, just to be sure that I could, but it is not currently
deployed anywhere. I want to make some more content posts before doing that.
The two posts that I have are available in the sqlite database that was dumped
in the whole_db.sql file.

If anyone is looking at this and thinking about giving me a job let me give
a brief walkthrough on what needs to be done to restore the database and get
the site running on the dev server.

1. Clone the repo
2. Possibly create at virtualenv, install the packages from requirements.txt,
   assuming you are using Ubuntu do something like
   `pip install -r requirement.txt` from the main project directory.
3. Next, rather than migrating the database like normal just copy the
   database dump file 'whole_db.sql' into the django sqlite database
   by running this command `sqlite3 db.sqlite3 < whole_db.sql`. This
   way you can at least see the content posts that are currently available.
4. Now you should be able to run the site on the local server with
   `python manage.py runserver`
