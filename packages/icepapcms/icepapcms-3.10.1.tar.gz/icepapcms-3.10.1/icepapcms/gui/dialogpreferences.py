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
import logging
from ..lib import ConfigManager, DataBasesTypes
from .messagedialogs import MessageDialogs
from ..helpers import loggingInfo
import os

# TODO Change to properties
MYSQL_PORT = 3306
POSTGRES_PORT = 5432


# TODO: Change Debug Level widget to use more levels
class DialogPreferences(QtWidgets.QDialog):
    log = logging.getLogger('{}.DialogPreferences'.format(__name__))

    @loggingInfo
    def __init__(self, parent):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = self
        with path('icepapcms.gui.ui','dialogpreferences.ui') as f:
            uic.loadUi(f, baseinstance=self.ui)
        self.modal = True
        self.StorageChanged = False
        self.selectedDB = ""

        # Connect Signals
        self.ui.listWidget.itemClicked.connect(self.listWidget_on_click)
        self.ui.btnBrowser.clicked.connect(self.btnBrowse_on_click)
        self.ui.btnLogBrowser.clicked.connect(self.btnLogBrowse_on_click)
        self.ui.btnFirmwareBrowser.clicked.connect(
            self.btnFirmwareBrowse_on_click)
        self.ui.btnTemplatesBrowser.clicked.connect(
            self.btnTemplatesBrowse_on_click)
        self.ui.closeButton.clicked.connect(self.closeButton_on_click)
        self.ui.rbmysql.toggled.connect(self.rbMySql_toogled)
        self.ui.rbpostgres.toggled.connect(self.rbPostgres_toogled)
        self.ui.rbsqlite.toggled.connect(self.rbSqlite_toogled)
        self.ui.btnSnapshotsBrowser.clicked.connect(self.snapshots_browser)
        self.ui.btnConfigsBrowser.clicked.connect(self.configs_browser)

        self.config = ConfigManager()
        self.fillConfig()
        self.ui.listWidget.item(0).setSelected(True)
        """ check imports for dbs to disable errors """

    @loggingInfo
    def closeButton_on_click(self):
        if os.access(self.config.filename, os.W_OK):
            if self.checkPreferences():
                self.config.saveConfig()
                self.close()
            else:
                MessageDialogs.showWarningMessage(self, "Preferences", 
                    "Check configuration parameters")
        else:
            MessageDialogs.showWarningMessage(self, "Preferences", 
                "You must run IcePAPCMS as superuser to change"
                " the configuration parameters.")
            self.fillConfig()

    @loggingInfo
    def listWidget_on_click(self, item):
        index = self.ui.listWidget.row(item)
        self.ui.stackedWidget.setCurrentIndex(index)

    @loggingInfo
    def rbSqlite_toogled(self, checked):
        if checked:
            self.selectedDB = DataBasesTypes.SQLite
            self.ui.gbLocal.setEnabled(True)
            self.ui.gbRemote.setEnabled(False)

    @loggingInfo
    def rbPostgres_toogled(self, checked):
        if checked:
            self.selectedDB = DataBasesTypes.Postgres
            self.ui.gbLocal.setEnabled(False)
            self.ui.gbRemote.setEnabled(True)
            self.ui.txtPort.setText(str(POSTGRES_PORT))

    @loggingInfo
    def rbMySql_toogled(self, checked):
        if checked:
            self.selectedDB = DataBasesTypes.MySQL
            self.ui.gbLocal.setEnabled(False)
            self.ui.gbRemote.setEnabled(True)
            self.ui.txtPort.setText(str(MYSQL_PORT))

    @loggingInfo
    def btnBrowse_on_click(self):
        current_folder = self.config.db_folder
        fn = QtWidgets.QFileDialog.getExistingDirectory(
            self, "Open Folder", current_folder)
        if fn == '':
            return
        folder = str(fn)
        self.ui.txtLocalFolder.setText(folder)

    @loggingInfo
    def btnLogBrowse_on_click(self):
        current_folder = self.config.log_folder
        fn = QtWidgets.QFileDialog.getExistingDirectory(
            self, "Open Log Folder", current_folder)
        if fn == '':
            return
        folder = str(fn)
        self.ui.txtLogFolder.setText(folder)

    @loggingInfo
    def btnFirmwareBrowse_on_click(self):
        current_folder = self.config.firmware_folder
        fn = QtWidgets.QFileDialog.getExistingDirectory(
            self, "Open Firmware Folder", current_folder)
        if fn == '':
            return
        folder = str(fn)
        self.ui.txtFirmwareFolder.setText(folder)

    @loggingInfo
    def btnTemplatesBrowse_on_click(self):
        current_folder = self.config.templates_folder
        fn = QtWidgets.QFileDialog.getExistingDirectory(
            self, "Open Templates Folder", current_folder)
        if fn == '':
            return
        folder = str(fn)
        self.ui.txtTemplatesFolder.setText(folder)

    def snapshots_browser(self):
        current_folder = self.config.snapshots_folder
        fn = QtWidgets.QFileDialog.getExistingDirectory(
            self, "Open Snapshots Folder", current_folder)
        if fn == '':
            return
        folder = str(fn)
        self.ui.txtSnapshotsFolder.setText(folder)

    def configs_browser(self):
        current_folder = self.config.configs_folder
        print(current_folder)
        fn = QtWidgets.QFileDialog.getExistingDirectory(
            self, "Open Configurations Folder", current_folder)
        if fn == '':
            return
        folder = str(fn)
        self.ui.txtConfigsFolder.setText(folder)

    @loggingInfo
    def checkDbEngines(self):
        module_errors = ""
        ok_sqlite = True
        try:
            from sqlite3 import dbapi2 as sqlite
        except ImportError:
            ok_sqlite = False
            module_errors = module_errors + \
                "Sqlite storage not available, requires 'sqlite3'\n"
        self.ui.rbsqlite.setEnabled(ok_sqlite)

        postgres = True
        try:
            import psycopg2
            import psycopg2.extensions
        except BaseException:
            postgres = False
            module_errors += "Postgres storage not available, requires module 'psycopg2'\n"
        self.ui.rbpostgres.setEnabled(postgres)

        mysql = True
        try:
            import MySQLdb
            import MySQLdb.converters
        except BaseException:
            module_errors += "MySQL storage not available, requires module 'MySQLdb'\n"
            mysql = False
        if module_errors != "":
            module_errors += "Check IcepapCMS user manual to solve these " \
                             "issues"
        self.ui.lblModules.setText(module_errors)
        self.ui.rbmysql.setEnabled(mysql)

    @loggingInfo
    def fillConfig(self):
        msg = f'Configuration file: {self.config.filename}'
        self.ui.lblConfigFilename.setText(msg)
        ''' storage configuration'''
        self.checkDbEngines()
        db = self.config.database
        rb = getattr(self.ui, "rb" + db)
        rb.setChecked(True)
        self.ui.txtLocalFolder.setText(self.config.db_folder)
        server = self.config.db_server
        server = server.split(':')
        self.ui.txtHost.setText(server[0])
        self.ui.txtPort.setText(server[1])
        user = self.config.db_user
        pwd = self.config.db_password
        self.ui.txtUser.setText(user)
        self.ui.txtPassword.setText(pwd)

        ''' icepap configuration'''
        debug_enabled = self.config.debug_enabled == str(True)
        self.ui.chkDebug.setChecked(debug_enabled)
        self.ui.sbDebugLevel.setValue(int(self.config.debug_level))
        self.ui.txtLogFolder.setText(self.config.log_folder)
        self.ui.txtFirmwareFolder.setText(self.config.firmware_folder)
        self.ui.txtConfigsFolder.setText(self.config.configs_folder)
        self.ui.txtTemplatesFolder.setText(self.config.templates_folder)
        self.ui.txtSnapshotsFolder.setText(self.config.snapshots_folder)
        self.ui.txtFixedLocationEdit.setText(self.config.fixed_location)

    @loggingInfo
    def checkPreferences(self):
        try:
            ''' Storage Configuration '''

            if self.config.database != str(self.selectedDB):
                self.StorageChanged = True
                self.config.database = str(self.selectedDB)

            if self.ui.rbsqlite.isChecked():
                local_folder = str(self.ui.txtLocalFolder.text())
                if self.config.db_folder != local_folder:
                    self.config.db_folder = local_folder
                    self.StorageChanged = True
            else:
                host = str(self.ui.txtHost.text()).strip()
                port = str(self.ui.txtPort.text()).strip()
                user = str(self.ui.txtUser.text()).strip()
                pwd = str(self.ui.txtPassword.text()).strip()
                if host == "" or port == "":
                    return False
                remote_server = host + ":" + port
                if self.config.db_server != remote_server:
                    self.StorageChanged = True
                    self.config.db_server = remote_server
                if (user != self.config.db_user or pwd !=
                        self.config.db_password):
                    self.StorageChanged = True
                    self.config.db_user = user
                    self.config.db_password = pwd

            ''' icepap configuration'''


            self.config.debug_enabled = str(self.ui.chkDebug.isChecked())
            self.config.debug_level = int(self.ui.sbDebugLevel.value())
            self.config.log_folder = self.ui.txtLogFolder.text()
            self.config.configs_folder = self.ui.txtConfigsFolder.text()
            self.config.firmware_folder = self.ui.txtFirmwareFolder.text()
            self.config.templates_folder= self.ui.txtTemplatesFolder.text()
            self.config.snapshots_folder = self.ui.txtSnapshotsFolder.text()
            self.config.fixed_location = self.ui.txtFixedLocationEdit.text()

            return True
        except BaseException as e:
            self.log.error("Unexpected error on checkPreferences: %s", e)
            return False


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)

    w = DialogPreferences(None)
    w.show()
    sys.exit(app.exec_())