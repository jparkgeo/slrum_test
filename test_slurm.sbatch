#!/bin/tcsh
#SBATCH --job-name=access
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=24
#SBATCH --mem-per-cpu=8GB
#SBATCH --time=2:00:00
#SBATCH --mail-type=end,fail
#SBATCH --mail-user=jparkgeo@khu.ac.kr
#SBATCH --output=R-%x.%j.out
#SBATCH --error=R-%x.%j.err

# 실제 작업을 실행합니다.
conda run -n ox_jp python test_slurm.py