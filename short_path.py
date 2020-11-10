import priority_queue
def short_path(graph, start, end):
    queue =  priority_queue.PriorityQueue(lambda x, y: x['distance'] < y['distance'])
    queue.enqueue({"name": start, "distance": 0, 'index': 0, 'path': ['A']})
    seen = {}
    while len(queue):
        value = queue.dequeue()
        seen[value['name']] = True
        if value['name'] == end:
            value.pop('name')
            return value
        for node in graph[value['name']]:
            if node in seen:
                continue
            queue.enqueue({'name': node, 'distance': value['distance'] + graph[value['name']][node], 'path': value['path'] + [node]})
    return None