#!../../bin/linux-x86_64/psh

## You may have to change psh to something else
## everywhere it appears in this file

< envPaths

cd "${TOP}"

## Register all support components
dbLoadDatabase "dbd/psh.dbd"
psh_registerRecordDeviceDriver pdbbase

## Load record instances
dbLoadRecords("db/psh.db","BL=PINK,DEV=STS")

cd "${TOP}/iocBoot/${IOC}"
iocInit

## Start any sequence programs
#seq sncxxx,"user=epics"
