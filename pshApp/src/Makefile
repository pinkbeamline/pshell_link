TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC = psh
# psh.dbd will be created and installed
DBD += psh.dbd

# psh.dbd will be made up from these files:
psh_DBD += base.dbd

# Include dbd files from all support applications:
#psh_DBD += xxx.dbd

# Add all the support libraries needed by this IOC
#psh_LIBS += xxx

# psh_registerRecordDeviceDriver.cpp derives from psh.dbd
psh_SRCS += psh_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
psh_SRCS_DEFAULT += pshMain.cpp
psh_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#psh_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Finally link to the EPICS Base libraries
psh_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

