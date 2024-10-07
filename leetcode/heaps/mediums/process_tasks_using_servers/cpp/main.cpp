#include <iostream>
#include <vector>
#include <queue>
#include <tuple>

using namespace std;

/*
**Leetcode Heap (Priority Queue) Questions**:

- https://leetcode.com/problem-list/heap-priority-queue/

**Leetcode Problem:**

- https://leetcode.com/problems/process-tasks-using-servers/description/?envType=problem-list-v2&envId=heap-priority-queue

**ChatGPT Solution:**

- https://chatgpt.com/share/6702f1c2-4cbc-8005-9d09-0e0548ce8028
*/

/**
Problem Breakdown and Approach:

- To solve the "Process Tasks Using Servers" problem,
the task involves scheduling jobs (tasks) on servers.
We choose servers based on 2 criteria:

    1. "Smallest weight" of the server
    2. "Smallest index" in case of a tie

We also account for servers taking a certain amount of
time to complete each task, and only after that time will
they be available for new tasks.

Software Design Perspective:

1. Heap (Priority Queue): A "min-heap" is used to manage
available servers based on their weight and index.
    - "Primary Key": server weight
    - "Secondary Key": server index (to break ties)

2. Heap to Manage Busy Servers: When a server is busy, we
need to track when it will be free. We'll use another
min-heap to keep track of buys servers by storing the server's
free time.

3. Two Priority Queues:
    - Available Servers: Min-heap that holds servers ordered by their weight and index
    - Busy Servers: Min-heap that holds servers ordered by when they'll become free

Time Complexity:

- Heap Insert/Extract: Each task may be processed by pushing/popping from a heap (O(log n))
- Overall Complexity: O(m log n) where "m" is the number of tasks and "n" is the number of servers

Space Complexity:

- O(n + m) for storing server and task information in the heaps

*/

vector<int> assignTasks(vector<int>& servers, vector<int>& tasks) {
    int n = servers.size();
    int m = tasks.size();

    // Heap (Priority Queues)
    // Free Available Servers: sorted by (weight, index)
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> freeServers;

    // Busy Servers: sorted by (release time, weight, index)
    priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> busyServers;

    vector<int> ans(m);

    // Add all servers to free server heap
    for (int i = 0; i < n; i++) {
        freeServers.emplace(servers[i], i);
    }

    int currentTime = 0;

    for (int i = 0; i < m; i++) {
        // Current time advances to at least task index
        currentTime = max(currentTime, i);

        // Move servers from busy to free as they become available
        while (!busyServers.empty() && get<0>(busyServers.top()) <= currentTime) {
            auto [timeFree, weight, index] = busyServers.top();
            busyServers.pop();
            freeServers.emplace(weight, index);
        }

        // If no free servers, wait for the next one to be available
        if (freeServers.empty()) {
            currentTime = get<0>(busyServers.top());
            while (!busyServers.empty() && get<0>(busyServers.top()) <= currentTime) {
                auto [timeFree, weight, index] = busyServers.top();
                busyServers.pop();
                freeServers.emplace(weight, index);
            }
        }

        // Assign the current task to the free server
        auto [serverWeight, serverIndex] = freeServers.top();
        freeServers.pop();

        // Record which server processed task i
        ans[i] = serverIndex;

        // Add this server to the busy heap, indicating when it will be free
        busyServers.emplace(currentTime + tasks[i], serverWeight, serverIndex);
    }

    return ans;
}

void displayProcessedTasksByServers(vector<int>& processedTasks) {
    for (int i = 0; i < processedTasks.size(); i++) {
        cout << processedTasks[i] << " ";
    }
    cout << endl;
}

int main() {

    // Example 1
    vector<int> servers1 = {3, 3, 2};
    vector<int> tasks1 = {1, 2, 3, 2, 1, 2}; //1,2,3,2,1,2

    vector<int> result1 = assignTasks(servers1, tasks1);

    cout << "Result for Example 1: ";
    displayProcessedTasksByServers(result1);

    // Example 2
    vector<int> servers2 = {5, 1, 4, 3, 2};
    vector<int> tasks2 = {2, 1, 2, 4, 5, 2, 1}; //1,4,1,2,3,1,0

    vector<int> result2 = assignTasks(servers2, tasks2);

    cout << "Result for Example 2: ";
    displayProcessedTasksByServers(result2);

    return 0;
}