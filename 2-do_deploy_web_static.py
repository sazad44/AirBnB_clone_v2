#!/usr/bin/python3
"""Fab file to archive web_static content"""
from os import remove
from os.path import exists
from fabric.api import *
from datetime import datetime


env.hosts = ['35.190.184.163', '35.185.88.238']

def do_deploy(archive_path):
    """
    uploads archive, uncompresses, and creates new symbolic links
    """
    if not os.path.isfile(archive_path):
        return False
    put(archive_path, "/tmp/")
    splitpath = archive_path.split('/')
    cp_path = ' /data/web_static/releases/' + (splitpath[-1])[:-4]
    tmp_path = '/tmp/' + splitpath[-1]
    if sudo('mkdir -p ' + cp_path).failed:
        return False
    if sudo("tar -xvf " + tmp_path + ' -C' + cp_path).failed:
        return False
    if sudo('mv ' + cp_path + '/web_static/* ' + cp_path).failed:
        return False
    if sudo('rm -rf ' + cp_path + '/web_static').failed:
        return False
    if sudo('rm -rf /data/web_static/current').failed:
        return False
    if sudo('ln -s ' + cp_path + ' /data/web_static/current').failed:
        return False
    print('New version deployed!')
    return True
