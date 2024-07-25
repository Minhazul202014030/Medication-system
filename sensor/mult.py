import subprocess
import time

script_paths = ['ir(1).py', 'ir2.py']

processes = []

try:
    while True:
        for script_path in script_paths:
            process = subprocess.Popen(['python', script_path])
            processes.append(process)

        # Run scripts for a specified time (e.g., 60 seconds)
        time.sleep(60)

        # Terminate all processes
        for process in processes:
            process.terminate()

        # Clear the list for the next iteration
        processes.clear()

except KeyboardInterrupt:
    # Handle keyboard interrupt to gracefully terminate all processes
    for process in processes:
        process.terminate()
