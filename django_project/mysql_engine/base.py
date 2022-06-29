import logging

import MySQLdb
from django.db.backends.mysql import base
from django.utils.asyncio import async_unsafe


class DatabaseWrapper(base.DatabaseWrapper):
    def check_connection_for_inactivity(self) -> None:
        if self.connection is None:
            return

        try:
            self.connection.ping()
        except MySQLdb.OperationalError as e:
            if e.args[0] == 4031:  # inactivity
                logging.debug("Lost connection to mysql.. reconnecting")
                conn_params = self.get_connection_params()
                self.connection = self.get_new_connection(conn_params)
            else:
                raise

    @async_unsafe
    def cursor(self):
        """Create a cursor, opening a connection if necessary."""
        self.check_connection_for_inactivity()
        return self._cursor()
