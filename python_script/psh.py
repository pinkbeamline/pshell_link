#!/home/epics/miniconda3/envs/pshell_client/bin/python3

from pshell import client as psc
import time
import queue
import epics

## global queue variable
qbuff = queue.Queue()

## Constants
MAXARRAYSIZE = 131072

## event callback
def on_event(name, value):
    global qbuff
    qbuff.put(value)

## setup pschell client event subscription
ps = psc.PShellClient("http://pink-shuttle02:8080")
print(ps.get_state())
ps.start_sse_event_loop_task(["shell"], on_event)

## set PV connections
pvtxtout = epics.PV("PINK:STS:pshell", auto_monitor=False)
pvbuffsize = epics.PV("PINK:STS:buffersize", auto_monitor=False)

txtbuffer = []
txtstr = ""

print("Running pshell client listener service...")
while(1):
    if qbuff.qsize()>0:
        while qbuff.qsize():
            txtbuffer.append(str(qbuff.get()))
        try:
            buffsize = int(pvbuffsize.get())
            txtbuffer = txtbuffer[-buffsize:]
            txtstr = '\n'.join(txtbuffer)
            if len(txtstr) > MAXARRAYSIZE:
                txtstr = txtstr[-MAXARRAYSIZE:]
            pvtxtout.put(txtstr)
        except:
            print("Failed to post buffer to PV. Check IOC")
    time.sleep(1)
