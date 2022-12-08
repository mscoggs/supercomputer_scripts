import os

DD_list = range(100)
old = ["DD0???"]
new = [""]

submit_str = "#!/bin/bash\n\n"

for DD in DD_list:

    py_file = open("catalogs/catalog_base.txt", "r")
    replacement = ""

    for line in py_file:
        line = line.strip()
        changes = line.replace("trees", "trees"+str(DD))
        replacement = replacement + changes + "\n"

    py_file.close()
    # opening the file in write mode
    fout = open("catalogs/catalog"+str(DD)+".txt", "w")
    fout.write(replacement)
    fout.close()


    sbatch_file = open("sbatch_scripts/knl.mpi.slurm_base_mc", "r")
    replacement = ""

    for line in sbatch_file:
        line = line.strip()
        changes = line.replace("myjob.o%j", "myjob.o"+str(DD))
        changes = changes.replace("myjob.e%j", "myjob.e"+str(DD))
        changes = changes.replace("catalog.txt", "catalog"+str(DD)+".txt")
        changes = changes.replace("out_file.out", "out_file"+str(DD)+".out")
        changes = changes.replace("seed", str(DD+1))
        replacement = replacement + changes + "\n"

    sbatch_file.close()

    fout = open("sbatch_scripts/knl.mpi.slurm"+str(DD), "w")
    fout.write(replacement)
    fout.close()
    submit_str += "sbatch sbatch_scripts/knl.mpi.slurm"+str(DD)+"\n\n"


sbatch_submit = open("submit_jobs.sh", "w")
sbatch_submit.write(submit_str)
sbatch_submit.close()
