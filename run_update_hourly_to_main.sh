HOSTNAME="localhost"
PORT="3306"
USERNAME="root"
PASSWORD="chen12//"
DBNAME="byrbbs4"
replace_sql="replace into articleinfo(section_url,article_title,article_url,article_createtime,article_comment,article_author,updatetime) select section_url,article_title,article_url,article_createtime,article_comment,article_author,updatetime from articleinfohour"
cd /root/byrbbs/byrbbs-py3/
mysql -h${HOSTNAME} -P${PORT} -u${USERNAME} -p${PASSWORD} ${DBNAME} -e "${replace_sql}"
