#!/bin/sh

rm newhorizons.db
./manage.py syncdb
./manage.py migrate
./manage.py test advert
./manage.py test banner
./manage.py test blog
./manage.py test course
./manage.py test instructor
./manage.py test inthenews
./manage.py test location
./manage.py test news
./manage.py test node
./manage.py test page
./manage.py test testimonial
./manage.py loaddata node/fixtures/test_data.json
./manage.py loaddata advert/fixtures/test_data.json
./manage.py loaddata banner/fixtures/test_data.json
./manage.py loaddata blog/fixtures/test_data.json
./manage.py loaddata course/fixtures/test_data.json
./manage.py loaddata instructor/fixtures/test_data.json
./manage.py loaddata inthenews/fixtures/test_data.json
./manage.py loaddata location/fixtures/test_data.json 
./manage.py loaddata news/fixtures/test_data.json 
./manage.py loaddata page/fixtures/test_data.json
./manage.py loaddata testimonials/fixtures/test_data.json
echo COPY OVER THE MEDIA FILES
