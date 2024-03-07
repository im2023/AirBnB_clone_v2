#!/usr/bin/python3
"""
A Fabric script that generates tgz archive from contents of web_static
folder of the AirBnB Clone repo
"""

from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """generates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_nam = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_nam))
        return file_nam
    except:
        return None
