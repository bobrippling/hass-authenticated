"""Constants for authenticated."""

DOMAIN = "authenticated"
INTEGRATION_VERSION = "main"
ISSUE_URL = "https://github.com/rarosalion/authenticated/issues"

STARTUP = f"""
-------------------------------------------------------------------
{DOMAIN}
Version: {INTEGRATION_VERSION}
This is a custom component
If you have any issues with this you need to open an issue here:
https://github.com/rarosalion/authenticated/issues
-------------------------------------------------------------------
"""


CONF_NOTIFY = "enable_notification"
CONF_NOTIFY_ECLUDE_ASN = "notify_exclude_asns"
CONF_NOTIFY_ECLUDE_HOSTNAMES = "notify_exclude_hostnames"
CONF_EXCLUDE = "exclude"
CONF_EXCLUDE_CLIENTS = "exclude_clients"
CONF_PROVIDER = "provider"
CONF_LOG_LOCATION = "log_location"

OUTFILE = ".ip_authenticated.yaml"
