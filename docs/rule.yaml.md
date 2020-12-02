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

  tags: [ string ]                      # list of tags associated with this object

config:
  symptom: enum                         # see list of symptoms below

  # Training settings (Also see Advanced settings below). this is only needed for rules that need training
  learningPeriod:                       # update to training period (?)
    startTimestamp: float               # epoch timestamp marking the start of training data (included)
    endTimestamp: float                 # epoch timestamp marking the end of training data (excluded)
    additionalPeriods: [ timeRange ]    # additional time periods to include in learning period

  # Detection settings
  direction: [ up | down | both ]
  aggressiveness:
    level: integer                      # number between 1-10 from low to high aggressiveness
    override: float                     # aggressiveness override (limit usage)

  bounds: bound                         # only valid with out of bounds symptom, see definition of bound below

  driftDuration: integer                # seconds after which drift is considered an incident
  recoveryDuration: integer             # seconds after drift has settled is the incident considered closed

  # Alert configuration
  schedules: [ string ]                 # list of muting schedule uuids
  isMuted: boolean                      # mute the rule
  alertChannels: [ string ]             # list of alerting channel uuids

  # Liveness
  isLive: boolean                       # true if the rule should start running

  # Advanced settings for training - only applicable for some cases
  smoothingWindow: integer
  detectionCriteria: toleranceInterval | zscore | doubleMad

  ownedBy: string                       # username who owns this rule (defaults to the user who created it but can be 
                                        # updated)

status:
  isTrained: boolean                    # true if filter has been trained

  trainingSummary: { string : any }     # training details populated after training completes

  lastUpdatedBy: string                 # username who last updated this rule

  lastSampleTimestamp: float            # epoch timestamp of the last sample that was processed by this rule
```

## Supported Symptom types

The following symptom types are supported

```yaml
- sharpChange
- distributionDrift
- trendChange
- valueChange
- outOfBounds
- sustainedLocalDrift
- driftComparedToPast
```


## Additional structures used above:

```yaml
timeRange:
  startTimestamp: float                 # epoch timestamp
  endTimestamp: float                   # epoch timestamp

bound:
  upper: float
  lower: float
```
