#!/bin/bash

gem5_path=/app/gem5-X

${gem5_path}/build/ARM/gem5.fast \
-d ./output_ex1 \
${gem5_path}/configs/example/fs.py \
--cpu-clock=1GHz \
--kernel=vmlinux \
--machine-type=VExpress_GEM5_V1 \
--dtb-file=${gem5_path}/system/arm/dt/armv8_gem5_v1_1cpu.dtb \
-n 1 \
--disk-image=gem5_ubuntu16.img \
--caches \
--l2cache \
--l1i_size=32kB \
--l1d_size=32kB \
--l2_size=1MB \
--l2_assoc=2 \
--mem-type=DDR4_2400_4x16 \
--mem-ranks=4 \
--mem-size=1GB \
--sys-clock=1600MHz
