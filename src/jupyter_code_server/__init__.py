from shutil import which
import os
from subprocess import run
from tempfile import mkstemp

_HERE = os.path.dirname(os.path.abspath(__file__))


def which_code_server():
    command = which('code-server')
    if not command:
        raise FileNotFoundError('Could not find executable code-server!')
    return command


def pre_start_hook(code_server_module):

    LMOD_CMD = os.environ.get('LMOD_CMD', None)
    MODULEPATH = os.environ.get('MODULEPATH', None)
    if not LMOD_CMD and not MODULEPATH:
        raise EnvironmentError('Cannot initializing code-server for the jupyter-code-server proxy! Environment variable LMOD_CMD/MODULEPATH not set.')

    command_to_load = (LMOD_CMD, 'python', '--terse', 'load', str(code_server_module))

    subp = run(command_to_load, capture_output=True, text=True)
    if not subp.returncode == 0:
        raise OSError("Error executing $LMOD_CMD command to preload code-server: " + str(subp.stderr))

    # execute python environment functions from the module load call
    exec(subp.stdout)


def setup_code_server():

    code_server_module = os.environ.get('JSP_CODE_SERVER_LMOD_MODULE', None)
    if code_server_module:
        pre_start_hook(code_server_module)

    which_code_server()

    proxy_config_dict = {
        "new_browser_window": True,
        "timeout": 30,
        "launcher_entry": {
            # Option to disable launcher, e.g. for users that are not supposed to have editor available
            "enabled": False if os.environ.get('JSP_CODE_SERVER_LAUNCHER_DISABLED') else True,
            "title": "VSCode Web IDE",
            "path_info": "vscode",
            "icon_path": os.path.join(_HERE, 'icons/vscode.svg')
            }
        }

    # if code-server is already running and listening to TCP port
    code_server_port = os.environ.get('JSP_CODE_SERVER_PORT', None)
    if code_server_port:
        # set `command` be empty to avoid starting new code-server process and proxy requests to port specified
        proxy_config_dict.update({
            "command": [],
            "port": int(code_server_port)
            })
        return proxy_config_dict

    # if code-server is already running and listening to UNIX socket
    code_server_socket = os.environ.get('JSP_CODE_SERVER_SOCKET', None)
    if code_server_socket:
        # set `command` be empty to avoid starting new code-server process and proxy requests to socket specified
        proxy_config_dict.update({
            "command": [],
            "unix_socket": code_server_socket
            })
        return proxy_config_dict

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
    proxy_config_dict.update({
        "command": full_command,
        "unix_socket": socket_file_name
        })

    return proxy_config_dict
