from hr_assistant.pipeline import build_hr_assistant, ask

def main():
    agent = build_hr_assistant()
    while True:
        question = input("Ask a question (or type 'exit' to quit): ")
        if question.lower() == 'exit':
            break
        response = ask(agent, question)
        print("Response:", response)

if __name__ == "__main__":
    main()