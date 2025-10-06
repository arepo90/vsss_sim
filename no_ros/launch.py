import subprocess
import time

scripts = [
    "sim.py",
    "vision.py",
    "strat.py"
]
processes = []
print("Starting all processes...")
try:
    for script in scripts:
        proc = subprocess.Popen(["python3", script])
        processes.append(proc)
        print(f"Launched {script} with PID: {proc.pid}")
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nShutting down all processes...")
finally:
    for proc in processes:
        proc.terminate()
    for proc in processes:
        proc.wait()
    print("All processes have been terminated.")