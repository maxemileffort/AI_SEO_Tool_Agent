import os
import yaml
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from tools.file_tools import read_file, write_file
from tools.web_tools import search_web
from tools.prompt_tools import generate_image_prompt

# Load environment variables
load_dotenv()

# Function to load YAML configurations
def load_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

# Load agents and tasks
config_path = os.path.join(os.path.dirname(__file__), "config")
agents_config = load_yaml(os.path.join(config_path, "agents.yaml"))
tasks_config = load_yaml(os.path.join(config_path, "tasks.yaml"))

# Initialize Agents
agents = {
    "editor": Agent(
        role=agents_config["editor"]["role"],
        goal=agents_config["editor"]["goal"],
        backstory=agents_config["editor"]["backstory"],
        tools=[read_file, write_file]
    ),
    "researcher": Agent(
        role=agents_config["researcher"]["role"],
        goal=agents_config["researcher"]["goal"],
        backstory=agents_config["researcher"]["backstory"],
        tools=[search_web]
    ),
    "writer": Agent(
        role=agents_config["writer"]["role"],
        goal=agents_config["writer"]["goal"],
        backstory=agents_config["writer"]["backstory"],
        tools=[read_file, write_file]
    ),
    "illustrator": Agent(
        role=agents_config["illustrator"]["role"],
        goal=agents_config["illustrator"]["goal"],
        backstory=agents_config["illustrator"]["backstory"],
        tools=[generate_image_prompt, write_file]
    )
}

# Initialize Tasks
tasks = [
    Task(
        description=tasks_config["edit_draft_task"]["description"],
        expected_output=tasks_config["edit_draft_task"]["expected_output"],
        agent=agents["editor"]
    ),
    Task(
        description=tasks_config["enrich_content_task"]["description"],
        expected_output=tasks_config["enrich_content_task"]["expected_output"],
        agent=agents["researcher"]
    ),
    Task(
        description=tasks_config["rewrite_draft_task"]["description"],
        expected_output=tasks_config["rewrite_draft_task"]["expected_output"],
        agent=agents["writer"]
    ),
    Task(
        description=tasks_config["generate_prompts_task"]["description"],
        expected_output=tasks_config["generate_prompts_task"]["expected_output"],
        agent=agents["illustrator"]
    )
]

# Assemble the Crew
crew = Crew(
    agents=list(agents.values()),
    tasks=tasks,
    process=Process.sequential
)
