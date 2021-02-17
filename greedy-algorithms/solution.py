from pathlib import Path
from jobs import JobDiff, JobRatio

def get_input(rel_path):
  full_path = Path(__file__).parent / rel_path
  file = open(full_path, 'r')
  return file.read().strip().split('\n')[1:]

def build_jobs(strings, JobClass):
  jobs = []
  for string in strings:
    weight, length = string.split(' ')
    jobs.append(JobClass(weight, length))
  return jobs

def weighted_completion_times(strings, JobClass):
  jobs = sorted(build_jobs(strings, JobClass), reverse=True)
  completion = 0
  total = 0
  for job in jobs:
    completion += job.length
    total += int(job.weight * completion)
  return total

strings = get_input('./input.txt')

print('Diff:', weighted_completion_times(strings, JobDiff))
print('Ratio:', weighted_completion_times(strings, JobRatio))
