#!/bin/bash

sudo chown www-data:www-data /var/www/she-dev/.*
sudo chown www-data:www-data /var/www/she-dev/* -R
sudo chown www-data:www-data /var/www/she-dev/.hg/* -R
sudo chown www-data:www-data /var/www/static/* -R
sudo chown root:env /var/env/she-dev -R
sudo chown root:env /var/env/she -R
sudo chmod g+rw /var/www/she-dev/* -R
sudo chmod -x /var/www/she-dev/*/*.py -R
sudo chmod -x /var/www/she-dev/*/*/*.py -R
