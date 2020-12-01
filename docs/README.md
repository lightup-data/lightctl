This is the documentation folder for the YAML schema

The documentation formatting style follows https://docs.microsoft.com/en-us/azure/devops/pipelines/yaml-schema

Each YAML object follows the template:

```yaml
apiVersion: v0
type: [ source | metric | rule | alertchannel | schedule ]

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
