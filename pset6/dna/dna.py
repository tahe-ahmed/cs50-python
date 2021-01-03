from sys import argv, exit
import csv

if len(argv) != 3:
    print('Usage: python dna.py data.csv sequence.txt')
    exit(1)

# load sequence to memory
with open(argv[2], 'r') as DAN_sequence_file:
    for line in DAN_sequence_file:
        DAN_sequence = line

# load people data to memory
people_data = []
with open(argv[1]) as people_data_file:

    reader = csv.DictReader(people_data_file)
    for row in reader:
        people_data.append(row)


# create a STRs dictiory to use it for counting
STRs = list(people_data[1].keys())
STRs_counts = dict()
for STR in STRs[1:]:
    STRs_counts[STR] = 0
# {'AGATC': 0, 'TTTTTTCT': 0, 'AATG': 0, 'TCTAG': 0, 'GATA': 0, 'TATC': 0, 'GAAA': 0, 'TCTG': 0}

# iterate over keys
for key in STRs_counts:

    STR_lenght = len(key)
    temp = 0
    temp_max = 0

    # iterate over the sequence
    sequence_length = len(DAN_sequence)
    for i in range(sequence_length):

        # move the iteration the temp_max to skip the segment that we already tested
        while temp > 0:
            temp -= 1
            continue

        # keep iterating through the sequence moving if the subsequence equals to the key STR_lenght and keep count how many times this key repeats consecutive
        while key == DAN_sequence[i: i + STR_lenght]:
            temp += 1
            i += STR_lenght

        # if current repeatation greater than the previous update the temp_max value
        if temp > temp_max:
            temp_max = temp

    # set the count of the current STR to temp_max
    STRs_counts[key] = temp_max


for person in people_data:
    correct_link = 0
    for STR in STRs_counts:
        if (int(person[STR]) == STRs_counts[STR]):
            correct_link += 1

    if correct_link == len(STRs_counts):
        print(person['name'])
        exit(0)

print('No match')
exit(0)
