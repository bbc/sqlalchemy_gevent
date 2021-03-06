from setuptools import setup, find_packages

setup(name="sqlalchemy_gevent",
	version = '0.2',
	url="https://github.com/hkwi/sqlalchemy_gevent",
	author="Hiroaki KAWAI",
	author_email="hiroaki.kawai@gmail.com",
	py_modules=["sqlalchemy_gevent",],
	install_requires = ["sqlalchemy", "gevent>=1.0"],
	entry_points = ''' 
[sqlalchemy.dialects]
gevent_drizzle=sqlalchemy_gevent:DrizzleDialect
gevent_drizzle.mysqldb=sqlalchemy_gevent:DrizzleMysqldbDialect
gevent_firebird=sqlalchemy_gevent:FirebirdDialect
gevent_firebird.fdb=sqlalchemy_gevent:FirebirdFdbDialect
gevent_firebird.kinterbasdb=sqlalchemy_gevent:FirebirdKinterbasdbDialect
gevent_mssql.adodbapi=sqlalchemy_gevent:MssqlAdodbapiDialect
gevent_mssql=sqlalchemy_gevent:MssqlDialect
gevent_mssql.mxodbc=sqlalchemy_gevent:MssqlMxodbcDialect
gevent_mssql.pymssql=sqlalchemy_gevent:MssqlPymssqlDialect
gevent_mssql.pyodbc=sqlalchemy_gevent:MssqlPyodbcDialect
gevent_mssql.zxjdbc=sqlalchemy_gevent:MssqlZxjdbcDialect
gevent_mysql.cymysql=sqlalchemy_gevent:MysqlCymysqlDialect
gevent_mysql=sqlalchemy_gevent:MysqlDialect
gevent_mysql.gaerdbms=sqlalchemy_gevent:MysqlGaerdbmsDialect
gevent_mysql,mysqlconnector=sqlalchemy_gevent:MysqlMysqlconnectorDialect
gevent_mysql.mysqldb=sqlalchemy_gevent:MysqlMysqldbDialect
gevent_mysql.oursql=sqlalchemy_gevent:MysqlOursqlDialect
gevent_mysql.pymysql=sqlalchemy_gevent:MysqlPymysqlDialect
gevent_mysql.pyodbc=sqlalchemy_gevent:MysqlPyodbcDialect
gevent_mysql.zxjdbc=sqlalchemy_gevent:MysqlZxjdbcDialect
gevent_oracle.cx_oracle=sqlalchemy_gevent:OracleCx_oracleDialect
gevent_oracle=sqlalchemy_gevent:OracleDialect
gevent_oracle.zxjdbc=sqlalchemy_gevent:OracleZxjdbcDialect
gevent_postgresql=sqlalchemy_gevent:PostgresqlDialect
gevent_postgresql.pg8000=sqlalchemy_gevent:PostgresqlPg8000Dialect
gevent_postgresql.psycopg2=sqlalchemy_gevent:PostgresqlPsycopg2Dialect
gevent_postgresql.pypostgresql=sqlalchemy_gevent:PostgresqlPypostgresqlDialect
gevent_postgresql.zxjdbc=sqlalchemy_gevent:PostgresqlZxjdbcDialect
gevent_sqlite=sqlalchemy_gevent:SqliteDialect
gevent_sqlite.pysqlite=sqlalchemy_gevent:SqlitePysqliteDialect
gevent_sybase=sqlalchemy_gevent:SybaseDialect
gevent_sybase.pyodbc=sqlalchemy_gevent:SybasePyodbcDialect
gevent_sybase.pysybase=sqlalchemy_gevent:SybasePysybaseDialect
'''
)

