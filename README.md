# Constant pH Coarse-Grained Molecular Dynamics with Stochastic Charge Neutralization - in NAMD

## Publication

Alexander van Teijlingen, Hamish W. A. Swanson, King Hang Aaron Lau, and Tell Tuttle
The *Journal of Physical Chemistry Letters* 2022 13 (18), 4046-4051
DOI: https://doi.org/10.1021/acs.jpclett.2c00544


![Abstract.png](.\Abstract.png)

## Description

A constant charge version of the NAMD constant pH software and associated tcl scripts.



NAMD source code modified according to: https://jeffcomer.us/downloads.html to allow for PME electrostatics with MARTINI, compile with GCC 8.2.0.



The constant pH TCL files were altered to allow for skipping of the cheap pre-switch evaluation step and force a switch attempt as well as adding a call to a python script which balances charge through a least modifications possible method.


## Common errors encoutered when using Constant pH Molecular Dynamics in NAMD

Something that looks like this:
``` tcl
FATAL ERROR: 
MOLECULE DESTROYED BY FATAL ERROR!  Use resetpsf to start over.
    while executing
"psfset resname $segid $resid $realName"
    (procedure "buildSystem" line 66)
    invoked from within
"buildSystem {*}$args"
    ("build" arm line 2)
    invoked from within
"switch -nocase -- $action {
        get {
            cphSystemGet {*}$args
        }
        set {
            cphSystemSet {*}$args
        }
      ..."
    (procedure "cphSystem" line 2)
    invoked from within
"cphSystem build [readConfig] $excludeList"
    (procedure "initialize" line 39)
    invoked from within
"initialize"
    (procedure "cphRun" line 6)
    invoked from within
"cphRun 5000 100000000"
    (file "CPHMD.inp" line 79)
```

Your atom labels in your psf file dont match exactly the atom labels in the atom labels in your cphConfigFile and/or topology .rtf file.
