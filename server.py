from bottle import Bottle
import os
import sentry_sdk
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    dsn="https://d69a7ae27e5941a2b81a20f7ea294c6d@sentry.io/1529854",
    integrations=[BottleIntegration()]
)

app = Bottle()

@app.route("/success")
def success():
    return "OK"

@app.route("/fail")
def fail():
    raise RuntimeError("Error!")

if os.environ.get("APP_LOCATION") == "heroku":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    app.run(host="localhost", port = 8080, debug=True)