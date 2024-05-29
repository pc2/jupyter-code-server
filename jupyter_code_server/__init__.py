from shutil import which
import os
from tempfile import mkstemp

_HERE = os.path.dirname(os.path.abspath(__file__))


def pre_start_hook():
    """ 
    Useful for loading code-server via e.g. Lmod
    """
    pass


def which_code_server():
    command = which('code-server')
    if not command:
        raise FileNotFoundError('Could not find executable code-server!')
    return command


def setup_code_server():

    pre_start_hook()

    working_directory = os.environ.get('CODE_WORKING_DIRECTORY', None)
    if not working_directory:
        working_directory = os.environ.get('JUPYTERHUB_ROOT_DIR', os.environ.get('JUPYTER_SERVER_ROOT', os.environ.get('HOME')))

    additional_arguments = []

    socket_file, socket_file_name = mkstemp()

    command_arguments = [
        '--socket={unix_socket}',
        '--auth=password',
        '--disable-update-check',
        '--disable-file-uploads',
        '--disable-file-downloads',
        '--ignore-last-opened'  # needed to set a specific working directory
    ]

    full_command = [which_code_server()] + command_arguments + additional_arguments + ['--'] + [working_directory]

    return {
        "command": full_command,
        "unix_socket": socket_file_name,
        "new_browser_window": True,
        "timeout": 30,
        "launcher_entry": {"title": "VSCode Web IDE", "path_info": "vscode", "icon_path": os.path.join(_HERE, 'icons/vscode.svg')}
    }
