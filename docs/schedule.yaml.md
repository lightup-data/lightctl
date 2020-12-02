# Schedule YAML documentation

This document describes the data model for schedules. Schedules are used to define various time ranges.
Primarily schedules are used for muting alerts based on events.

```yaml
# Lightup Data Inc.

apiVersion: v0

type: schedule

metadata:
  name: string
  uuid: string

  description: string                   # description of the muting schedule (ignored by the system)

  tags: [ string ]                      # list of tags associated with this object

config:
  timeRanges: [ timeRange ]             # sequence of time range (see definition of timeRange)

  repeatInterval: integer               # schedule repeat interval in seconds - indicates a recurring event
  repeatCount: integer                  # number of times to repeat a recurring event
```