def evaluate_answer(answer: str, topic: str) -> str:
    return f"""
You are evaluating a human's understanding of: {topic}

Human answer:
{answer}

Score the understanding from 1 to 5 based on:
- clarity
- causal reasoning
- ability to generalize

Then explain:
- what is missing
- what is strong
- one follow-up question to probe deeper

Be honest, not polite.
"""
