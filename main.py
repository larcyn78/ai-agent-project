import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
my_api_key = os.environ.get("GEMINI_API_KEY")

def main():
    argv = sys.argv[1:]
    if not argv:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)

    verbose = "--verbose" in argv
    # positional prompt is the first non-flag arg
    args = [a for a in argv if not a.startswith("--")]
    if not args:
        print("Error: missing prompt")
        sys.exit(1)
    user_prompt = args[0]

    client = genai.Client(api_key=my_api_key)
    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]
    resp = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )

    # print model output first (tests expect your normal output unchanged)
    print(resp.text)

    if verbose:
        print(f'User prompt: {user_prompt}')
        print(f'Prompt tokens: {resp.usage_metadata.prompt_token_count}')
        print(f'Response tokens: {resp.usage_metadata.candidates_token_count}')



if __name__ == "__main__":
    main()
