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

`python3 -m pip install jupyter-code-server`

## Configuration

### Setting the working directory

`CODE_WORKING_DIRECTORY` is prioritised and can be changed for the VSCode Web IDE independently of the Jupyter working/notebook directory.

The order/priority is as follows:
1. `CODE_WORKING_DIRECTORY`
2. `JUPYTERHUB_ROOT_DIR`
3. `JUPYTER_SERVER_ROOT`
4. `HOME`

### Loading `code-server` using Lmod

An example of loading code-server via Lmod can be found in the branch lmod_pre_start:
[lmod_pre_start](https://github.com/mawigh/jupyter-code-server/tree/lmod_pre_start)

**Important:** You might want to change the loaded code-server version.