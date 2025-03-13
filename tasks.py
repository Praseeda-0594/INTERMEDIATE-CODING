# You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label. Return the minimum number of CPU intervals required to complete all tasks.

from collections import Counter

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # Count the frequency of each task
        task_counts = Counter(tasks)

        # Sort the frequencies in descending order
        frequencies = sorted(task_counts.values(), reverse=True)

        # Maximum frequency of a task
        max_freq = frequencies[0]

        # Calculate the maximum possible idle time
        idle_time = (max_freq - 1) * n

        # Reduce idle time using remaining tasks
        for freq in frequencies[1:]:
            idle_time -= min(max_freq - 1, freq)

        # Idle time can't be negative
        idle_time = max(0, idle_time)

        # Total intervals required = tasks count + idle time
        return len(tasks) + idle_time

# Main function to take user input
if __name__ == "__main__":
    tasks = list(input("Enter tasks (e.g., AAABBBCC): ").strip())
    n = int(input("Enter cooldown interval n: ").strip())

    sol = Solution()
    result = sol.leastInterval(tasks, n)

    print("Minimum intervals required:", result)
