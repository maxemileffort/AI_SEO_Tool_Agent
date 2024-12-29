import os
from dotenv import load_dotenv
from crew import crew

# Load environment variables
load_dotenv()

def main():
    # Inputs for the Crew
    inputs = {
        "draft_file": "path/to/your/draft.docx",
    }

    # Kick off the Crew
    print("Starting the blog refinement process...")
    results = crew.kickoff(inputs)
    
    # Display results
    print("\n=== Crew Output ===")
    for key, value in results.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
