Hello, Everyone!

Here is Some assessment test project on Python 
(docker, django, postgres, redis, celery)

All confs files in repository, so you can pull and start in few commands.

Terminal commands:
1. docker-compose build
2. docker-compose up

After all process starts well, pls, open second terminal window and do next commands:
1. docker-compose run web python manage.py makemigrations
2. docker-compose run web python manage.py migrate
3. docker-compose run web python manage.py createsuperuser (enter email and password for new admin user)

If all commands done well, you can say: "I solemnly swear that I am only plotting a prank" and start create posts, 
    comments and also upvote posts.

URLs:
1. http://0.0.0.0:8000/admin - Django Admin
2. http://0.0.0.0:8000/posts/posts [post, get, put, patch, delete] - Posts CRUD
3. http://0.0.0.0:8000/posts/comments [post, get, put, patch, delete] - Comments CRUD
4. http://0.0.0.0:8000/posts/vote [post, get, delete] - Comments CRD

FYI:
1. Posts redactor and destroy possible for post's author (you can check it in "posts" app's permissions file)
2. Comments update and destroy possible for comment's author, also comment can be deleted by the author of the post 
   to which the comment relates (you can check it in "posts" app's permissions file)