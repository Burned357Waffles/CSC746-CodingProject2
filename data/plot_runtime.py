"""

E. Wes Bethel, Copyright (C) 2022

October 2022

Description: This code loads a .csv file and creates a 3-variable plot

Inputs: the named file "data_MFLOPS.csv"

Outputs: displays a chart with matplotlib

Dependencies: matplotlib, pandas modules

Assumptions: developed and tested using Python version 3.8.8 on macOS 11.6

"""

import pandas as pd
import matplotlib.pyplot as plt


fname = "data_runtime.csv"
df = pd.read_csv(fname, comment="#")
print(df)

var_names = list(df.columns)

print("var names =", var_names)

# split the df into individual vars
# assumption: column order - 0=problem size, 1=blas time, 2=basic time

problem_sizes = df[var_names[0]].values.tolist()
code1_time = df[var_names[1]].values.tolist()
code2_time = df[var_names[2]].values.tolist()
code3_time = df[var_names[3]].values.tolist()
code4_time = df[var_names[4]].values.tolist()
code5_time = df[var_names[5]].values.tolist()
code6_time = df[var_names[6]].values.tolist()

plt.title("Comparison of Runtimes of each code")

xlocs = [i for i in range(len(problem_sizes))]

plt.xticks(xlocs, problem_sizes)

plt.plot(code1_time, "r-o")
plt.plot(code2_time, "y-x")
plt.plot(code3_time, "c-^")
plt.plot(code4_time, "g-.")
plt.plot(code5_time, "b-v")
plt.plot(code6_time, "m-D")

#plt.xscale("log")
#plt.yscale("log")

plt.xlabel("Problem Sizes")
plt.ylabel("Time (ms)")

varNames = [var_names[1], var_names[2], var_names[3], var_names[4], var_names[5], var_names[6]]
plt.legend(varNames, loc="best")

plt.grid(axis='both')

plt.show()

# EOF
