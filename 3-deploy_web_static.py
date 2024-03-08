#!/usr/bin/python3
"""
Creates and distributes an archive to web servers.
"""

from fabric.api import env
from fabric.api import local
from fabric.api import put
from fabric.api import run
from datetime import datetime
from os.path import exists, isdir
env.hosts = ['142.44.167.228', '144.217.246.195']


def do_pack():
    """generating tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
        return None


def do_deploy(archive_path):
    """distributing archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        file_nm = archive_path.split("/")[-1]
        no_ext = file_nm.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_nm, path, no_ext))
        run('rm /tmp/{}'.format(file_nm))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except:
        return False


def deploy():
    """creating and distributing archive to web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
