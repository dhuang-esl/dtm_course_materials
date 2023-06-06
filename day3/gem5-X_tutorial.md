# gem5-X tutorial

## Setting up and building gem5-X
The gem5-X is already configured and built in the VM. If you want to build it from scratch, you can follow the instructions in the [gem5-X repository](https://github.com/gem5-X/gem5-X)
## Running your first gem5-X simulation

The gem5-X enviromnet is created and configured with the provide docker image and container, and the container is alredy built in the VM, called gem5x-container.
But if want to create the docker container from scratch, you can use the follow command to create the container and share the local files between the docker container and the host.

```
docker run --name gem5x-container -it -v /home/student/Documents/gem5-X:/app gem5x
```

Run the follow commnad to start the gem5x container
```
docker start gem5x-container
```

and attach to the container with the follow command
```
docker exec -it gem5x-container bash
```

Now you are inside the container, and you can run the gem5-X simulation with the follow command
```
cd app/scripts/
bash ex1_runGem5-X.sh
```

Now open another terminal and run the follow command to connect to the gem5-X terminal
``` 
docker exec -it gem5x-container bash
./app/gem5-X/util/term/m5term 127.0.0.1 3456
```
You can see the ubuntu is booting. However, this can take 10 to 20 minutes to complete. We will skip this process by using the checkpointing feature of gem5-X.


## Using gem5-X’s checkpointing feature

A checkpoint in gem5-X captures the entire state of the simulated system at a specific point in time, including the register values, memory contents, cache state, and microarchitectural details. It allows users to save the state of a running simulation and later restore it to continue execution from the exact same point. This is particularly useful for debugging, performance analysis, and experimentation purposes.

```
<!-- Stop the previous simulation first, then -->
bash ex2_runGem5-X-checkpoint.sh
<!-- connect to the m5term  -->
```

Now you can see the ubuntu is already booted. It is a full function ubuntu thanks to the full systm simulation with gem5-X. For example, you can run "ls" and the "hello world" program in the terminal.

To save your own checkpoint, you can use the following command. 
```
m5 checkpoint
```

## Profiling the target application

We have already put a simple application (sum_bench) in the gem5-X environment, and you can run the follow command to run and profile the application
```
m5 resetstats; ./sum_bench 2000000; m5 dumpstats
```

It may take 1 or 2 minites based on your machine. Now, let's check the output results in stat.txt

## Modifying the hardware configuration
Checkpoint is very useful when you only want to change the configurations of the hardware. For instance, let's change the frequency of the CPU. 

```
<!-- Stop the previous simulation first, then -->
bash ex3_runGem5-X-checkpoint.sh
<!-- connect to the m5term  -->
```
Exercises:
1. Change the frequency of the CPU from 1.0 to 2.0 GHz, with a step of 0.2 GHz.
2. Fix the CPU frequency at 1.0GHz, change the cache size to investigate the possible performance effect.

## Modify the image with chroot

It's also possible to run your own benchmark in the gem5-X environment. You need to first put the target application and benchmakr inside the ubuntu image first. You can use the chroot command to do that.

```
<!-- Inside the VM, not the docker container -->
cd /home/student/Documents/gem5-X/gem5-X/full_system_images/disks
sudo mount -o loop,offset=$((2048*512)) gem5_ubuntu16.img local_mnt
sudo mount -o bind /proc local_mnt/proc
sudo mount -o bind /dev local_mnt/dev
sudo mount -o bind /dev/pts local_mnt/dev/pts
sudo mount -o bind /sys local_mnt/sys

cd local_mnt/
sudo chroot ./ 
```
Once it is finished, exit and umount the image
```
exit or ctrl+d

cd ..
sudo umount local_mnt/proc
sudo umount local_mnt/dev/pts
sudo umount local_mnt/dev
sudo umount local_mnt/sys
sudo umount local_mnt

```

Note that you need to boot the image with gem5-X from scratch (without using checkpoint) when you change the image.