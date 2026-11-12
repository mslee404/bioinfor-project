import subprocess

sra_numbers = (
    [f"SRR{i}" for i in range(24961559, 24961646)] +
    [f"SRR{i}" for i in range(27392853, 27392911)]
)

for sra_id in sra_numbers:
    print ("Currently downloading: " + sra_id)
    prefetch = "prefetch " + sra_id
    subprocess.call(prefetch, shell=True)
    
    print ("Generating fastq for: " + sra_id)
    fastq_dump = f"fasterq-dump {sra_id}/{sra_id}.sra --outdir fastq --split-files"
    subprocess.call(fastq_dump, shell=True)

    delete_sra = f"rmdir /s /q {sra_id} "
    subprocess.call(delete_sra, shell=True)
    print("Folder deleted")

    
    