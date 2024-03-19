echo "BUILD START"
 python3.9 -m pip install -r requirements.txt
 sudo apt-get install build-dep python-psycopg2
 pip install psycopg2-binary
 python3.9 manage.py collectstatic --noinput --clear
 echo "BUILD END"