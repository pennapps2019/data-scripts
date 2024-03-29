#!/usr/bin/env python3
#
# This Python 3 script converts a file outputted by the StillSpace app
# into data formatted for a Google Maps Heatmap.
#
# The input file must be in the same directory, named 'location_log.csv'.
# The output file will be in the same directory, named 'location_heatmap.json'.

import csv

filtered = True  # Filters out spots with less than a specific value
filter_less_than = 3
output_filename = 'location_heatmap.json'

def print_to_output(output_file, string):
    print(string, end='')
    output_file.write(string)

output = open(output_filename, 'w')
print_to_output(output, '[')

with open('location_log.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    first_row = True;
    for row in csv_reader:
        # Skip empty lines
        if len(row) is 0:
            continue;

        count = int(row[1])
        if filtered and count < filter_less_than:
            continue;

        # Truncate to 6 decimal points
        lat = round(float(row[2]), 6)
        lon = round(float(row[3]), 6)

        # Format as JSON
        if first_row:
            first_row = False
        else:
            print_to_output(output, ' ,')

        print_to_output(output, '\n{"lat" : ' + str(lat) + ', "lng" : ' + str(lon) + ' }')

print_to_output(output, '\n]')
output.close()

print()
print(output_filename)

'''
'''
