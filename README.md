[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/pc2/jupyter-code-server/main)

# jupyter-code-server

Running VSCode Web IDE code-server inside the Jupyter environment.

![JupyterLab ](./imgs/code_lab_icon.png)

## Table of Contents

- [jupyter-code-server](#jupyter-code-server)
  - [Table of Contents](#table-of-contents)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Configuration](#configuration)
    - [Setting the working directory](#setting-the-working-directory)
    - [Loading `code-server` using Lmod](#loading-code-server-using-lmod)


## Requirements

* Installed version of [https://github.com/coder/code-server](https://github.com/coder/code-server)
  * If code-server is installed via Lmod: [Loading `code-server` using Lmod](#loading-code-server-using-lmod)
* `jupyter-server-proxy>=4.1.2`

## Installation

```
python3 -m pip install jupyter-code-server
```

## Configuration

### Setting the working directory

The environment variable `CODE_WORKING_DIRECTORY` is prioritised and can be changed for the VSCode Web IDE independently of the Jupyter working/notebook directory.

The order/priority is as follows:
1. `CODE_WORKING_DIRECTORY`, if not set:
2. `JUPYTERHUB_ROOT_DIR`, if not set:
3. `JUPYTER_SERVER_ROOT`, if not set:
4. `HOME`

### Loading `code-server` using Lmod

An example of loading code-server via Lmod can be found in the branch lmod_pre_start:
[lmod_pre_start](https://github.com/mawigh/jupyter-code-server/tree/lmod_pre_start)

**Important:** You might want to change the loaded code-server version.
### Using pre-started code-server

In case code-server is already running (e.g. started in sidecar container with Jupyter running in Kubernetes)
and servig either via TCP port or UNIX socket, it is possible to proxy this already running instance instead
of starting a new one with jupyter-server-proxy. Variables `JSP_CODE_SERVER_PORT` and `JSP_CODE_SERVER_SOCKET`
set `command` to empty list which makes `jupyter-server-proxy` pass requests to specified port of socket.

If running code-server is listening to TCP port, environment variable `JSP_CODE_SERVER_PORT` may be set to
port number.

If running code-server is listening to UNIX socket, environment variable `JSP_CODE_SERVER_SOCKET` may be set to
socket file path.

If none of these environment variables are set, jupyter-code-server starts new code-server process and proxies
requests to its socket.
