#!/usr/bin/env python3
'''
Compute clustering efficacy (average number of individuals infected by
user-selected individuals between from_time and to_time).
'''
from gzip import open as gopen
import argparse
parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-i', '--individuals', required=True, type=str, help="Individuals (one per line)")
parser.add_argument('-tn', '--transmissions', required=True, type=str, help="Transmission Network (FAVITES format)")
parser.add_argument('-t', '--from_time', required=True, type=float, help="From Time")
parser.add_argument('-tt', '--to_time', required=False, type=float, default=float('inf'), help="To Time")

args = parser.parse_args()
assert args.to_time > args.from_time, "To Time must be larger than From Time"
if args.individuals.endswith('.gz'):
    args.individuals = gopen(args.individuals)
else:
    args.individuals = open(args.individuals)
if args.transmissions.endswith('.gz'):
    args.transmissions = gopen(args.transmissions)
else:
    args.transmissions = open(args.transmissions)

# load FAVITES transmission network
trans = []; nodes = set(); inf_at_t = set(); avg = 0.
for line in args.transmissions:
    if isinstance(line,bytes):
        l = line.decode().strip()
    else:
        l = line.strip()
    try:
        u,v,t = l.split(); t = float(t)
    except:
        raise RuntimeError("Invalid transmission network")
    if u not in nodes:
        nodes.add(u)
    if v not in nodes:
        nodes.add(v)
    trans.append((u,v,t))
    if t < args.from_time:
        inf_at_t.add(u); inf_at_t.add(v)
    elif t <= args.to_time:
        avg += t
avg /= len(inf_at_t)
print("Global Average Number Infected: %f"%avg)

# load user's individuals
user_individuals = set()
for line in args.individuals:
    if isinstance(line,bytes):
        l = line.decode.strip()
    else:
        l = line.strip()
    assert l in nodes, "Individual not in transmission network: %s"%l
    user_individuals.add(l)

# compute average number infected
avg = 0.
for u,v,t in trans:
    if t >= args.from_time and t <= args.to_time and u in user_individuals:
        avg += 1
avg /= len(user_individuals)
print("User Average Number Infected: %f"%avg)