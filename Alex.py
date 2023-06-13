import sys
from collections import defaultdict

def quality_markup(tasks, verdicts):
    pre_marked = {}
    for task in tasks:
        task_id, verdict = task.split()
        pre_marked[task_id] = int(verdict)

    worker_verdicts = defaultdict(list)
    for verdict in verdicts:
        worker_id, task_id, verdict = verdict.split()
        if task_id in pre_marked:
            worker_verdicts[worker_id].append(int(verdict) == pre_marked[task_id])

    reliable_workers = set()
    for worker_id, correctness in worker_verdicts.items():
        if sum(correctness) / len(correctness) >= 0.6:
            reliable_workers.add(worker_id)

    task_verdicts = defaultdict(list)
    for verdict in verdicts:
        worker_id, task_id, verdict = verdict.split()
        if task_id not in pre_marked and worker_id in reliable_workers:
            task_verdicts[task_id].append(int(verdict))

    output = []
    for task_id, verdicts in sorted(task_verdicts.items()):
        most_common_verdicts = [v for v in set(verdicts) if verdicts.count(v) == verdicts.count(max(set(verdicts), key=verdicts.count))]
        output.append(f"{task_id} {min(most_common_verdicts)}")
    
    return "\n".join(output)

pre_marked_tasks = []
worker_verdicts = []
for line in sys.stdin:
    line = line.strip()
    if line.startswith("T"):
        pre_marked_tasks.append(line)
    else:
        worker_verdicts.append(line)

result = quality_markup(pre_marked_tasks, worker_verdicts)

print(result)