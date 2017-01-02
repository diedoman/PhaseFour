from app.services import io
from app.models import event


logfile = io.log("PhaseFour.log")
nu = event.Event()
logfile.bWrite(nu.write())

