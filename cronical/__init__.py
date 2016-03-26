from flask import Flask
from glob import glob


app = Flask(__name__)
app = Flask(__name__)
app.config.from_object('cronical.default_settings')
app.config.from_envvar('CRONICAL_SETTINGS')

filelist = app.config["CRON_DIRS"]

if app.config["USER_CRONTABS"]:
    filelist.extend(glob("/var/spool/cron/*"))

if app.config["SYSTEM_CRONTAB"]:
    filelist.append("/etc/crontab")

# This should make sure there are not dup files in case user configuration
# has /etc/crontab or /var/spool/cron files on CRON_DIRS:
app.config.filelist = set(tuple(filelist))

import cronical.views
