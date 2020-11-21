# Rule YAML documentation

This document describes the data model for configuring a Rule

```yaml
# Lightup Data Inc.

apiVersion: v1beta

# kpi associated with this rule. can be specified by either name or uuid.
kpi:
  name: string
  uuid: string

name: string                          # name of the rule

description: string                   # optional string that describes this rule (ignored by the system)

symptom: |
  [ sharp_change | distribution_drift | trend_change | value_change | out_of_bounds |
    sustained_local_drift | drift_compared_to_past ]

config:
  # Training settings (Also see Advanced settings below)
  learningPeriod:                   # update to training period (?)
    startTimestamp: datetime format "2020-10-08T10:00:00Z"
    endTimestamp: datetime
    additionalPeriods: [ timeRange ]

  # Detection settings
  direction: [ up | down | both ]
  aggressiveness:
    level: [ 1 | 2 | 3 | ... | 9 | 10 ]
    override: float
  bounds: bound                     # only valid with out of bounds symptom, see definition below

  driftDuration: integer            # seconds after which drift is considered an incident
  recoveryDuration: integer         # seconds after drift has settled is the incident considered closed

  # Alert configuration
  schedules: [ string ]             # list of muting schedule uuids
  isMuted: boolean                  # mute the rule
  alertChannels: [ string ]         # list of alerting channel uuids

  # Liveness
  isLive: boolean                   # true if the rule is live/running

  # Advanced settings for training
  smoothingWindow: integer
  detectionCriteria: [ tolerance_interval | zscore | double_mad ]

tags: [ string ]                        # list of tags associated with this object
```
Additional structures used above:

```yaml
timeRange:
  startTimestamp:
  endTimestamp:

bound:
  upper: float
  lower: float
```