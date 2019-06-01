"""
EXTRA commands Plugin

Demo Bismuth Plugin

Showcase the use of filter event to provide new commands to a node

Defines SCTTR_test1, SCTTR_echo and SCTTR_echo2
"""

import json
import sqlite3
from hashlib import blake2b

__version__ = '0.0.1'


MANAGER = None

VERBOSE = True

# Convention is to have a prefix ending in _ , so prefix and subsequent commands are easily readable.
# Take care not to overload an existing command
PREFIX = "SCTTR_"

class DbHandler:
    def __init__(self):
        self.database = sqlite3.connect("scatter.db")
        self.cursor = self.database.cursor()

    # save data, save hash
    def save(self, data):
        self.cursor.execute("INSERT OR IGNORE INTO data VALUES (?,?)", (data,hash(data)))
        self.database.commit()

    # get data based on hash
    def get(self, hash):
        self.cursor.execute("SELECT * FROM data WHERE hash = ?", (hash,))
        returned = self.cursor.fetchall()[0]
        db_result = {"data": returned[0], "hash": returned[1]}

        return db_result

    # create database if it does not exist
    def create(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS `data` ( '
                   '`data` TEXT, '
                   '`hash` TEST UNIQUE,'
                   'PRIMARY KEY(`hash`)'
                   ' )')

db = DbHandler()
db.create()

def hash(data):
    hashed = blake2b(repr((data)).encode(), digest_size=20).hexdigest()
    return hashed

def action_init(params):
    """Generic plugin init"""
    global MANAGER
    try:
        MANAGER = params['manager']
        MANAGER.app_log.warning("Init SCATTER Plugin")
    except:
        pass


def SCTTR_store(socket_handler):
    """This command takes one param from an extra packet and echoes it back"""
    MANAGER.app_log.warning("EXTRA command SCTTR_store")
    input = MANAGER.execute_filter_hook('receive_extra_packet', {'socket': socket_handler}, first_only=True)
    result = input['data']

    db = DbHandler()
    db.save(result)

    data = json.dumps({"data" : result,"hash" : hash(result)})
    MANAGER.execute_filter_hook('send_data_back', {'socket': socket_handler, 'data': data}, first_only=True)

def SCTTR_get(socket_handler):
    """This command takes one param from an extra packet and echoes it back"""
    MANAGER.app_log.warning("EXTRA command SCTTR_get")
    input = MANAGER.execute_filter_hook('receive_extra_packet', {'socket': socket_handler}, first_only=True)
    result = input['data']

    db = DbHandler()
    data = json.dumps(db.get(result))

    MANAGER.execute_filter_hook('send_data_back', {'socket': socket_handler, 'data': data}, first_only=True)


def my_callback(command_name, socket_handler):
    """The magic is here. This is the generic callback handler answering to the extra command"""
    # This method could stay as this.
    MANAGER.app_log.warning("Got EXTRA command {}".format(command_name))
    if command_name in globals():
        # this allow to transparently map commands to this module functions with no more code
        globals()[command_name](socket_handler)

    elif ' ' in command_name:
        # An alternate way is to define commands with inline param(s) and a custom separator (here, a space)
        command_name, *params = command_name.split(' ')
        if command_name in globals():
            globals()[command_name](socket_handler, params)
    else:
        MANAGER.app_log.warning("Undefined EXTRA command {}".format(command_name))


def filter_extra_commands_prefixes(prefix_dict):
    """
    This is the initial - required - setup step.
    Easy peasy: just add our prefix(es) in the provided dict and send it back.
    """
    prefix_dict[PREFIX] = my_callback
    # More prefixes could go here
    return prefix_dict