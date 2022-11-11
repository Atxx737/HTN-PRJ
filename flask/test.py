import uuid

print(str(uuid.uuid4().fields[-1])[:5])