Перечень команд по созданию реплики

открываем консоль 1

устанавливаем postgres <br>
sudo -i -u postgres - переключаемся на учетную запись <br>
psql - заходим в postgres <br>
CREATE TABLE workers(id integer PRIMARY KEY, name text); - создаем таблицу <br>
INSERT INTO workers (id, name) VALUES (5, 'Вадим'); - создаем запись <br>
SELECT pg_create_physical_replication_slot('replica'); - создаем слот репликации <br>
SELECT name, setting FROM pg_settings WHERE name IN('wal_level'); - в каком режиме находится журнал wal <br>
SHOW config_file; - где находится сервер <br>

открываем консоль 2

sudo -i -u postgres - переключаемся на учетную запись <br>
pg_basebackup -U postgres --pgdata=/etc/postgresql/12/repl -R --slot=replica <br>
Устанавливаем порт 5555 файле repl/postgresql.auto.conf <br>
Переименовываем файл postgresql.auto.conf в postgresql.conf <br>
Копируем файл 12/main/pg_hba.conf в 12/repl/pg_hba.conf <br>
/usr/lib/postgresql/12/bin/pg_ctl -D '/etc/postgresql/12/repl' start - запускаем сервер реплики <br>

открываем консоль 3

sudo -i -u postgres - переключаемся на учетную запись <br>
pg_lsclusters - проверяем какие серверы работают <br>

SELECT * FROM pg_stat_replication; - смотрим номера записей wal <br>

открываем консоль 4

sudo -i -u postgres - переключаемся на учетную запись <br>
psql -h 127.0.0.1 -p 5555 - заходим в реплику <br>
SELECT * FROM worker; - проверяем появились ли записи <br>
INSERT INTO workers (id, name) VALUES (5, 'Денис'); - проверяем возможность создания записи в реплике - доступ запрещен <br>

Проблемы были в создании третьей учетной записи postgres - из-за этого не мог понять почему реплика не работает.