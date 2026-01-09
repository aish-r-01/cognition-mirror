import ollama
from core.probe import generate_probe
from core.evaluator import evaluate_answer

topic = input("Enter a topic you want to test understanding for: ")

question = ollama.generate(
    model="mistral",
    prompt=generate_probe(topic)
)["response"]

print("\nPROBE QUESTION:\n", question)

user_answer = input("\nYour answer: ")

evaluation = ollama.generate(
    model="mistral",
    prompt=evaluate_answer(user_answer, topic)
)["response"]

print("\nEVALUATION:\n", evaluation)
