import pymysql
import click
from flask import current_app, g


def get_db():
    if 'db' not in g:
        conn = pymysql.connect(host='localhost',
                               port=3306,
                               user='root',
                               password='1234',
                               db='pymysql_db',
                               charset='utf8')
        click.echo('db connect.')
        g.db = conn
    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
