import os
from dotenv import load_dotenv
from crew import crew

# Load environment variables
load_dotenv()

def main():
    # Inputs for the Crew
    inputs = {
        "draft_file": r"C:\Users\maxw2\Downloads\tjd draft 1.txt",
    }

    # Kick off the Crew
    print("Starting the blog refinement process...")
    results = crew.kickoff(inputs)
    
    # Display results
    print("\n=== Crew Output ===")
    # Inspect the CrewOutput object
    try:
        if hasattr(results, "__dict__"):
            for key, value in results.__dict__.items():
                print(f"{key}: {value}")
        else:
            print("The CrewOutput object has no accessible attributes via __dict__. Please inspect its structure manually.")
    except Exception as e:
        print(f"An error occurred while processing the results: {e}")

if __name__ == "__main__":
    main()
