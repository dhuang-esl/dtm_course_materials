# gem5-X tutorial

## Setting up and building gem5-X
```
sudo apt install  ... gcc-arm..
tar -zxvf "image.tar.gz"
export M5_PATH=~/gem5-X-master/full_system_images

<!-- compile gem5-X -->

make -C system/arm/dt
scons build/ARM/gem5.fast -j4
```
## Running your first gem5-X simulation

```
bash runGem5-X.sh
```

```
telnet localhost 3456
```

introduce the output folder of the booting process
stats.txt


## Using gem5-X’s enhanced features

### Checkpointing

```
bash runGem5-X-checkpoint.sh
telnet localhost 3456
m5 checkpoint
m5 exit
```

Checkpoint is very useful when you only want to change the configurations of the hardware

### 9P over Virtio and running benchmarks

However, if you want to change the image, you need to reboot the system from scratch. In this case, you can use 9P over Virtio to mount the host folder to the guest system.

change of kernel
--workload-automation-vio=
```
bash runGem5-X-9P.sh
```

```
sh mount.sh PATH
ls /mnt

```

## Modify the image with chroot

```
cd ../gem5-X-master/full_system_images/disks
sudo mount -o loop,offset=$((2048*512)) gem5_ubuntu16.img /mnt
ls /mnt
sudo mount -o bind /proc /mnt/proc
sudo mount -o bind /dev /mnt/dev
sudo mount -o bind /dev/pts /mnt/dev/pts
sudo mount -o bind /sys /mnt/sys

cd /mnt
sudo chroot /mnt

exit or ctrl+d

sudo umount /mnt/sys
sudo umount /mnt/dev/pts
sudo umount /mnt/dev
sudo umount /mnt/proc
cd
sudo umount /mnt
```