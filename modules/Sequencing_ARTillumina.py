#! /usr/bin/env python3
'''
Niema Moshiri 2016

"Sequencing" module, using ART to simulate NGS reads
'''
from Sequencing import Sequencing
import FAVITES_GlobalContext as GC
from subprocess import call
from os.path import expanduser
from os import getcwd
from os import makedirs
from os import chdir

class Sequencing_ARTillumina(Sequencing):
    def init():
        GC.out_dir = expanduser(GC.out_dir)
        GC.art_illumina_args = [i.strip() for i in GC.art_illumina_args.strip().split()]
        assert "-i" not in GC.art_illumina_args and "--in" not in GC.art_illumina_args, "Don't use the -i (--in) argument (we will specify it for you)"
        assert "-o" not in GC.art_illumina_args and "--out" not in GC.art_illumina_args, "Don't use the -o (--out) argument (we will specify it for you)"
        GC.art_illumina_path = expanduser(GC.art_illumina_path.strip())

    def introduce_sequencing_error(node):
        command = [GC.art_illumina_path] + GC.art_illumina_args
        command.append("-i")
        command.append(GC.out_dir + "/error_free_files/sequence_data/seqs_" + node.get_name() + ".fasta")
        command.append("-o")
        command.append(node.get_name())
        orig_dir = getcwd()
        chdir(GC.out_dir)
        makedirs("error_prone_files/sequence_data", exist_ok=True)
        chdir("error_prone_files/sequence_data")
        call(command, stdout=open("log_" + node.get_name() + ".txt", 'w'))
        chdir(orig_dir)