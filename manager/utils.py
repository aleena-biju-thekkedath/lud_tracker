import requests
import csv
from django.contrib.auth.models import User

def process_csv_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        decoded_content = response.content.decode('utf-8')
        csv_reader = csv.reader(decoded_content.splitlines(), delimiter=',')
        for row in csv_reader:
            username = row[0]
            email = row[1]
            password = row[2]
            User.objects.create_user(username=username, email=email, password=password)