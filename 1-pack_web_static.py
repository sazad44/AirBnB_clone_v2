#!/usr/bin/python3
"""Fab file to archive web_static content"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Pack web_static files into archive"""
    dt = datetime.now().strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions/")
    path = local("tar -cvzf versions/web_static_{}.tgz web_static".format(dt))
    return path
