start-via-direct-exec:
	echo "Starting application with Makefile via direct exec"
	./main.py
	echo "This will never be executed"

start-with-exec-call:
	echo "Starting application via Makefile using 'exec' call"
	exec ./main.py
	echo "This will never be executed"

start-with-python:
	echo "Starting application via Makefile sing python arg"
	python ./main.py
	echo "This will never be executed"
