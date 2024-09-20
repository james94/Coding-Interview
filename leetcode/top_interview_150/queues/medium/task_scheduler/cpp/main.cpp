#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>

using namespace std;

// ChatGPT: https://chatgpt.com/share/66ebcdb4-5d8c-8005-b2cd-4cb246ba689c

// Time Complexity: O(m log m) where "m" is the number of unique tasks
    // - This accounts for operations of insertions and removing tasks from the priority queue

// Space Complexity: O(m) for storing the frequencies of tasks and for the queue
    // storing tasks under cooldown
int leastInterval(vector<char>& tasks, int n) {
    // Step 1: Determine frequency map of each task
    unordered_map<char, int> freq_map_tasks;
    for (char task : tasks) {
        freq_map_tasks[task]++;
    }

    // Step 2: Use priority queue (Max Heap) to store tasks by frequency
        // , allowing us to pick the most frequent task first thats not on cooldown
    priority_queue<int> max_heap;
    for (auto& task_freq : freq_map_tasks) {
        max_heap.push(task_freq.second);
    }

    // Step 3: Queue to track cooldown tasks with their "ready time", storing tasks until they can be rescheduled
    queue<pair<int, int>> cooldown_queue;
    int time = 0;

    // Step 4: Simulation of task scheduling: in each step, execute a task or insert an idle cycle if
        // no task can be scheduled
    while (!max_heap.empty() || !cooldown_queue.empty()) {
        time++; // Increment time with each interval

        if (!max_heap.empty()) {
            int current_task_freq = max_heap.top();
            max_heap.pop();

            // If more instances of the task remain, add it to the cooldown queue
            if (--current_task_freq > 0) {
                cooldown_queue.push({current_task_freq, time+n});
            }
        }

        // Check if any tasks in cooldown queue are ready to be rescheduled
        if (!cooldown_queue.empty() && cooldown_queue.front().second <= time) {
            max_heap.push(cooldown_queue.front().first);
            cooldown_queue.pop();
        }
    }

    return time;
}

int main() {
    vector<char> tasks1 = {'A', 'A', 'A', 'B', 'B', 'B'};
    int n1 = 2;

    cout << "Example 1: Least Interval: " << leastInterval(tasks1, n1) << endl;

    vector<char> tasks2 = {'A', 'C', 'A', 'B', 'D', 'B'};
    int n2 = 1;

    cout << "Example 2: Least Interval: " << leastInterval(tasks2, n2) << endl;

    vector<char> tasks3 = {'A', 'A', 'A', 'B', 'B', 'B'};
    int n3 = 3;

    cout << "Example 3: Least Interval: " << leastInterval(tasks3, n3) << endl;

    return 0;
}
