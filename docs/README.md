This is the documentation folder for the YAML schema

The documentation formatting style follows https://docs.microsoft.com/en-us/azure/devops/pipelines/yaml-schema

Each YAML object follows the template:

```yaml
apiVersion: v0
type: enum                            # see supported object types below

metadata: 
  name:
  uuid:
  description: 
   
  # ... other metadata parameters

config:
  # ... parameters describing the object configuration

status:
  # ... object status descriptors

```

## Supported object types

```yaml
source | kpi | rule | schedule | alertChannel 
```
