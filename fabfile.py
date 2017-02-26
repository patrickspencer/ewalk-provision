from fabric.api import *
import configparser

config = configparser.RawConfigParser()
config.read('server_settings.ini')

env.hosts = [config.get('env', 'hosts')]
env.user  = config.get('env', 'user')

def host_type():
    run('uname -s')
