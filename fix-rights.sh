#!/bin/bash

# Fix production dirs
sudo chown www-data:www-data /var/www/she/.*
sudo chown www-data:www-data /var/www/she/* -R
sudo chown www-data:www-data /var/www/she/.hg/* -R
sudo chown www-data:www-data /var/www/static/she/* -R
sudo chown root:env /var/env/she -R
sudo chmod g+rw /var/www/she/* -R
sudo chmod -x /var/www/she/*/*.py -R
sudo chmod -x /var/www/she/*/*/*.py -R

# Fix development dirs
sudo chown www-data:www-data /var/www/dev-she/.*
sudo chown www-data:www-data /var/www/dev-she/* -R
sudo chown www-data:www-data /var/www/dev-she/.hg/* -R
sudo chown www-data:www-data /var/www/static/dev-she/* -R
sudo chown root:env /var/env/dev-she -R
sudo chmod g+rw /var/www/dev-she/* -R
sudo chmod -x /var/www/dev-she/*/*.py -R
sudo chmod -x /var/www/dev-she/*/*/*.py -R
