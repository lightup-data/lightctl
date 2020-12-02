# KPI YAML documentation

This document describes the data model for configuring a KPI

```yaml
# Lightup Data Inc.

apiVersion: v0

type: kpi

metadata:
  # datasource associated with this KPI. can be specified by either name or uuid.
  sources:
    name: string
    uuid: string

  name: string                          # name of the kpi
  uuid: string                          # created by the system

  description: string                   # optional string that describes this kpi (ignored by the system)

  tags: [ string ]                      # list of tags associated with this object

config:
  tableName: string                     # table name - not used with customSql option

  transform:                            # choose one of customSql or function
    customSql: string                   # customSql is data source specific SQL
    function: enum                      # see function types below

  timezone: string                      # timezone (see pytz.all_timezones for options, default UTC)

  interval: integer                     # interval in seconds - second, minute, hour, day, week 
                                        # encoded as 1 | 60 | 3600 | 86400 | 604800

  valueColumns: [ string ]              # columns to monitor
  timestampColumn: string               # timestamp column

  sliceColumns: [ string ]              # list of slice columns
  sliceOptions:                         # options
    include: [ string ]                 # list of slices in the sliceColumn to include
                                        # other slices will be ignored
    exclude: [ string ]                 # list of slices in the sliceColumn to exclude
                                        # other slices will be processed

  seasonality:
    season: integer                     # season in seconds
    period: integer                     # period in seconds

  synchronizationDelay: integer         # delay after which the data is materialized, system will not
                                        # read samples before (now - synchronizationDelay) in seconds
  pollingInterval: integer              # how frequently the data source needs to be polled for
                                        # this KPI in seconds
```

## KPI Aggregation Function Types

```yaml
sum | count | countUnique | average
```