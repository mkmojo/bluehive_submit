#!/bin/bash
#SBATCH -J 12_1
#SBATCH -t 5-00:00:00
#SBATCH --mem-per-cpu=10GB
#SBATCH -n 12
#SBATCH -p standard
#SBATCH -o out_slurm_abyss_p_%j
#SBATCH -e out_slurm_abyss_p_%j
#SBATCH --mail-type fail
#SBATCH --mail-type begin
#SBATCH --mail-type end
#SBATCH --mail-user qiuqiyuan@gmail.com
$HOME/git-repo/abys_mod/release/bin/abyss-pe np=12 k=25 name=test_12_1 in='/home/qqiu2/SRR498276_1.fastq /home/qqiu2/SRR498276_2.fastq'
