def generate_probe(topic: str) -> str:
    return f"""
You are testing whether someone truly understands a concept.

Ask ONE probing question about:
{topic}

The question should:
- require explanation, not definition
- expose shallow understanding
- be answerable in text

Only output the question.
"""
