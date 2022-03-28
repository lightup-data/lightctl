# lightctl - Lightup CLI tool 

lightctl is Lightup's CLI tool.

Install using pip:
```
pip install lightctl==0.7.0 --find-links https://s3-us-west-2.amazonaws.com/pypi.lightup.ai/poc/lightctl/index.html
```

Install from source:

```
python3 setup.py build
python3 setup.py install
```

Verify with:

```
lightctl version
lightctl --help
```

Usage:

You can check the usage of lightctl using the following command: 

```lightctl --help```

API credentials

Lightctl relies on API credentials associated with a specific Lightup cluster. Please see Lightup documentation to see how to get these credentials on a per cluster basis. These credentials can be saved under `~/.lightup/credential` or if in a different path, as follows:

```LIGHTUP_API_CREDENTIAL=<path-to-credential> lightctl ...```
