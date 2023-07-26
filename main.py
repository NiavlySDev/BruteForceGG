import requests
from random import choice as random
from time import sleep as wait
from datetime import datetime as current

from BruteForce import Main as BF
from Logique import Main as Logique
from params import FONCTION as demande

VERSION=3.0
AUTHOR="NiavlyS"
NAME="BruteForcerGG"

print(NAME+" by "+AUTHOR+" version "+str(VERSION))

if demande=="BruteForce": BF()
if demande=="Logique": Logique()