echo '=== reseting db ===';
./reset_db.sh;

echo ;
echo ;
echo '=== syncdb and migrate ===';
./manage.py syncdb --migrate --noinput;

echo ;
echo ;
echo '=== fill shop ===';
./manage.py shopfill;

echo ;
echo ;
./manage.py runserver 8002