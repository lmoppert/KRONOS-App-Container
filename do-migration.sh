./manage.py makemigrations chemicals --settings=she.settings.stage
./manage.py migrate admin --settings=she.settings.stage
./manage.py migrate auth --settings=she.settings.stage
./manage.py migrate --settings=she.settings.stage
./manage.py import_files --path /var/www/tmp/Chemicals/ --settings=she.settings.stage
./manage.py runscript legacy_migration --settings=she.settings.stage
