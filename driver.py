import time
import matplotlib.pyplot as plt
from copy import deepcopy
from pprint import pprint
from list_generators import Gen
from sorting_algorithms import Sort

# Define time & swap variables for each experiment
merge_stats = {
    # Random time and swaps arrays
    "random_time" : [],
    "random_swaps" : [],
    # Sorted time and swaps arrays
    "sorted_time" : [],
    "sorted_swaps" : [],
    # Reversed time and swaps arrays
    "reversed_time" : [],
    "reversed_swaps" : [],
    # Repetitive time and swaps arrays
    "repetitive_time" : [],
    "repetitive_swaps": [],
}
shell_stats = {
    # Random time and swaps arrays
    "random_time" : [],
    "random_swaps" : [],
    # Sorted time and swaps arrays
    "sorted_time" : [],
    "sorted_swaps" : [],
    # Reversed time and swaps arrays
    "reversed_time" : [],
    "reversed_swaps" : [],
    # Repetitive time and swaps arrays
    "repetitive_time" : [],
    "repetitive_swaps": [],
}
insertion_stats = {
    # Random time and swaps arrays
    "random_time" : [],
    "random_swaps" : [],
    # Sorted time and swaps arrays
    "sorted_time" : [],
    "sorted_swaps" : [],
    # Reversed time and swaps arrays
    "reversed_time" : [],
    "reversed_swaps" : [],
    # Repetitive time and swaps arrays
    "repetitive_time" : [],
    "repetitive_swaps": [],
}
selection_stats = {
    # Random time and swaps arrays
    "random_time" : [],
    "random_swaps" : [],
    # Sorted time and swaps arrays
    "sorted_time" : [],
    "sorted_swaps" : [],
    # Reversed time and swaps arrays
    "reversed_time" : [],
    "reversed_swaps" : [],
    # Repetitive time and swaps arrays
    "repetitive_time" : [],
    "repetitive_swaps": [],
}

def calculate_swaps_and_time():

    # Function to write results of experiments in dictionaries
    def time_for_sort(sort_function, sort_stats, i, j, array, experiments, array_type):
        a = deepcopy(array)
        start = time.time()
        swaps = sort_function(a)
        worktime = time.time() - start
        if j == 0:
            sort_stats[f"{array_type}_time"].append(worktime/experiments)
            sort_stats[f"{array_type}_swaps"].append(int(round(swaps/experiments, 0)))
        else:
            sort_stats[f"{array_type}_time"][i] += worktime/experiments
            sort_stats[f"{array_type}_swaps"][i] += int(round(swaps/experiments, 0))

    # Function to run experiments according to the task requirements
    def stats_for_array(experiments, array_type, array_function):
        # Random array from 2**7 to 2**15
        for i in range(9):
            for j in range(experiments):

                # Create an array from a function that was passed
                array = array_function(2**(i+7))

                # Merge
                time_for_sort(Sort.merge, merge_stats, i, j, array, experiments, array_type)
                # Shell
                time_for_sort(Sort.shell, shell_stats, i, j, array, experiments, array_type)
                # Insertion
                time_for_sort(Sort.insertion, insertion_stats, i, j, array, experiments, array_type)
                # Selection
                time_for_sort(Sort.selection, selection_stats, i, j, array, experiments, array_type)

    # # 5 experiments of random_array
    stats_for_array(5, "random", Gen.random_array)

    # # 1 experiment of sorted_array
    stats_for_array(1, "sorted", Gen.sorted_array)

    # # 1 experiment of reversed_array
    stats_for_array(1, "reversed", Gen.reversed_array)

    # 3 experiments of repetitive array
    stats_for_array(3, "repetitive", Gen.repetitive_array)

    # Print out the results
    print("\nMERGE "+"-"*30)
    pprint(merge_stats)
    print("\nSHELL "+"-"*30)
    pprint(shell_stats)
    print("\nINSERTION "+"-"*30)
    pprint(insertion_stats)
    print("\nSELECTION "+"-"*30)
    pprint(selection_stats)

# Generate log scale plot using matplotlib
def show_chart(array_type, data_type):
    tests = ["2^7", "2^8", "2^9", "2^10", "2^11", "2^12", "2^13", "2^14", "2^15"]
    _, ax = plt.subplots()
    ax.plot(tests, merge_stats[f"{array_type}_{data_type}"], label='Merge')
    ax.plot(tests, shell_stats[f"{array_type}_{data_type}"], label='Shell')
    ax.plot(tests, insertion_stats[f"{array_type}_{data_type}"], label='Insertion')
    ax.plot(tests, selection_stats[f"{array_type}_{data_type}"], label='Selection')

    if data_type == "swaps":
        data = "Comparisons"
    else:
        data = "Time"
    ax.set(ylabel='Time', xlabel="Size", title=f"Data: {array_type.capitalize()} array, Measure: {data}")
    ax.set_yscale("log")
    ax.legend()
    ax.grid()
    plt.show()

if __name__ == "__main__":
    # Gather all data to build graphs
    calculate_swaps_and_time()

    # Random
    show_chart("random", "time")
    show_chart("random", "swaps")

    # Sorted
    show_chart("sorted", "time")
    show_chart("sorted", "swaps")

    # Reversed
    show_chart("reversed", "time")
    show_chart("reversed", "swaps")

    # Repetitive
    show_chart("repetitive", "time")
    show_chart("repetitive", "swaps")