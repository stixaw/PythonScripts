import os
import shutil
import sys
from os.path import join, abspath
import win32wnet
import tempfile
import logging
import threading
import stat
import subprocess
import getopt
import time
import re

string = r'\test\7.1.000.0\20111014145600\PL'
for line in string:
	re.sub(r'\test\d{24}', '\\', string)

print string