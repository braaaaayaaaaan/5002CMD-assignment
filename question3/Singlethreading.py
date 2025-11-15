import time

def factorial_task(name, n):
    """
    Function to calculate the factorial of 'n'.
    Returns the result and the start/end times in nanoseconds.
    """
    print(f"\nTask {name}: Starting factorial calculation for {n}!")

    # Record start time in nanoseconds
    start_time = time.time_ns()

    # Factorial computation
    result = 1
    for i in range(2, n + 1):
        result *= i

    # Record end time in nanoseconds
    end_time = time.time_ns()

    print(f"Task {name}: Finished factorial calculation for {n}!")
    return result, start_time, end_time

if __name__ == "__main__":
    # No. of testing rounds
    rounds = 10

    # Numbers to undergo factorial computation
    numbers = [50, 100, 200]

    # Name the threads accordingly (A,B, and C)
    task_names = ["A", "B", "C"]

    # Store total times for each round
    round_times = []

    for R in range(rounds):
        # Display header for each Round (1-10)
        print("*" * 50)
        print(f"Round {R + 1}".center(48))
        print("*" * 50)

        results = []
        times = []

        print("\nMain program: Starting sequential tasks.")

        earliest_start = None
        latest_end = None

        # Execute tasks sequentially
        for i in range(3):
            result, start_time, end_time = factorial_task(task_names[i], numbers[i])
            results.append(result)
            times.append((start_time, end_time))

            # Track earliest start and latest end for total time
            if earliest_start is None or start_time < earliest_start:
                earliest_start = start_time
            if latest_end is None or end_time > latest_end:
                latest_end = end_time

        # Calculate total time taken for this round
        total_time = latest_end - earliest_start
        round_times.append(total_time)

        print(f"\nMain program: All tasks finished for round {R + 1}.")
        print(f"Total Time Elapsed (ns) for this round: {total_time}\n")

    # Compute and display average time
    average_time = sum(round_times) // rounds

    # Display summary header
    print("*" * 50)
    print(f"Summary".center(48))
    print("*" * 50)

    for idx, t in enumerate(round_times):
        print(f"Round {idx + 1}: {t} ns")
    print(f"\nAverage Time Elapsed Over {rounds} rounds: {average_time} ns")

    print("*" * 50)