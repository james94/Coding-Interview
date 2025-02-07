from collections import deque

# Perplexity AI reference: https://www.perplexity.ai/search/can-you-solve-the-following-le-DuJjSC.9R5OMPlYJeVkC_g#6

# Leetcode problem: https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/description/

class DataStream:
    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.queue = deque()

    def consec(self, num: int) -> bool:
        self.queue.append(num)

        # If the queue size exceeds k, remove the oldest element
        if len(self.queue) > self.k:
            self.queue.popleft()

        # Check if the last k integers are equal to the value
        return len(self.queue) == self.k and all(x == self.value for x in self.queue)

def main():
    #["DataStream", "consec", "consec", "consec", "consec"]
    stream_ints = [[4, 3], [4], [4], [4], [3]]

    data_stream = DataStream(stream_ints[0][0], stream_ints[0][1])

    for i in range(1, len(stream_ints)):
        print(f"passing stream_int[{i}] = {stream_ints[i]}")
        data_stream.consec(stream_ints[i])

if __name__ == "__main__":
    main()
