import gzip
import shutil
from pathlib import Path

input_dir = Path("fastq")
output_dir = Path("fastq_gzipped")

output_dir.mkdir(parents=True, exist_ok=True)

for file_path in input_dir.glob("*.fastq"):
    if file_path.is_file():
        gz_path = output_dir / f"{file_path.name}.gz"

        with open(file_path, "rb") as f_in:
            with gzip.open(gz_path, "wb") as f_out:
                shutil.copyfileobj(f_in, f_out)

        print(f"Compressed: {file_path} -> {gz_path}")
