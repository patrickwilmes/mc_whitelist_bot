import sqlite3

from mc.constants import DATABASE_NAME_KEY, DATABASE_CONFIG_SECTION, SERVER_WHITELIST_TARGET_KEY, SERVER_CONFIG_SECTION


class UserAlreadyExistsException(Exception):
    pass


class WhitelistHandler(object):
    def __init__(self, config):
        self.config = config
        self._prepare_database()

    def _prepare_database(self):
        con = self._create_connection()
        cur = con.cursor()
        cur.execute('''
        create table if not exists whitelist (
            username varchar(512) primary key
        );
        ''')
        con.commit()
        con.close()

    def add_user(self, username):
        try:
            con = self._create_connection()
            cur = con.cursor()
            cur.execute("insert into whitelist (username) values (?);", (username,))
            con.commit()
            con.close()
            self._generate_whitelist()
        except sqlite3.IntegrityError:
            raise UserAlreadyExistsException

    def del_user(self, username):
        con = self._create_connection()
        cur = con.cursor()
        cur.execute("delete from whitelist where username = ?", (username,))
        con.commit()
        con.close()
        self._generate_whitelist()

    def _generate_whitelist(self):
        con = self._create_connection()
        cur = con.cursor()
        users = list()
        for row in cur.execute("select username from whitelist"):
            users.append(row[0])
        con.commit()
        con.close()
        whitelist_dir = self.config[SERVER_CONFIG_SECTION][SERVER_WHITELIST_TARGET_KEY]
        path = ''
        if whitelist_dir.strip():
            path = '%s/' % whitelist_dir
        with open('%swhitelist.txt' % path, 'w') as file:
            file.writelines(users)

    def _create_connection(self):
        return sqlite3.connect(self.config[DATABASE_CONFIG_SECTION][DATABASE_NAME_KEY])
