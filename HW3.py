# CptS 355 - Spring 2023 - Assignment 3 - Python

# Please include your name and the names of the students with whom you discussed any of the problems in this homework
# Name: Josh Abbott
# Collaborators: 

debugging = False
def debug(*s): 
     if debugging: 
          print(*s)

from functools import reduce

## problem 1(a) - aggregate_log  - 5%
def aggregate_log(data):
     log_output = {}
     for class_id, weekly_data in data.items():
          for day, study_time in weekly_data.items():
               if day not in log_output:
                    log_output[day] = 0
               log_output[day] += study_time
     return log_output


## problem 1(b) - combine_dict– 6%
def combine_dict(data1, data2):
     combined_data = {}
     for class_id, weekly_data in data1.items():
        combined_data[class_id] = weekly_data
     for class_id, weekly_data in data2.items():
            if class_id in combined_data:
                combined_data[class_id] += weekly_data 
            else:
                combined_data[class_id] = weekly_data
     return combined_data

## problem 1(c) - merge_logs– 12%
def merge_logs(log_list):
     merged_logs = {}
     for log in log_list:
          for class_id, weekly_data in log.items():
               if class_id not in merged_logs:
                    merged_logs[class_id] = {}
                    for day, study_time in weekly_data.items():
                         merged_logs[class_id][day] = study_time
               else:
                    merged_logs[class_id] = combine_dict(merged_logs[class_id], weekly_data)
     return merged_logs

## problem 2(a) - most_hours – 15%
from functools import reduce

def most_hours(log_input):
     def add_hours(list):
          return sum(hour for _, hour in list.items())
     
     return reduce(lambda x, y: x if x[1] >= y[1] else y, [(course, add_hours(hours)) for course, hours in log_input.items()])

## problem 2(b) - filter_log – 15%
def filter_log(log_input, day, hour_num):
     filtered_helper = lambda course: day in course and course[day] >= hour_num
     filtered = filter(filtered_helper, log_input.values())
     courses = reduce(lambda acc, course: acc + [key for key, value in log_input.items() if value == course], filtered, [])
     
     return courses

## problem 3 - graph_cycle – 12% 
def graph_cycle(graph, letter, visited=None, path=None):
     if visited is None:
          visited = []
     if path is None:
          path = [letter]

     visited.append(letter)

     for node, weight in [graph[letter]]:
          start = None
          if node in path:
               start = path.index(node)
          if start is not None:
               return path[start:] + [node]
          else:
               if node not in visited:
                    cycle = graph_cycle(graph, node, visited, path + [node])
                    if cycle is not None:
                         return cycle
          visited.pop()

     return None

## problem 4 - filter_iter – 15% 
class filter_iter():
     def __init__(self, it, op):
          self.it = it
          self.op = op
          self.index = 0
     def __next__(self):
          while True:
               self.index = next(self.it)
               if self.op(self.index) == True:
                    return self.index
          raise StopIteration
     def __iter__(self):
          return self

## problem 5 - merge – 10% 
def merge(it1, it2, n):
     result = []
     try:
          x1 = next(it1)
     except StopIteration:
          return result
     try:
          x2 = next(it2)
     except StopIteration:
          return result
     while len(result) < n:
          print(result)
          if x1 <= x2:
               result.append(x1)
               try:
                    x1 = next(it1)
               except StopIteration:
                    result.append(x2)
                    break
          else:
               result.append(x2)
               try:
                    x2 = next(it2)
               except StopIteration:
                    result.append(x1)
                    break
     
     return result[:n]
