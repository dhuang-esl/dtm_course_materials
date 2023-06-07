# %%
import pandas as pd
power_model = pd.read_csv('day3/power_model.csv', sep=',', header=0)

#%%
def parse_stat_file(filename):
    data = {}
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('-') or not line:
                continue
            key, value = line.split('#')[0].split()[0:2]
            try:
                value = int(value)
            except ValueError:
                value = float(value)
            data[key] = value
    return data

# Usage example
filename = 'day3/stats.txt'  # Replace with the actual filename
parsed_data = parse_stat_file(filename)

#%%
freq_run=1005
llc_size=1

power_loc=power_model.loc[power_model['Freq'] == freq_run].index[0]

num_cycles=parsed_data['system.cpu.numCycles']
idle_cycles=parsed_data['system.cpu.num_idle_cycles']
energy_active=(num_cycles-idle_cycles)*power_model['CoreActive'][power_loc]*10e-12
energy_idle=idle_cycles*power_model['CoreIdle'][power_loc]*10e-12
energy_static=num_cycles*power_model['CoreStatic'][power_loc]*10e-12
llc_read = parsed_data['system.l2.ReadReq_hits::total']+ parsed_data['system.l2.ReadExReq_hits::total']+ parsed_data['system.l2.ReadCleanReq_hits::total']+ parsed_data['system.l2.ReadSharedReq_hits::total']
energy_llc_read=llc_read*power_model['LLCRead'][power_loc]*10e-12
llc_write = parsed_data['system.l2.WritebackDirty_hits::total']+ parsed_data['system.l2.WritebackClean_hits::total']+ parsed_data['system.l2.WriteClean_hits::total']
energy_llc_write=llc_write*power_model['LLCWrite'][power_loc]*10e-12
energy_llc_leak=num_cycles*llc_size*power_model['LLCStatic'][power_loc]*10e-12
# %%

# %%
