#include <iostream>

/**

- ChatGPT: https://chatgpt.com/share/66ed0887-da0c-8005-8ae2-fda651317219

- A circular queue is a data structure that uses a single,
fixed-size array to implement a queue. It has two pointers,
front and rear, that point to the first and last elements of the queue,
respectively. When the rear pointer reaches the end of the array, it wraps
around to the beginning, making the queue circular.

Time Complexity: O(1) for all operations (enQueue, deQueue, Front, Rear, isEmpty, isFull)
- these operations involve simple pointer manipulations or checks

Space Complexity: O(n) for the array used to store the elements in the queue
- where n is the capacity of the circular queue because we maintain a fixed-size array

RESULT:

./run_circular_queue
Circular Queue First Item In Front: 1
Circular Queue Last Item In Rear: 3
Circular Queue Is Full?: 1
Circular Queue Is Full?: 0
Circular Queue First Item In Front: 2
Circular Queue Last Item In Rear: 4
Circular Queue Is Full?: 1
*/

class CircularQueue {
public:

    // Constructor
    CircularQueue(int k) {
        // Initialize the queue with size k
        capacity = k;
        queue = new int[capacity]; // Allocate memory for the queue's array
        front = 0; // Initialize dequeue front pointer
        rear = -1; // Initialize enqueue rear pointer
        count = 0; // Initialize current number of elements in the queue
    }

    // Destructor
    ~CircularQueue() {
        delete[] queue; // Free the memory allocated for the queue's array, can't insert
    }

    // Insert an element into the circular queue
    bool enQueue(int value) {
        if (isFull()) {
            return false; // Return false if the queue is full
        }

        rear = (rear + 1) % capacity; // Increment rear pointer
        queue[rear] = value;
        count++;
        return true;
    }

    // Delete an element from the circular queue
    bool deQueue() {
        if (isEmpty()) {
            return false; // Return false if the queue is empty, can't delete
        }

        front = (front + 1) % capacity; // Increment front pointer
        count--;
        return true;
    }

    // Get the front item from the queue
    int Front() {
        if (isEmpty()) {
            return -1; // Return -1 if the queue is empty
        }

        return queue[front];
    }

    // Get the last item (rear item) from the queue
    int Rear() {
        if (isEmpty()) {
            return -1; // Return -1 if the queue is empty
        }

        return queue[rear];
    }

    // Check if the circular queue is empty
    bool isEmpty() {
        return count == 0;
    }

    // Check if the circular queue is full
    bool isFull() {
        return count == capacity;
    }
private:
    int *queue; // Array to store elements
    int front; // Front pointer for dequeue to remove elements
    int rear; // Rear pointer for enqueue to add elements
    int capacity; // Maximum size of the queue
    int count; // Current number of elements in the queue
};

int main() {
    CircularQueue circularQueue(3); // Initialize a circular queue with size 3

    circularQueue.enQueue(1); // Insert 1 into the circular queue; returns true
    circularQueue.enQueue(2); // Insert 2 into the circular queue; returns true
    circularQueue.enQueue(3); // Insert 3 into the circular queue; returns true
    circularQueue.enQueue(4); // Insert 4 into the circular queue; returns false, the queue is full
    // circularQueue.Rear(); // Get the last item from the queue; returns 3

    std::cout << "Circular Queue First Item In Front: " << circularQueue.Front() << std::endl;
    std::cout << "Circular Queue Last Item In Rear: " << circularQueue.Rear() << std::endl;
    std::cout << "Circular Queue Is Full?: " << circularQueue.isFull() << std::endl;

    // circularQueue.isFull(); // Check if the queue is full; returns true
    circularQueue.deQueue(); // Delete an element from the circular queue; returns true
    std::cout << "Circular Queue Is Full?: " << circularQueue.isFull() << std::endl;

    circularQueue.enQueue(4); // Insert 4 into the circular queue; returns true
    circularQueue.Rear(); // Get the last item from the queue; returns 4

    std::cout << "Circular Queue First Item In Front: " << circularQueue.Front() << std::endl;
    std::cout << "Circular Queue Last Item In Rear: " << circularQueue.Rear() << std::endl;
    std::cout << "Circular Queue Is Full?: " << circularQueue.isFull() << std::endl;

    return 0;
}