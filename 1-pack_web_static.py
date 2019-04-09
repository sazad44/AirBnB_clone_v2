#!/usr/bin/python3
import tarfile
from datetime import datetime
from fabric.api import *


def do_pack():
    """Fabric script that generates a .tgx archive"""
    n = datetime.now().strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    result = local("tar -cvzf versions/web_static_{}.tgz web_static".format(n))
    if result.failed:
        return None
    else:
        return "versions/web_static_{}".format(n)
