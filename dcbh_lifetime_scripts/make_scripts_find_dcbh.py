import os


submit_str = "#!/bin/bash\n\n"

for x in range(100):

    sbatch_file = open("sbatch_scripts/knl.mpi.slurm_base_find_dcbh", "r")
    replacement = ""

    for line in sbatch_file:
        line = line.strip()
        changes = line.replace("myjob.o%j", "myjob.o"+str(x))
        changes = changes.replace("myjob.e%j", "myjob.e"+str(x))
        changes = changes.replace("trees", "trees"+str(x))
        changes = changes.replace("out_file.out", "out_file"+str(x)+".out")
        replacement = replacement + changes + "\n"

    sbatch_file.close()

    fout = open("sbatch_scripts/knl.mpi.slurm"+str(x), "w")
    fout.write(replacement)
    fout.close()
    submit_str += "sbatch sbatch_scripts/knl.mpi.slurm"+str(x)+"\n\n"


sbatch_submit = open("submit_jobs.sh", "w")
sbatch_submit.write(submit_str)
sbatch_submit.close()
