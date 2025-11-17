from memory_manager import add_memory, get_memories
from calendar_manager import get_todays_meetings, get_week_meetings

def chatbot(user_id, message):

    msg = message.lower()

    # --- MEMORY ---
    if "remember that" in msg:
        info = message.replace("remember that", "").strip()
        add_memory(user_id, info)
        return f"I will remember that: {info}"

    if "what do you remember" in msg:
        memories = get_memories(user_id)
        results = memories.get("results", [])

        if not results:
            return "I don't have any memories yet."

        # SAFE extraction of text from mem0 results
        def extract_text(item):
            if "content" in item:
                return item["content"]
            if "text" in item:
                return item["text"]
            if "memory" in item:
                return item["memory"]
            return str(item)

        return "\n".join([extract_text(item) for item in results])

    # --- CALENDAR ---
    if "today" in msg and "meeting" in msg:
        events = get_todays_meetings()
        return "\n".join([f"{e['title']} at {e['time']}" for e in events])

    if "this week" in msg or "week meetings" in msg:
        events = get_week_meetings()
        return "\n".join([e["title"] for e in events])

    return "I can remember things or show your meetings! Try: 'What are my meetings today?'"
