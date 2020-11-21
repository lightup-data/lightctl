# Alerting Channel YAML documentation

This document describes the data model for configuring an alerting channel

```yaml
# Lightup Data Inc.

apiVersion: v1beta

name: string

description: string                     # optional string that describes this channel (ignored by the system)

# supported alert channels
type: [ slack | email | flock | mattermost ]

config:
  timezone: string                      # list of timezones see pytz.all_timezones, default: UTC

  # used for slack, mattermost and flock
  webHookUrl: string                    # url of webhook to send the alert to 
  channel: string                       # name of the channel eg: # P1 KPIs. Not used by the system 
                                        # other than for display.

  # used for email 
  emailAddressList: [ string ]          # list of emails to send the alert to

  muteResolvedAlerts: boolean           # if true, only send out open alerts (not closed or resolved alerts)
  digestPeriod: [ immediately | hour | day | week ] # when to send out alert messages
  sendHealthyDigests: boolean           # if true, send healthy digests on a daily basis if there were no 
                                        # incidents to report

tags: [ string ]                        # list of tags associated with this object

```