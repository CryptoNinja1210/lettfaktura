python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py collectstatic
# python3 manage.py collectstatic --noinput