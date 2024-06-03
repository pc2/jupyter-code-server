# jupyter-code-server
Running VSCode Web IDE inside the Jupyter environment

- [jupyter-code-server](#jupyter-code-server)
  - [Installation](#installation)
  - [Configuration](#configuration)
    - [Setting the working directory](#setting-the-working-directory)
    - [Loading `code-server` using Lmod](#loading-code-server-using-lmod)


## Installation
`
`python3 -m pip install jupyter-code-server`
`
## Configuration

### Setting the working directory

`CODE_WORKING_DIRECTORY` is prioritised and can be changed for the VSCode Web IDE independently of the Jupyter working/notebook directory.

The order/priority is as follows:
1. `CODE_WORKING_DIRECTORY`
2. `JUPYTERHUB_ROOT_DIR`
3. `JUPYTER_SERVER_ROOT`
4. `HOME`

### Loading `code-server` using Lmod

