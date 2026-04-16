set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate --noinput
python -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'tabarandiaye772@gmail.com', 'Admin123456!') if not User.objects.filter(username='admin').exists() else print('Admin existe déjà')"