# Alert Channel YAML documentation

This document describes the data model for configuring an alerting channel

```yaml
# Lightup Data Inc.

apiVersion: v0

type: alertChannel

metadata:
  name: string
  uuid: string                          # created by the system (do not populate)  
 
  description: string                   # optional string that describes this channel (ignored by the system)

  tags: [ string ]                      # list of tags associated with this object

config:
  type: enum                            # see the list of types below

  timezone: string                      # list of timezones see pytz.all_timezones, default: UTC

  # used for slack, mattermost and flock
  webHookUrl: string                    # url of webhook to send the alert to 
  channel: string                       # name of the channel eg: # P1 KPIs. Not used by the system 
                                        # other than for display.

  # used for email 
  emailAddressList: [ string ]          # list of emails to send the alert to

  muteResolvedAlerts: boolean           # if true, only send out open alerts (not closed or resolved alerts)
  digestPeriod: 0 | 3600 | 86400 | 604800  # when to send out alert messages - immediately, hourly, daily, weekly
  sendHealthyDigests: boolean           # if true, send healthy digests on a daily basis if there were no 
                                        # incidents to report
```

## Alert Channel Types

The types of alert channels that are currently supported are 
```yaml
slack | email | flock | mattermost
```