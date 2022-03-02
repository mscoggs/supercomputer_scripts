import os

DD_list = [6,7,8,9,10,11,12]
old = ["DD0???"]
new = [""]

submit_str = "#!/bin/bash\n\n"

for DD in DD_list:

    py_file = open("collision_scripts/make_plots_base.py", "r")
    replacement = ""

    if(DD < 10): sub = "0"+str(DD)+"?"
    else: sub = str(DD) +"?"

    for line in py_file:
        line = line.strip()
        changes = line.replace("DD0???", "DD0"+sub)
        replacement = replacement + changes + "\n"

    py_file.close()
    # opening the file in write mode
    fout = open("collision_scripts/make_plots"+str(DD)+".py", "w")
    fout.write(replacement)
    fout.close()


    sbatch_file = open("sbatch_scripts/knl.mpi.slurm_base", "r")
    replacement = ""

    for line in sbatch_file:
        line = line.strip()
        changes = line.replace("myjob.o%j", "myjob.o"+str(DD))
        changes = line.replace("myjob.e%j", "myjob.e"+str(DD))
        changes = line.replace("make_plots.py", "collision_scripts/make_plots"+str(DD)+".py")
        changes = line.replace("out_file.out", "out_files/out_file"+str(DD)+".out")
        replacement = replacement + changes + "\n"

    sbatch_file.close()

    fout = open("sbatch_scripts/knl.mpi.slurm"+str(DD), "w")
    fout.write(replacement)
    fout.close()
    submit_str += "sbatch sbatch_scripts/knl.mpi.slurm"+str(DD)+"\n\n"


sbatch_submit = open("submit_jobs.sh", "w")
sbatch_submit.write(submit_str)
sbatch_submit.close()
