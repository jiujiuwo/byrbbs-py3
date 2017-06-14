HOSTNAME="localhost"
PORT="3306"
USERNAME="root"
PASSWORD="chen12//"
DBNAME="byrbbs4"

replace_sql="replace into test2(url,num) select url,num from test"

mysql -h${HOSTNAME} -P${PORT} -u${USERNAME} -p${PASSWORD} ${DBNAME} -e ${replace_sql}

