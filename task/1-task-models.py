from app.main import run_single_question

# HINT: All available models you can find here: https://ai-proxy.lab.epam.com/openai/models

# TODO:
#  Try different models (`deployment_name`) with such user request:
#  User massage: What LLMs can do?

# Models to try:
models = [
    'gpt-4o',
    'claude-3-7-sonnet@20250219',
    'gemini-2.5-pro'
]

# Ask the user for a question
question = input("Ask your question: ").strip()

if not question:
    question = "What LLMs can do?"  # Default question

# Test each model with the same question
for model in models:
    print(f"\n{'='*60}")
    print(f"Testing model: {model}")
    print('='*60)
    response = run_single_question(
        question=question,
        deployment_name=model,
        print_request=False, # Switch to False if you do not want to see the request in console
        print_only_content=True, # Switch to True if you want to see only content from response
    )
    print(f"Response:\n{response}\n")

# The main goal of this task is to explore the functional capabilities of DIAL to be able to work with different
# LLMs through unified API