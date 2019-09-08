#!/usr/bin/env python3
#
# This Python 3 script converts a file outputted by the StillSpace app
# into data formatted for a Google Maps Heatmap.
#
# The input file must be in the same directory, named 'location-log.csv'.
# The output file will be in the same directory, named 'location-heatmap.json'.

import csv

output_filename = 'location-heatmap.json'

def print_to_output(output_file, string):
    print(string)
    output_file.write(string + '\n')

output = open(output_filename, 'w')

print_to_output(output, '[')

with open('location-log.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        # Skip empty lines
        if len(row) is 0:
            continue;

        # Truncate to 6 decimal points
        lat = round(float(row[2]), 6)
        lon = round(float(row[3]), 6)

        # Format as JSON
        print_to_output(output, '    {"lat" : ' + str(lat) + ', "lng" : ' + str(lon) + ' },')

print_to_output(output, ']')
output.close()

print()
print(output_filename)
