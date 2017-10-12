#! /usr/bin/env python3
'''
Niema Moshiri 2017

Align each given sequence against a given profile HMM.
'''
from common import readFASTQ
from os.path import isfile
from subprocess import CalledProcessError,check_output
import argparse
INFORMATS = {'FASTA', 'FASTQ', 'EMBL', 'GENBANK', 'UNIPROT'}
OUTFORMATS = {'STOCKHOLM', 'PFAM', 'A2M', 'PSIBLAST'}

# parse user args
parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-H', '--HMM', required=True, type=str, help="Profile HMM")
parser.add_argument('-s', '--seq', required=True, type=str, help="Sequences")
parser.add_argument('-if', '--informat', required=False, type=str, default='FASTA', help="Input Sequence Format")
parser.add_argument('-of', '--outformat', required=False, type=str, default='STOCKHOLM', help="Output Sequence Format")
parser.add_argument('-a', '--hmmalign', required=False, type=str, default='hmmalign', help="Path to hmmalign")
args = parser.parse_args()
assert isfile(args.HMM), "ERROR: Invalid file: %s" % args.HMM
assert isfile(args.seq), "ERROR: Invalid file: %s" % args.seq
args.informat = args.informat.strip().upper()
assert len(args.informat) == 0 or args.informat in INFORMATS, "ERROR: Invalid input format: %s (Choices: %s)" % (args.informat, ', '.join(sorted(INFORMATS)))
args.outformat = args.outformat.strip().upper()
assert len(args.outformat) == 0 or args.outformat in OUTFORMATS, "ERROR: Invalid output format: %s (Choices: %s)" % (args.outformat, ', '.join(sorted(OUTFORMATS)))

# if user specified FASTQ, convert to FASTA
if args.informat == 'FASTQ':
    from tempfile import NamedTemporaryFile
    seqs = readFASTQ(open(args.seq))
    tmp = NamedTemporaryFile(mode='w')
    tmp.write('\n'.join([">%s\n%s" % (ID,seqs[ID][0]) for ID in seqs]))
    tmp.flush()
    args.seq = tmp.name
    args.informat = 'FASTA'

# perform alignment
try:
    print(check_output([args.hmmalign,'--informat',args.informat,'--outformat',args.outformat,args.HMM,args.seq]).decode())
except CalledProcessError as e:
    print(e.output.decode())
