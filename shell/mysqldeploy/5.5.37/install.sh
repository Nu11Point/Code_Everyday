#!/usr/bin/env bash
#time: 2019-03-20
#auth: victor
#func: mysql auto install
#vers: 5.5.37

path=`pwd`
prefix="/usr/local/mysql"
datadir="/data/mydata"
logdir="/data/mylog"

useradd mysql
mkdir /usr/local/mysql
mkdir /usr/local/mysql/run
mkdir -p /data/mydata
mkdir -p /data/mylog/log
chown mysql.mysql /data -R
chown mysql.mysql /usr/local/mysql -R

tar xf mysql-5.5.37.tar.gz
cd mysql-5.5.37
yum -y install gcc gcc-c++ cmake bison ncurses-devel zlib libxml2 libxml2-devel

source $path/env.sh 

cmake .                                             \
  -DSYSCONFDIR=${prefix}                            \
  -DCMAKE_INSTALL_PREFIX=${prefix}                  \
  -DCMAKE_BUILD_TYPE=Release                      \
  -DENABLE_PROFILING=1                            \
  -DWITH_DEBUG=0                                  \
  -DWITH_VALGRIND=0                               \
  -DENABLE_DEBUG_SYNC=0                           \
  -DWITH_EXTRA_CHARSETS=all                       \
  -DWITH_SSL=bundled                              \
  -DWITH_UNIT_TESTS=0                             \
  -DWITH_ZLIB=bundled                             \
  -DWITH_PARTITION_STORAGE_ENGINE=1               \
  -DWITH_INNOBASE_STORAGE_ENGINE=1                \
  -DWITH_ARCHIVE_STORAGE_ENGINE=1                 \
  -DWITH_BLACKHOLE_STORAGE_ENGINE=1               \
  -DWITH_PERFSCHEMA_STORAGE_ENGINE=1              \
  -DDEFAULT_CHARSET=utf8                                 \
  -DDEFAULT_COLLATION=utf8_general_ci                    \
  -DWITH_EXTRA_CHARSETS=all                              \
  -DENABLED_LOCAL_INFILE=1                        \
  -DWITH_EMBEDDED_SERVER=0                               \
  -DINSTALL_LAYOUT=STANDALONE                     \
  -DCOMMUNITY_BUILD=1                             \
  -DMYSQL_SERVER_SUFFIX='-r5436';

make & make install
${prefix}/scripts/mysql_install_db --user=mysql --datadir=${datadir} --basedir=${prefix}
echo 'export PATH=/usr/local/mysql/bin:$PATH'>>/etc/profile
echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/mysql/lib'>>/etc/profile
source /etc/profile
\cp ../my.cnf /etc/ -ra
${prefix}/bin/mysqld &

tail -f /data/mylog/alter.log
