Перечень команд по созданию реплики

открываем консоль 1

устанавливаем postgres
sudo -i -u postgres - переключаемся на учетную запись
psql - заходим в postgres
CREATE TABLE workers(id integer PRIMARY KEY, name text); - создаем таблицу
INSERT INTO workers (id, name) VALUES (5, 'Вадим'); - создаем запись
SELECT pg_create_physical_replication_slot('replica'); - создаем слот репликации
SELECT name, setting FROM pg_settings WHERE name IN('wal_level'); - в каком режиме находится журнал wal
SHOW config_file; - где находится сервер

открываем консоль 2

sudo -i -u postgres - переключаемся на учетную запись
pg_basebackup -U postgres --pgdata=/etc/postgresql/12/repl -R --slot=replica
Устанавливаем порт 5555 файле repl/postgresql.auto.conf
Переименовываем файл postgresql.auto.conf в postgresql.conf
Копируем файл 12/main/pg_hba.conf в 12/repl/pg_hba.conf
/usr/lib/postgresql/12/bin/pg_ctl -D '/etc/postgresql/12/repl' start - запускаем сервер реплики

открываем консоль 3

sudo -i -u postgres - переключаемся на учетную запись
pg_lsclusters - проверяем какие серверы работают

SELECT * FROM pg_stat_replication; - смотрим номера записей wal

открываем консоль 4

sudo -i -u postgres - переключаемся на учетную запись
psql -h 127.0.0.1 -p 5555 - заходим в реплику
SELECT * FROM worker; - проверяем появились ли записи
INSERT INTO workers (id, name) VALUES (5, 'Денис'); - проверяем возможность создания записи в реплике - доступ запрещен

Проблемы были в создании третьей учетной записи postgres - из-за этого не мог понять почему реплика не работает.