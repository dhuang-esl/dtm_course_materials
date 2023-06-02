# %%
import pandas as pd
import subprocess
import matplotlib.pyplot as plt
#%%
# load the power_col.mat file into a pandas dataframe
with open('data/freq_level9.csv', 'r') as f:
    content=f.readlines()
with open('flp_demo.flp', 'w') as f:
    for i in range(4):
        block_name='core'+str(i)
        f.write("{0} :\n  position  {1},   {2} ;\n  dimension  {3},   {4} ;\n  power values  {5} ;\n\n".format(block_name, 1000*(i%2), 1000*int(i/2), 1000, 1000, content[0][0:-1]))
#%%
# %%
run_output = subprocess.run(["../../WiPLASH/3d-ice/bin/3D-ICE-Emulator", "stk_demo.stk"], stdout=subprocess.DEVNULL)
df = pd.read_csv('CPU_DIE_flp.txt', sep='\s\t\s', header=1, engine='python')
fig, ax = plt.subplots()
df.plot(x='% Time(s)', y='core0(K)',ax=ax)
df.plot(x='% Time(s)', y='core1(K)',ax=ax)
df.plot(x='% Time(s)', y='core2(K)',ax=ax)
df.plot(x='% Time(s)', y='core3(K)',ax=ax)
ax.legend(["Core0", "Core1", "Core2", "Core3"])
ax.set_xlabel("Time (s)")
ax.set_ylabel("Temperature (K)")

# %%
# load the power_col.mat file into a pandas dataframe
with open('data/freq_level7.csv', 'r') as f:
    content=f.readlines()
with open('flp_demo.flp', 'w') as f:
    for i in range(4):
        block_name='core'+str(i)
        f.write("{0} :\n  position  {1},   {2} ;\n  dimension  {3},   {4} ;\n  power values  {5} ;\n\n".format(block_name, 1000*(i%2), 1000*int(i/2), 1000, 1000, content[0][0:-1]))

# %%
