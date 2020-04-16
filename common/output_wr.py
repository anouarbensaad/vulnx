
import os
import sys


def writelogs(data, data_name, output_dir):
    """Write the results."""
    for data, data_name in zip(data, data_name):
        if data:
            filepath = output_dir + '/' + data_name + '.txt'
            with open(filepath, 'w+') as out_file:
                joined = '\n'.join(data)
                out_file.write(str(joined.encode('utf-8').decode('utf-8')))
                out_file.write('\n')
