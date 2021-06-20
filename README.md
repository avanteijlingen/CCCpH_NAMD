# CCCpH_NAMD
A constant charge version of the NAMD constant pH software and associated tcl scripts.



NAMD source code modified according to: https://jeffcomer.us/downloads.html to allow for PME electrostatics with MARTINI, compile with GCC 8.2.0.



The constant pH TCL files were altered to allow for skipping of the cheap pre-switch evaluation step and force a switch attempt as well as adding a call to a python script which balances charge through a least modifications possible method.





