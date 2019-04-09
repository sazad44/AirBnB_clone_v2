#!/usr/bin/python3
"""Fab file to archive web_static content"""
from os import remove
from os.path import isfile
from fabric.api import *
from datetime import datetime


env.hosts = ['35.190.184.163', '35.185.88.238']


def do_pack():
    """Pack web_static files into archive"""
    try:
        dt = datetime.now().strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions/")
        path = local("tar -cvzf versions/web_static_{}.tgz web_static".format(dt))
        return "versions/web_static_{}.tgz".format(dt)
    except:
        return None

def do_deploy(archive_path):
    """Deploy function for archive to get deployed to servers"""
    if not isfile(archive_path):
        return False
    fileNameExt = archive_path.split('/')[-1]
    fileName = fileNameExt.split(".")[0]
    result = put(archive_path, '/tmp/{}'.format(fileNameExt))
    if result.failed:
        return False
    result = run("rm -rf /data/web_static/releases/{}/".format(fileName))
    if result.failed:
        return False
    result = run("mkdir -p /data/web_static/releases/{}/".format(fileName))
    if result.failed:
        return False
    result = run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
                 .format(fileNameExt, fileName))
    if result.failed:
        return False
    result = run("rm /tmp/{}".format(fileNameExt))
    if result.failed:
        return False
    input = "mv /data/web_static/releases/{}/web_static/*\
 /data/web_static/releases/{}/".format(fileName, fileName)
    result = run(input)
    if result.failed:
        return False
    result = run("rm -rf /data/web_static/releases/{}/web_static"
                 .format(fileName))
    if result.failed:
        return False
    result = run("rm -rf /data/web_static/current")
    if result.failed:
        return False
    result = run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
                 .format(fileName))
    if result.failed:
        return False
    print("New version deployed!")
    return True

def deploy():
    """Call pack and deploy"""
    path = do_pack()
    if path is None:
        return False
    do_deploy(path)
