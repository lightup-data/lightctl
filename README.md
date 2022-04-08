# lightctl - Lightup CLI tool

lightctl is Lightup's CLI tool.

## Installation

<details>
  <summary>[Optional] Setup virtual env</summary>

We prefer that lightctl is installed in a virtual environment to isolate from other dependencies on the system:

```
pip install virtualenv
python3 -m venv .lightctl
source .lightctl/bin/activate
```
</details>


Install using pip:
```
pip install lightctl==0.7.0 --find-links https://s3-us-west-2.amazonaws.com/pypi.lightup.ai/poc/lightctl/index.html
```

<details>
  <summary>[If needed] Install from source</summary>

In the very rare case where you would like to install it from source - you can run the following commands:
```
python3 setup.py build
python3 setup.py install
```
</details>

Verify with:

```
lightctl version
lightctl --help
```

## Usage

You can check the usage of lightctl using the following command:

```lightctl --help```

### API credentials

Lightctl relies on API credentials associated with a specific Lightup cluster. Please see Lightup documentation to see how to get these credentials on a per cluster basis. These credentials can be saved under `~/.lightup/credential`. If saved in a different path, use the command as follows:

```LIGHTCTL_CREDENTIAL_PATH=<path-to-credential> lightctl ...```

or

```
export LIGHTCTL_CREDENTIAL_PATH=<path-to-credential>
lightctl ...
```

### Working with workspaces

Lightctl operates on data objects within the context of a workspace. Commands involve workspace id as a parameter. In the absence of a workspace id parameter, lightctl will use a default workspace (which may or may not exist on your system)

```
lightctl --workspace <workspace id> ....
```


In order to set the base workspace, you can set the environment variable:
```
export LIGHTCTL_DEFAULT_WORKSPACE=<workspace id>
lightctl ...
```
