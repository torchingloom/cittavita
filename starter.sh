echo '=== reseting db ===';
./reset_db.sh;

echo ;
echo ;
echo '=== syncdb and migrate ===';
./manage-dev.py syncdb --migrate --noinput;

echo ;
echo ;
echo '=== fill shop ===';
./manage-dev.py shopfill;

echo ;
echo ;
./run.sh