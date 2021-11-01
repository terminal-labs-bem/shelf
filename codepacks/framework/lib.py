import pathlib
import configparser
from pathlib import Path
from os.path import join, abspath, isfile, dirname

config = configparser.ConfigParser()

package_link = ".tmp/symlink"
_setuppy = "/setup.py"
_setupcfg = "/setup.cfg"
_dsstore = ".DS_Store"
_repo = "repo"
_back = ".."
_blank = ""
_slash = "/"
_path = str(pathlib.Path(__file__).parent.absolute())

def cwd():
    return join(dirname(__file__))

def join(a, b):
    return abspath(join(a, b))

def split(a):
    return a.split(_slash)

def backout(path):
    return join(path, _back)

def import_fun(mod, func):
    return getattr(__import__(mod, fromlist=[func]), func)

def get_pkg_dir():
    currentpath = cwd()
    i = len(currentpath.split(_slash))
    while i > 0:
        currentpath = join(currentpath, _back)
        if isfile(currentpath + _setuppy):
            return currentpath
            i = -1
        i = i - 1


def find_file(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)


def find_src_dir():
    currentpath = cwd()
    currentpath = currentpath.split(_slash)
    currentpath.reverse()
    build_new_path = False
    new_path = []
    for dir in currentpath:
        if dir == "src":
            build_new_path = True
        if build_new_path == True:
            new_path.append(dir)
    new_path.reverse()
    return "/".join(new_path)


def find_config_file():
    currentpath = cwd()
    currentpath = currentpath.split(_slash)
    currentpath.reverse()
    search = currentpath[:]
    for dir in currentpath:
        search.pop(0)
        candidate = search[:]
        candidate.reverse()
        if find_file("setup.cfg", "/".join(candidate)):
            return find_file("setup.cfg", "/".join(candidate))

def find_local_file():
    currentpath = cwd()
    currentpath = currentpath.split(_slash)
    currentpath.reverse()
    search = currentpath[:]
    for dir in currentpath:
        search.pop(0)
        candidate = search[:]
        candidate.reverse()
        if find_file("local.py", "/".join(candidate)):
            return find_file("local.py", "/".join(candidate))


def is_install_editable():
    if find_src_dir() == "":
        return False
    else:
        return True

def get_pgk_name():
    config.read(find_config_file())
    NAME = config["metadata"]["name"]
    return NAME

def setup_links(package_name):
    _link = package_link + _slash
    Path(_path + _slash + _link).mkdir(parents=True, exist_ok=True)
    if not os.path.islink(_path + _slash + _link + package_name):
        os.symlink(os.path.join(_path, _src), _path + _slash + _link + _slash + package_name)

def smart_reqs(repos, package_name):
    # styles = standalone, repo
    currentpath = _path
    def _get_deploy_style():
        currentpath = _path
        for _ in range(len(split(currentpath))):
            currentpath = backout(currentpath)
            if isdir(currentpath + _slash + ".tmp" + _slash + _repo):
                return _repo

    if _get_deploy_style() == _repo:
        local_repos = os.listdir(join(_path, _back))
        if _dsstore in local_repos:
            local_repos.remove(_dsstore)
        if package_name in local_repos:
            local_repos.remove(package_name)
        for repo in local_repos:
            repos = [_ for _ in repos if not _.endswith(repo + ".git")]
        return repos
    return repos
