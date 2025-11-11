import os
import sys
from dotenv import load_dotenv
from google import genai

load_dotenv()
my_api_key = os.environ.get("GEMINI_API_KEY")

def main():
    client = genai.Client(api_key=my_api_key)
    myContents = sys.argv
    if len(myContents) < 2:
        print("usage: uv run main.py \"<prompt>\"")
        sys.exit(1)
        
    else:
        query = client.models.generate_content(
            model="gemini-2.0-flash-001", 
            contents=myContents[1]
        )
        print(query.text)
        print(f"Prompt tokens: {query.usage_metadata.prompt_token_count}\nResponse tokens: {query.usage_metadata.candidates_token_count}")
    
        




if __name__ == "__main__":
    main()
