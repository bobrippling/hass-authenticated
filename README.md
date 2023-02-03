**Just keeping this great integration for personal use.**
- Unfortunately the original author decided to mark it as deprecated and set it to archive/read only mode.
- Anyway, it still can be used adding this repository as custom repository in HACS.
- Let's hope it will continue to work as long as possible: only perfect and final solution would be someone integrating it into core. 

Original readme below the following line.
______________________

At this point this integtration is considered deprecated.

Parts of it can probably be added to core by someone, if its usefull.

For general info about securing your instance:
- https://www.home-assistant.io/docs/authentication/
- https://www.home-assistant.io/docs/authentication/multi-factor-auth
- https://www.home-assistant.io/docs/configuration/securing/


<details>
  <summary>old readme</summary>
  
  
# authenticated

A platform which allows you to get information successful logins to Home Assistant.

To get started you should know what to get from this repo, or use [HACS](https://hacs.xyz/).

**Example configuration.yaml:**

```yaml
sensor:
  - platform: authenticated
```

**Configuration variables:**

| key | required | default | description
| --- | --- | --- | ---
| **platform** | yes | | The sensor platform name.
| **enable_notification** | no | `true` | Turn on/off `persistant_notifications` when a new IP is detected, can be `true`/`false`.
| **exclude** | no | | A list of IP addresses you want to exclude.
| **provider** | no | 'ipapi' | The provider you want to use for GEO Lookup, 'ipapi', 'extreme', 'ipvigilante'.
| **log_location** | no | | Full path to the logfile.

**Sample overview:**\
![Sample overview](/img/overview.png)

If a new IP is detected, it will be added to a `.ip_authenticated.yaml` file in your configdir, with this information:

```yaml
8.8.8.8:
  city: Mountain View
  country: US
  hostname: google-public-dns-a.google.com
  last_authenticated: '2018-07-26 09:27:01'
  previous_authenticated_time: '2018-07-26 09:27:01'
  region: california
```

If not disabled, you will also be presented with a `persistent_notification` about the event:\
![notification](/img/persistant_notification.png)

## Debug logging

In your `configuration.yaml`

```yaml
logger:
  default: warn
  logs:
    custom_components.sensor.authenticated: debug
```

***

[buymeacoffee.com](https://www.buymeacoffee.com/ludeeus)

  
</details>
