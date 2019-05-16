"""
This file is used to test your model.

CHANGES TO THIS FILE ARE NOT SUBMITTED.
"""

import time, subprocess, sys, multiprocessing, os

# Change these paths to point to your local machine
cwd = os.getcwd()
RESULT_LOCATION = os.path.join(cwd, 'result.txt')
DATASET_LOCATION = os.path.join(cwd, 'data.csv')
SCORE_LOCATION = os.path.join(cwd, 'score.txt')
INCLUDE_Y_VALUE = False
argc = len(sys.argv)

def log_pipe(pipe):
    for line in iter(pipe.stderr.readline, b''):
        print(line.decode('utf-8'))

def follow(the_process):
    while(True):
        line = the_process.stdout.readline()
        yield line

if not os.path.isfile(RESULT_LOCATION):
    with open(RESULT_LOCATION, 'a'):
        os.utime(RESULT_LOCATION, None)
if not os.path.isfile(SCORE_LOCATION):
    with open(SCORE_LOCATION, 'a'):
        os.utime(SCORE_LOCATION, None)
if not os.path.isfile(DATASET_LOCATION):
    print(f"Cannot find dataset at {DATASET_LOCATION}, please move dataset \
            here or specify dataset path")

p = subprocess.Popen(["python3", "python/submission.py"], stdin=subprocess.PIPE,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE) \
    if not(argc > 1 and sys.argv[1] == "r") else \
    subprocess.Popen(["r", "-f", "r/submission.r", "--slave"],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE)

stderr_logger_thread = multiprocessing.Process(target=log_pipe, args=(p,))
stderr_logger_thread.start()

output = follow(p)

with open(DATASET_LOCATION) as data_file, open(RESULT_LOCATION, 'w') as result_file:
    # Skip header
    header = data_file.readline()

    while(True):
        data_row = data_file.readline()
        if not data_row: # EOF
            break
            
        if not INCLUDE_Y_VALUE:
            data_row = ','.join(data_row.split(',')[:-1]) + '\n'

        p.stdin.write(str.encode(data_row))
        p.stdin.flush()
        result_file.write(output.__next__().decode("utf-8"))

stderr_logger_thread.terminate()

# Score submission
p = subprocess.run(["python3", "src/scorer.py", RESULT_LOCATION, DATASET_LOCATION, SCORE_LOCATION])

