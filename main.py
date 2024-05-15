#!/usr/bin/env python3

"""
This module simulates an application that after receiving a SIGTERM or SIGINT takes a few seconds
to successfully exit.
"""

import os
import signal
import time
import sys


SECONDS_TO_WAIT_BEFORE_EXITING = 2
WATCHING_SIGNALS = [
    signal.SIGTERM,  # Termination request (can be caught or ignored)
    signal.SIGINT,  # Interrupt from keyboard (Ctrl+C)
    signal.SIGQUIT,  # Quit signal (Ctrl+\)
]


own_process_id = os.getpid()

print(f"Started main.py (PID: {own_process_id})")


def handle_exit_signal(signum, frame):
    signal_name = WATCHING_SIGNALS[WATCHING_SIGNALS.index(signum)].name

    print(
        (
            "\nReceived signal {signal_name} ({signum}), "
            "exiting gracefully in {wait_time} seconds..."
        ).format(
            signal_name=signal_name,
            signum=signum,
            wait_time=SECONDS_TO_WAIT_BEFORE_EXITING,
        )
    )

    time.sleep(SECONDS_TO_WAIT_BEFORE_EXITING)

    sys.exit(0)


for signum in WATCHING_SIGNALS:
    signal.signal(signum, handle_exit_signal)

print("Going to sleep. Waiting for kill signals.")

while True:
    time.sleep(100000)
