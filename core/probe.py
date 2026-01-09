def generate_probe(topic: str) -> str:
    return f"""
You are testing whether someone truly understands a concept.

Ask ONE probing question about:
{topic}

The question should:
- focuses on a single causal mechanism
- require explanation, not definition
- exposes shallow or memorized understanding
- be answerable in text

The question must require the person to explain WHY something happens.

Only output the question.
"""
