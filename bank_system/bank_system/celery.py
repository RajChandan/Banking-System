from __future__ import absolute_import, unicode_literals
import os
import multiprocessing
from celery import Celery

if os.name == "nt":
    multiprocessing.set_start_method("spawn", force=True)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bank_system.settings")
app = Celery("bank_system")
app.config_from_object("django.conf.settings", namespace="CELERY")

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request : {self.request!r}")
