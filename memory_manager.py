from mem0 import MemoryClient

# Initialize Mem0 client with your API key
client = MemoryClient(api_key="m0-O6LqN2yPyJg2JLkfEhEaSl0eoCaYg4WwG6nRaRjH")

# Add memory for a user
def add_memory(user_id, text):
    return client.add(messages=[{"role": "user", "content": text}], user_id=user_id)

# Retrieve memories for a user (mem0 v2 requires a non-empty query)
def get_memories(user_id):
    return client.search(
        query="memory",
        version="v2",
        filters={
            "OR": [
                {
                    "user_id": user_id
                }
            ]
        }
    )
