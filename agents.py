from crewai import Agent, LLM
import os

from dotenv import load_dotenv
load_dotenv()

from tools import tool

llm = LLM(
    api_key=os.getenv("GOOGLE_API_KEY"),
    model="gemini/gemini-1.5-flash",
    temperature=0.5,
    verbose=True
)

## Define the agents
news_researcher = Agent(role="Senoir Researcher", goal="Uncover ground breaking technologies in {topic}", verbose=True, memory=True, backstory="""
Driven by curiosity, you are the forefront of innovation,
eager to explore and share khowledge that could change the world.
""", 
llm=llm,
tools=[tool],
allow_delegation=True)

## creating a writer agent with custom tools responsible in writing news blogs
news_writer = Agent(
role="Senoir Writer", goal="Narrate compelling tech stories about {topic}", verbose=True, memory=True, backstory="""
With a flair for simplifying complex ideas, you creft,
enagaging narratives that capativate and educate, bringing new
discoveries to light in accessible manner.
""", 
llm=llm,
tools=[tool],
allow_delegation=True
)


