from openai import OpenAI

client = OpenAI()

# -- tool definitions --
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_time",
            "description": "Get the current date and time in a specific timezone.",
            "parameters": {
                "type": "object",
                "properties": {
                    "timezone": {"type": "string", "description": "Timezone name, e.g. America/Vancouver"}
                },
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather for a specific city",
            "parameters": {
                "type" : "object",
                "parameters" : {
                    "type": "object",
                    "properties": {
                        "city": {"type": "string", "description": "City name"},
                        "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
                    },
                },
            },
        },
    },
]

# --tool execution function (stub with canned results; a real implementation
#   must parse the JSON `arguments` and call actual APIs) ─-
def execute_tool(name, arguments):
    if name == "get_current_time":
        return '{"datetime": "2025-09-13T05:18:47", "day_of_week": "Saturday"}'
    elif name == "get_weather":
        return '{"temperature": 13.2, "unit": "celsius", "conditions": "clear", "humidity": 93}'

# --Initial message list --
messages = [
    {"role": "system", "content": "You are a helpful assistant. Use tools to get real-time information when needed."},
    {"role": "user", "content": "What is the current time in New York?"},
]

# --Agent core loop --
# Production code needs a max_iterations cap here: as discussed later in
# this chapter, Agents can get stuck repeating the same tool calls forvever 
while True:
    response = client.chat.completions.create(
        model="Qwen3-",    
    )