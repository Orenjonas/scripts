import subprocess, sys, os

"""
A short script for timing taskt.
printing the time between punching in and punching out.

Usage:
    >>> python3 punchclock.py start
    Timer startet
    >>> python3 punchclock.py slutt
    tid:  00:00:05
"""


p = subprocess.Popen(['date', '+%s'], stdout=subprocess.PIPE, universal_newlines=True)
time, err = p.communicate()

if (sys.argv[1] == "start"):
    logfile = open(os.path.join(sys.path[0], 'punchclock.log'), "w+")
    logfile.write(time)
    logfile.close()
    print("Timer startet")

elif (sys.argv[1] == "slutt"):
    logfile = open(os.path.join(sys.path[0], 'punchclock.log'), "r")
    start_tid = logfile.readline()
    logfile.close()
    sekunder = int(time) - int(start_tid)
    os.system("echo 'tid: ' $(date -u -d @{} '+%H:%M:%S')".format(sekunder))

else:
    print("Ukjent kommando")

logfile.close()
