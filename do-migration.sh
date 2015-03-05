./manage.py makemigrations chemicals
./manage.py migrate
./manage.py import_files --path /var/www/tmp/Chemicals/ --settings=she.settings.stage 
./manage.py runscript legacy_migration
