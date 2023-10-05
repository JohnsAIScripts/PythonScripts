import multiprocessing
import time

def worker():
    while True:
        pass

def stress_cpu(percentage, duration):
    try:
        num_processes = multiprocessing.cpu_count()

        processes = []
        for _ in range(num_processes):
            process = multiprocessing.Process(target=worker)
            process.start()
            processes.append(process)

        print(f"Stressing CPU at {percentage}% utilization for {duration} seconds...")
        time.sleep(duration)

        for process in processes:
            process.terminate()
            process.join()

        print("CPU stress test completed.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    target_percentage = 90  # Adjust the desired CPU utilization percentage here
    stress_duration = 30   # Adjust the duration of the stress test in seconds here

    stress_cpu(target_percentage, stress_duration)
