Гайд на структуру проекта и выкладку

Структура проекта:

project_name (Название проекта)
- python (virtualenv-окружение для проекта)
- project_name (исходники, они гитуются)
- - project_name
- - - public
- - - static
- - - templates
- - - ...
- - app (модули)
- - - ...



Порядок действий для создания нового проекта на машине разработчика:

mkdir project_name
cd project_name
virtualenv --system-site-packages ./python
source ./python/bin/activate
git clone https://github.com/sociogenetics/ptemplate.git
django-admin.py startproject --template=./ptemplate/ project_name
rm -rf ./ptemplate
pip install -r project_name/requirements.txt

Заходим на http://5.172.14.177/phpmyadmin/ и создаем базу под названием project_name

Добавляем в .gitignore папку public путем дописывания в конец файла строчки project_name/public (опционально)



Порядок действий для добавления проекта в гит (на офисный сервак)
**предполагается что файл .gitignore создан и корректно заполнен

cd project_name (исходники)
git init
git add --all
git commit -am "init"
cd ..
git clone --bare project_name
scp -r project_name.git tahy@5.172.14.177:/opt/git/
rm -rf project_name project_name.git **убедиться, что *.git репозиторий корректно скопирован на сервак!!!!!!
git clone tahy@5.172.14.177:/opt/git/project_name.git



Порядок действий для развертывания проекта уже имеющегося в гите (на офисном серваке)

mkdir project_name
cd project_name
virtualenv --system-site-packages ./python
source ./python/bin/activate
git clone tahy@5.172.14.177:/opt/git/project_name.git
pip install -r project_name/requirements.txt

В случае если проект жопный, т.е. собран хуй знает под что и как (а все актуальные проекты такие, блядь),
нет файла requirements.txt и т.п. - импровизируем


Развертывание проекта на хостинге infobox

Делегирование домена:

Прописываем ДНСы на домене:
ns1.pa.infobox.ru
ns2.pa.infobox.ru

Добавляем домен в панели инфобокса "управление доменами->добавить существующий домен"

Создаем А запись в системе ДНС домена
Вида  *.domain_name.ru  109.120.164.95

<через несколько часов когда ДНС-ы прописались>



Выкладка файлов:

Логинимся по ssh под пользователем sgn
cd ~
mkdir domain_name
cd domain_name
mkdir log
virtualenv --system-site-packages ./python
source ./python/bin/activate
git clone tahy@5.172.14.177:/opt/git/project_name.git
pip install -r project_name/requirements.txt
cd project_name/project_name/
mkdir -p public/media public/static
cd ..
chmod +x manage.py
./manage.py collectstatic
**здесь может быть косяк, в пакете файлбраузера какой-то пидарас положил в тестовые картинки файл с неюникод названием


Создание бд:
mysql -u root -p
CREATE DATABASE `project_name` CHARACTER SET utf8 COLLATE utf8_general_ci;

Заливка дампа бд:
mysql -u root -p db_name < dump.sql



Конфигурирование веб-сервера и прочего:

**nginx
cd /etc/nginx/sites-available/
sudo cp nginx.tmpl domain_name.ru
!!Открываем созданный файл, правим пути и названия доменов
sudo ln -s domain_name.ru ../sites-enabled/domain_name.ru

**uwsgi
cd
cp wsgi.tmpl.ini domain_name/wsgi.ini
!!Открываем созданный файл, правим пути и названия доменов

**supervisor
cd /etc/supervisor/conf.d/
sudo cp sudo cp supervisor.tmpl domain_name.conf **суффикс .conf обязателен!
!!Открываем созданный файл, правим пути и названия доменов
!!Обязательно вписать название сайта в директиву [program:domain_name.ru]

Запуск всего этого блядства:
sudo supervisorctl update
sudo service nginx restart

















