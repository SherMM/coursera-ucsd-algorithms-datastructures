# python3
from collections import deque

class Request:
    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time

class Response:
    def __init__(self, dropped, start_time):
        self.dropped = dropped
        self.start_time = start_time

class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = deque()

    def Process(self, request):
        # pop all packets with finish times less
        # than new packet's arrival time
        curr_arrv = request.arrival_time
        curr_proc = request.process_time
        while self.finish_time and self.finish_time[0] <= curr_arrv:
            self.finish_time.popleft()

        # buffer is still full, drop packet
        if len(self.finish_time) == self.size:
            return Response(True, -1)

        # buffer empty, process immediately
        if len(self.finish_time) == 0:
            self.finish_time.append(curr_arrv + curr_proc)
            return Response(False, curr_arrv)
        else:
            # get last added finish time, to determine
            # new packet's finish time
            top_time = self.finish_time[-1]
            finish = top_time + curr_proc
            self.finish_time.append(finish)
            return Response(False, top_time)



def ReadRequests(count):
    requests = []
    for i in range(count):
        arrival_time, process_time = map(int, input().strip().split())
        requests.append(Request(arrival_time, process_time))
    return requests

def ProcessRequests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.Process(request))
    return responses

def PrintResponses(responses):
    for response in responses:
        print(response.start_time if not response.dropped else -1)

if __name__ == "__main__":
    size, count = map(int, input().strip().split())
    requests = ReadRequests(count)

    buffer = Buffer(size)
    responses = ProcessRequests(requests, buffer)

    PrintResponses(responses)
