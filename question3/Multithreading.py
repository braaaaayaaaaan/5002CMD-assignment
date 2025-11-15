import threading
import time

def factorial_task(name, n, results, times, index):
    """
    Function to calculate the factorial of 'n'.
    Stores the result in 'results' list and records start/end time in 'times' list.
    """
    print(f"\nThread {name}: Starting factorial calculation for {n}!")

    # Record start time in nanoseconds
    start_time = time.time_ns()

    # Factorial computation
    result = 1
    for i in range(2, n + 1):
        result *= i

    # Record end time in nanoseconds
    end_time = time.time_ns()

    results[index] = result

    times[index] = (start_time, end_time)

    print(f"Thread {name}: Finished factorial calculation for {n}!")

if __name__ == "__main__":
    # Set the default number of rounds to 10
    rounds = 10

    # List to store numbers before performing factorial computation
    numbers = [50, 100, 200]

    """
    Name each thread accordingly
    A - handles 50!
    B - handles 100!
    C - handles 200!
    """
    thread_names = ["A", "B", "C"]

    # Store the total time it takes for each round (1-10)
    round_times = []


    for R in range(rounds):
        # Display the header for each round
        print("*" * 50)
        print(f"Round {R + 1}".center(48))
        print("*" * 50)

        threads = []
        results = [None] * 3
        times = [None] * 3

        print("\nMain thread: Creating and starting threads.")

        # Thread creation using threading library
        for i in range(3):
            """
            Assign each thread to its respective integer for computation
            Target the factorial_task() function
            """

            # Create the thread
            t = threading.Thread(target=factorial_task, args=(thread_names[i], numbers[i], results, times, i))

            # Append the threads to an array
            threads.append(t)

            # When called, each thread begins running concurrently
            t.start()

        print("\nMain thread: Doing other work while threads run...")

        """
        Wait for all threads to finish
        Enforces that the main thread waits for all worker threads
        """
        for t in threads:
            t.join()

        """
        Computes elapsed time across concurrent threads
        """
        earliest_start = min(t[0] for t in times)
        latest_end = max(t[1] for t in times)

        # Evaluate the total time taken
        total_time = latest_end - earliest_start

        # Append the total_time to an array
        round_times.append(total_time)

        print(f"\nMain thread: All threads finished for round {R + 1}.")
        print(f"Total Time Elapsed for this round: {total_time} ns\n")

    # Evaluate the average time (Divide by 10)
    average_time = sum(round_times) // rounds

    # Display the summary header at the end of program
    print("*" * 50)
    print(f"Summary".center(48))
    print("*" * 50)

    # Display the average time elapsed over 10 rounds
    for idx, t in enumerate(round_times):
        print(f"Round {idx + 1}: {t} ns")
    print(f"\nAverage Time Elapsed Over {rounds} rounds: {average_time} ns")

    print("*" * 50)