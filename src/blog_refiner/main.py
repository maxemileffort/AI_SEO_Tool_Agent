# import os
# from dotenv import load_dotenv
# from crew import crew

# # Load environment variables
# load_dotenv()

# def main():
#     # Inputs for the Crew
#     inputs = {
#         "draft_file": r"C:\Users\maxw2\Downloads\tjd draft 1.txt",
#     }

#     # Kick off the Crew
#     print("Starting the blog refinement process...")
#     results = crew.kickoff(inputs)
    
#     # Display results
#     print("\n=== Crew Output ===")
#     # Inspect the CrewOutput object
#     try:
#         if hasattr(results, "__dict__"):
#             for key, value in results.__dict__.items():
#                 print(f"{key}: {value}")
#         else:
#             print("The CrewOutput object has no accessible attributes via __dict__. Please inspect its structure manually.")
#     except Exception as e:
#         print(f"An error occurred while processing the results: {e}")

# if __name__ == "__main__":
#     main()

import os
import streamlit as st
from dotenv import load_dotenv
from crew import crew

# Load environment variables
load_dotenv()

def process_file(file_path):
    # Inputs for the Crew
    inputs = {
        "draft_file": file_path,
    }

    # Kick off the Crew
    st.write(f"Processing file: {file_path}...")
    results = crew.kickoff(inputs)

    # Display results
    st.write("\n=== Crew Output ===")
    try:
        if hasattr(results, "__dict__"):
            for key, value in results.__dict__.items():
                st.write(f"{key}: {value}")
        else:
            st.write("The CrewOutput object has no accessible attributes via __dict__. Please inspect its structure manually.")
    except Exception as e:
        st.write(f"An error occurred while processing the results: {e}")

st.title("Blog Refinement Process")
st.write("Upload your draft files for refinement. Only .txt files are allowed.")

# File uploader
uploaded_files = st.file_uploader(
    "Upload .txt files", type="txt", accept_multiple_files=True
)

if uploaded_files:
    for uploaded_file in uploaded_files:
        # Save the uploaded file to a temporary location
        temp_file_path = os.path.join("temp", uploaded_file.name)
        os.makedirs("temp", exist_ok=True)
        with open(temp_file_path, "wb") as temp_file:
            temp_file.write(uploaded_file.read())

        # Process the file
        process_file(temp_file_path)

