echo "BUILD START"
python3.10.6 -m  pip install -r requirements.txt
python3.10.6 manage.py collectstatic --noinput --clear
echo "BUILD END"