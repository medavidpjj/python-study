#!/usr/bin/python
# _*_coding:utf-8_*_

import os, sys, time, subprocess
import warnings, logging
warnings.filterwarnings("ignore", category=DeprecationWarning)
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy import traceroute


domains = input('input IP/domain:')
target = domains.split(' ')
dport = [80]

if len(target) >= 1 and target[0] != '':
    res,unans = pytraceroute(target, dport=dport,retry=2)
    res.graph(target='>test,svg')
    time.sleep(1)







