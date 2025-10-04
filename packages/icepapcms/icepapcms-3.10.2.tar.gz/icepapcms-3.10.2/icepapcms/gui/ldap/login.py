#!/usr/bin/env python

# -----------------------------------------------------------------------------
# This file is part of icepapcms https://github.com/ALBA-Synchrotron/icepapcms
#
# Copyright 2008-2018 CELLS / ALBA Synchrotron, Bellaterra, Spain
#
# Distributed under the terms of the GNU General Public License,
# either version 3 of the License, or (at your option) any later version.
# See LICENSE.txt for more info.
# -----------------------------------------------------------------------------

from PyQt5 import QtWidgets, uic
from importlib.resources import path
import ldap3
import logging
import re


class DialogLdapLogin(QtWidgets.QDialog):
    log = logging.getLogger('{}.DialogLdapLogin'.format(__name__))

    def __init__(self, servers, user_template, not_allowed=[], parent=None):
        """
        Widget to verify the user on LDAP servers
        :param servers: <list> list of servers to validate the users
                        e.g: [ldap.server.com]
        :param user_template: <str> string format to login on the server
                             e.g: 'uid={},ou=People'
        :param not_allowed: <list> list of users not allowed to use
                            the application e.g: [root]
        :param parent: QtWidget
        """
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = self
        with path('icepapcms.gui.ldap.ui', 'login.ui') as f:
            uic.loadUi(f, baseinstance=self.ui)
        self.username = None

        self.modal = True
        self.flag_error = False
        self.ldap_servers = servers
        self.ldap_user_template = user_template
        self.regex = '(?:% s)' % '|'.join(not_allowed)
        self.dialog_buttons.accepted.connect(self.ok_clicked)
        self.dialog_buttons.rejected.connect(self.reject)
        if not self.flag_error:
            self.user.textChanged.connect(self.user_change)

    def user_change(self, text):
        if re.match(self.regex, text):
            self.user.setStyleSheet('color: red;')
        else:
            self.user.setStyleSheet('color: black;')

    def validate(self):
        if self.flag_error:
            QtWidgets.QMessageBox.critical(
                self, 'Login Error',
                'Wrong ldap configuration contact with support')
            self.clear()
            return False

        user = self.user.text()
        if re.match(self.regex, user):
            self.log.error('Try to log as %s', user)
            QtWidgets.QMessageBox.critical(self, "Login Error",
                                           "User not allowed")
            self.clear()
            return False

        passwd = self.password.text()

        for server in self.ldap_servers:
            s = ldap3.Server(server)
            ldap_user = self.ldap_user_template.format(user)
            connection = ldap3.Connection(s, ldap_user, passwd)
            if connection.bind():
                self.log.info('Login as %s', user)
                self.username = user
                return True

        QtWidgets.QMessageBox.critical(
            self, "Login Error", "Your username or password is incorrect")
        self.clear()
        return False

    def clear(self):
        self.password.setText('')
        self.user.setText('')
        self.user.setFocus()

    def ok_clicked(self):
        if self.validate():
            self.accept()


def main():
    logging.basicConfig(level=logging.INFO)
    import sys
    app = QtWidgets.QApplication(sys.argv)
    d = QtWidgets.QWidget()
    w = DialogLdapLogin(d)
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
