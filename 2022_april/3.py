topics = ['data', 'science',  'artificial', 'intelligence']
difficulties = {'data':5, 'science':3, 'machine':1, 'learning':4}
result = {topic:difficulties[topic] if topic in difficulties else len(topic) for topic in topics}
print(result)