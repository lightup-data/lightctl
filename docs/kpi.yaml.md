# KPI YAML documentation

This document describes the data model for configuring a KPI

```yaml
# Lightup Data Inc.

apiVersion: v1beta

# datasource associated with this KPI. can be specified by either name or uuid.
source:
  name: string
  uuid: string

name: string                            # name of the kpi

description: string                     # optional string that describes this kpi (ignored by the system)

type: [ metric ]

config:
  tableName: string                     # table name - not used with customSql option

  transform:                            # choose one of customSql or function
    customSql: string                   # customSql is data source specific SQL
    function: [ sum | count | count unique | average ]

  timezone: string                      # timezone (see pytz.all_timezones for options, default UTC)

  # interval in seconds - support second, minute, hour, day, week
  interval: [ second | minute | hour | day | week ]

  valueColumn: [ string ]               # columns to monitor
  timestampColumn: string               # timestamp column

  sliceColumn: [ string ]               # list of slice columns
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

tags: [ string ]                        # list of tags associated with this object
```
