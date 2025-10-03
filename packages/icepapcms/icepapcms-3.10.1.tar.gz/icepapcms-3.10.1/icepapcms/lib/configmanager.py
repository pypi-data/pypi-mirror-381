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


import os
from configobj import ConfigObj
from validate import Validator
import logging
from enum import StrEnum
from ..helpers import loggingInfo
from .singleton import singleton

__all__ = ['ConfigManager', 'DataBasesTypes']

class DataBasesTypes(StrEnum):
    SQLite = 'sqlite'
    Postgres = 'postgres'
    MySQL = 'mysql'


@singleton
class ConfigManager:
    use_user_config = False
    run_expert_mode = False
    run_skip_version_check = False
    run_all_networks = False
    run_debug_level = 'WARNING'
    run_debug_module = ''
    run_debug = False

    if os.name == "nt":
        conf_path_system = os.path.expandvars("%PROGRAMDATA%/IcePAP")
        conf_path_user = os.path.expandvars("~/.icepapcms")
    else:
        conf_path_system = "/etc/icepap"
        conf_path_user = os.path.expanduser("~/.icepapcms")

    username = 'NotValidated'
    log = logging.getLogger('{}.ConfigManager'.format(__name__))


    def __init__(self, expert_mode=False, skip_version_check=False,
                 all_networks=False, filename='', use_user_config=False,
                 debug_level='WARNING', debug_module='', debug=False):

        self.run_expert_mode = expert_mode
        self.run_skip_version_check = skip_version_check
        self.run_all_networks = all_networks
        self.use_user_config = use_user_config
        self.run_debug_level = debug_level
        self.run_debug_module = debug_module
        self.run_debug = debug

        if filename and not os.path.exists(filename):
            # If we specifically ask for a particular config file,
            # then we don't want to start if it doesn't exist.
            raise RuntimeError("Specified configuration file not found!")

        if self.use_user_config:
            filename = os.path.join(self.conf_path_user,
                                    "icepapcms.conf")
        else:
            filename = os.path.join(self.conf_path_system,
                                    "icepapcms.conf" )
            if not os.path.exists(filename):
                filename = os.path.join(self.conf_path_user,
                                                    "icepapcms.conf")

        new_config = not os.path.exists(filename)

        vdt = Validator()

        default_sqlite_folder = os.path.expanduser('~/.icepapcms/sqlitedb')
        default_log_folder = os.path.expanduser('~/.icepapcms/log')
        default_firmware_folder = os.path.expanduser('~/.icepapcms/firmware')
        default_configs_folder = os.path.expanduser("~/.icepapcms/configs")
        default_templates_folder = os.path.expanduser('~/.icepapcms/templates')
        default_snapshots_folder = os.path.expanduser('~/.icepapcms/snapshots')

        defaults_config = [
            f'[database]',
            f'password = string(default=configure)',
            f'folder = string(default={default_sqlite_folder})',
            f'server = string(default=localhost:3306)',
            f'user = string(default=icepapcms)',
            f'database = string(default=sqlite)',
            f'[icepap]',
            f'debug_enabled = string(default=False)',
            f'debug_level = string(default=1)',
            f'log_folder = string(default={default_log_folder})',
            f'configs_folder = string(default={default_configs_folder})',
            f'firmware_folder = string(default={default_firmware_folder})',
            f'templates_folder = string(default={default_templates_folder})',
            f'snapshots_folder = string(default={default_snapshots_folder})',
            f'fixed_location = string(default=*)',
            f'[ldap]',
            f'use = boolean(default=False)',
            f'not_allowed = string(default="List of users no allowed")',
            f'servers = string(default="list of servers")',
            f'user_template=string(default="string with the configuration")',
            f'[all_networks]',
            f'use = boolean(default=False)'
        ]
        self.configspec = ConfigObj(defaults_config)
        self.config = ConfigObj(filename, configspec=self.configspec)
        self.config.validate(vdt, copy=True)

        #Force the absolute path
        self.config["database"]["folder"] = (
            os.path.expanduser(self.config["database"]["folder"]))

        # Other User configuration
        # always create base folder if not found.
        # Using the recursive "makedirs" to create the full path.
        for folder in ("log_folder", "snapshots_folder", "firmware_folder",
                       "templates_folder","configs_folder"):
            directory = os.path.expanduser(self.config["icepap"][folder])
            if not os.path.exists(directory):
                print("Create missing directory: ", directory)
                os.makedirs(directory)
        

        # self.config.filename = self.config_filename
        if new_config:
            self.saveConfig()
        print("Using configuration file: ", self.config.filename)

    @loggingInfo
    def saveConfig(self):
        self.config.write()

    @property
    def filename(self):
        return self.config.filename

    @property
    def database(self):
        return self.config['database']['database']

    @database.setter
    def database(self, value):
        self.config['database']['database'] = value

    @property
    def db_password(self):
        return self.config['database']['password']

    @db_password.setter
    def db_password(self, value):
        self.config['database']['password'] = value

    @property
    def db_folder(self):
        return self.config['database']['folder']

    @db_folder.setter
    def db_folder(self, value):
        self.config['database']['folder'] = value

    @property
    def db_server(self):
        return self.config['database']['server']

    @db_server.setter
    def db_server(self, value):
        self.config['database']['server'] = value

    @property
    def db_user(self):
        return self.config['database']['user']

    @db_user.setter
    def db_user(self, value):
        self.config['database']['user'] = value

    @property
    def debug_enabled(self):
        return self.config['icepap']['debug_enabled']

    @debug_enabled.setter
    def debug_enabled(self, value):
        self.config['icepap']['debug_enabled'] = value

    @property
    def debug_level(self):
        return self.config['icepap']['debug_level']

    @debug_level.setter
    def debug_level(self, value):
        self.config['icepap']['debug_level'] = value

    @property
    def log_folder(self):
        return self.config['icepap']['log_folder']

    @log_folder.setter
    def log_folder(self, value):
        self.config['icepap']['log_folder'] = value

    @property
    def configs_folder(self):
        return self.config['icepap']['configs_folder']

    @configs_folder.setter
    def configs_folder(self, value):
        self.config['icepap']['configs_folder'] = value

    @property
    def firmware_folder(self):
        return self.config['icepap']['firmware_folder']

    @firmware_folder.setter
    def firmware_folder(self, value):
        self.config['icepap']['firmware_folder'] = value

    @property
    def templates_folder(self):
        return self.config['icepap']['templates_folder']

    @templates_folder.setter
    def templates_folder(self, value):
        self.config['icepap']['templates_folder'] = value

    @property
    def snapshots_folder(self):
        return self.config['icepap']['snapshots_folder']

    @snapshots_folder.setter
    def snapshots_folder(self, value):
        self.config['icepap']['snapshots_folder'] = value

    @property
    def fixed_location(self):
        return self.config['icepap']['fixed_location']

    @fixed_location.setter
    def fixed_location(self, value):
        self.config['icepap']['fixed_location'] = value

    @property
    def use_ldap(self):
        return self.config['ldap']['use']

    @property
    def ldap_not_allowed(self):
        return self.config['ldap']['not_allowed']

    @property
    def ldap_servers(self):
        return self.config['ldap']['servers']

    @property
    def ldap_user_template(self):
        return self.config['ldap']['user_template']

    @property
    def use_all_networks(self):
        return self.config['all_networks']['use']
