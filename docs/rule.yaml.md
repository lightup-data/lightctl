# Rule YAML documentation

This document describes the data model for configuring a Rule

```yaml
# Lightup Data Inc.

apiVersion: v0

type: rule

metadata:
  # kpi associated with this rule. can be specified by either name or uuid.
  kpi:
    name: string
    uuid: string

  name: string                          # name of the rule
  uuid: string                          # uuid of the rule (system implemented - do not fill in)

  description: string                   # optional string that describes this rule (ignored by the system)

config:
  symptom: |
    [ sharp_change | distribution_drift | trend_change | value_change | out_of_bounds |
      sustained_local_drift | drift_compared_to_past ]

  # Training settings (Also see Advanced settings below). this is only needed for 
  learningPeriod:                       # update to training period (?)
    startTimestamp: float               # epoch timestamp marking the start of training data (included)
    endTimestamp: float                 # epoch timestamp marking the end of training data (excluded)
    additionalPeriods: [ timeRange ]

  # Detection settings
  direction: [ up | down | both ]
  aggressiveness:
    level: [ 1 | 2 | 3 | ... | 9 | 10 ]
    override: float

  bounds: bound                         # only valid with out of bounds symptom, see definition of bound below

  driftDuration: integer                # seconds after which drift is considered an incident
  recoveryDuration: integer             # seconds after drift has settled is the incident considered closed

  # Alert configuration
  schedules: [ string ]                 # list of muting schedule uuids
  isMuted: boolean                      # mute the rule
  alertChannels: [ string ]             # list of alerting channel uuids

  # Liveness
  isLive: boolean                       # true if the rule should start running

  # Advanced settings for training
  smoothingWindow: integer
  detectionCriteria: [ tolerance_interval | zscore | double_mad ]

  tags: [ string ]                      # list of tags associated with this object

status:
  isTrained: bool                       # true if filter has been trained
  trainingSummary: json                 # training details

  ownedBy: string                       # username who created/owns this rule

  lastUpdatedBy: string                 # username who last updated this rule

  lastSampleTimestamp: float            # epoch timestamp of the last sample that was processed by this rule
```
Additional structures used above:

```yaml
timeRange:
  startTimestamp: float                 # epoch timestamp
  endTimestamp: float                   # epoch timestamp

bound:
  upper: float
  lower: float
```