from cronical import app
from cronical.cronical import Cronical

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):

    return Cronical(
            filelist=app.config.filelist, 
            period=app.config["PERIOD"],
            duration=app.config["DURATION"]
        ).ical()
