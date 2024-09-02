'''
RunPod | Endpoint | Dreambooth

This is the handler for the DreamBooth serverless worker.
'''

import os
import base64
import shutil
import requests
import subprocess
from requests.adapters import HTTPAdapter, Retry

import runpod
from runpod.serverless.utils import upload_in_memory_object
from runpod.serverless.utils.rp_validator import validate

from rp_dreambooth import dump_only_textenc, train_only_unet
from rp_custom_model import selected_model
from rp_schemas import TRAIN_SCHEMA




# ---------------------------------------------------------------------------- #
#                                    Handler                                   #
# ---------------------------------------------------------------------------- #
def handler(job):
   print("job received....")


runpod.serverless.start({"handler": handler, "refresh_worker": True})
