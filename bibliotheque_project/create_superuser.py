# create_superuser.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bibliotheque_project.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

username = "admin"
email = "tabarandiaye772@gmail.com"
password = "Admin123456!"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print(f"✅ Superutilisateur '{username}' créé avec succès!")
else:
    print(f"⚠️ Le superutilisateur '{username}' existe déjà.")