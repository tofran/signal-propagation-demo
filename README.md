# Docker and Makefile signal handling and propagation demo

This project is intended to demo signal handling by processes running within Docker. 
It serves to test common scenarios, like:

- When the "main process" running (application process) is not the PID `1` inside a Docker container.
  For example when it is being forked by another process.

- Showcase that the signal propagation works when running a new process via the shell, Makefile
  or even calling `python <YOUR_MODULE>`.

## Requirements

- Have `python` in path (consider using a venv).
- Build the image with `docker build --tag process-test -f Dockerfile .`

## Usage / demo

This is an interactive demo, therefore you must run the program, send a signal and check the output.

After running, one must send the appropriate signal using linux's `kill` or `Ctrl+C` / `Ctrl+\` (SIGINT, SIGTERM).
The application will listen to it and print that it is exiting gracefully.
A zero exit code is expected.

```sh
# Locally
./main.py
exec ./main.py
python ./main.py

# Locally with "start" shell scripts
./start-via-direct-exec.sh
./start-with-exec-call.sh
./start-with-python.sh

# Locally with make
make start-via-direct-exec
make start-with-exec-call
make start-with-python

# Using docker and running directly
docker run -it process-test ./main.py
docker run -it process-test sh -c "exec ./main.py"
docker run -it process-test python ./main.py

# Using docker "start" shell script
docker run -it process-test ./start-via-direct-exec.sh
docker run -it process-test ./start-with-exec-call.sh
docker run -it process-test ./start-with-python.sh

# Using docker and make
docker run -it process-test make start-via-direct-exec
docker run -it process-test make start-with-exec-call
docker run -it process-test make start-with-python
```

A sample output would be:

```
Started main.py (PID: 8)
Going to sleep. Waiting for kill signals.
^C
Received signal SIGINT (2), exiting gracefully in 2 seconds...
```

## Conclusion

After running all these one can conclude that signals are always properly propagated.

The only behaviour that might be less obvious is that when using exec and/or make, commands after
the main one will not be executed. Check for "This will never be executed" both in the Makefile
and `start-with-exec-call.sh`.

Hopefully this clears some confusion with signal handling.

It would be interesting to implement tests on top of this, in order to showcase ina documented way
the behaviour for each scenario.
