import os 
import django 
from django.conf import settings 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 
                      'jwt_auth_project.settings')
django.setup()