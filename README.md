## 실행 방법
1. `cd mysite`
2. `python -m venv venv`
3. `venv\Scripts\activate`
4. `pip install -r requirements.txt`
5. `set DJANGO_SETTINGS_MODULE=mysite.settings`
6. `python.exe -m pip install --upgrade pip`
7. `pip install django-tinymce`
8. `python manage.py makemigrations`
9. `python manage.py runserver`


``` PS C:\Project\teamtwo\django> cd mysite
PS C:\Project\teamtwo\django\mysite> python manage.py runserver
Watching for file changes with StatReloader
Exception in thread django-main-thread:
Traceback (most recent call last):

ModuleNotFoundError: No module named 'tinymce'
오류가 뜰 경우 pip install django-tinymce 적기
