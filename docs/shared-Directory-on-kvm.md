# Set up a Shared Directory on Host

## Launch Virtual Manager Application 
 - select the guest os then click on open on light bulb 
 - enable shared memory then apply 

 -  click add hardware button , select filesystem 
  -  set the driver to `virtiofs`
  - also source path to the shared folder in host machine 
  and target path to any name that can be identigied by guest os.
  the apply. 
  and start windows os
## Install Windows File System proxy 
[WinFsp(windows File system Proxy)](https://github.com/winfsp/winfsp/releases/)