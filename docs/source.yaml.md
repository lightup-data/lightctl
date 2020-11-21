# Source YAML documentation

This document describes the data model for configuring a data source.

```yaml
# Lightup Data Inc.

apiVersion: v1beta
description: string               # optional string that describes this source. ignored
                                  # by the system.

name: string

# supported data sources 
type: [ postgres | redshift | snowflake | bigquery | athena | databricks | mysql ]

config:
  # configuration parameters for postgres, redshift, mysql, snowflake
  host: string                          # hostname depending on the type.
                                        # for snowflake, you can omit snowflakecomputing.com
                                        # not specified for bigquery.
  username: string                      # username
  password: string                      # password
  dbName: string                        # name of the database to connect to

  # configuration parameters for athena
  # in addition, dbName is also used in athena.
  regionName: string
  accessKeyId: string
  secretAccessKey: string
  stagingDirectory: string

  # configuration parameters for bigquery
  serviceAccountKey: json

  # configuration parameters for databricks
  # in addition, dbName is also used in databricks
  workspaceUrl: string
  workspaceId: string
  clusterId: string  
  token: string

tags: [ string ]                        # list of tags associated with this object
```