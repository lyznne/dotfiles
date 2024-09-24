# Set-Up QEMU in arch linux (Distros)

##### chech virtualization support
```bash
lscpu | grep -i Virtualization
```
- `VT-x` for intel
- `AMD-VI` for AMD

##### Ensure Kernel include KVM modules
```bash
zgrep CONFIG_KVM /proc/config.gz
```
- `y` = Yes (always installed)
-  `m` =  Loadable module

## Install Qemu, libvirt, viewers and Tools
run command (Update system before runnign the command)

```bash
sudo pacman -S qemu virt-manager virt-viewer dnsmasq vde2 bridge-utils openbsd-netcat ebtables iptables libguestfs
```
[click for more information](https://gist.github.com/tatumroaquin/c6464e1ccaef40fd098a4f31db61ab22)
### Enable the libvirt daemon
```bash
systemctl enable libvirtd.service
systemctl enable libvirtd
```
### Then Start the libvirt daemon
```bash
systemctl start libvirtd
```
#### Verify Host Virtualization

```bash
sudo virt-host-validate qemu
```
 - For any errir proceed to respective section, RE-RUN above command to check your changes.


## Make Libvirt Group For your $USER
edit `/etc/libvirt/libvirtd.conf` change the followinf lines.

```conf
unix_sock_group = "libvirt"
unix_sock_rw_perms = "0770"
```
## Then add $USER and create Group
```bash
sudo usermod -a -G libvirt $(whoami)
newgrp libvirt
```

## Validate Host Virtualization setup
```bash
sudo virt-host-validate qemu
```

### Reboot $ launch virtual manager

[ARTICLE](https://sysguides.com/install-kvm-on-linux)
## Intel CPU IOMMU Support
#### Enable IOMMU using grub
 - open GRUB config
 ```bash
 sudo vim /etc/default/grub
 ```

 - add kernel module entries
 ```bash
 # /etc/default/grub
GRUB_CMDLINE_LINUX="... intel_iommu=on iommu=pt"
```
 - then regenaret your `grub.cfg` file
 ```bash
 sudo grub-mkconfig -o /boot/grub/grub.cfg
sudo reboot
```

## Optimise Host with TuneD
- install TuneD
```bash
yay -S tuned
```

- Enable TuneD daemon
```bash
systemctl enable --now tuned.service
```
- Check active TuneD  Profile
```bash
tuned-adm active
```
- Optime profile
```bash
tuned-adm profile virtual-host
```



# Install Virtio
for ubuntu/ arch /debian

- Go to this link and choose the latest then download

```bash
https://fedorapeople.org/groups/virt/virtio-win/direct-downloads/archive-virtio/virtio-win-0.1.262-2/
```

or run command to download 
```bash
wget https://fedorapeople.org/groups/virt/virtio-win/direct-downloads/archive-virtio/virtio-win-0.1.240-1/virtio-win-0.1.240.iso
```

# Install Win 11 Image
[Installtion Video](https://www.youtube.com/watch?v=7tqKBy9r9b4)
[Article For Installation](https://sysguides.com/install-a-windows-11-virtual-machine-on-kvm)
