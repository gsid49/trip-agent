from crewai import Agent
from textwrap import dedent
from langchain_openai import ChatOpenAI

from tools.search_tools import SearchTools
from tools.calculator_tools import CalculatorTools

"""
Creating Agents Cheat Sheet:
- Think like a boss. Work backwards from the goal and think which employee 
    you need to hire to get the job done.
- Define the Captain of the crew who orient the other agents towards the goal. 
- Define which experts the captain needs to communicate with and delegate tasks to.
    Build a top down structure of the crew.

Goal:
- Create a 7-day travel itinerary with detailed per-day plans,
    including budget, packing suggestions, and safety tips.

Captain/Manager/Boss:
- Expert Travel Agent

Employees/Experts to hire:
- City Selection Expert 
- Local Tour Guide


Notes:
- Agents should be results driven and have a clear goal in mind
- Role is their job title
- Goals should actionable
- Backstory should be their resume
"""


class TravelAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(
            model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        self.OpenAIGPT4Mini = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7)

    def city_selection_expert(self):
        return Agent(
            role="City Selection Expert",
            backstory=dedent(
                f"""You are a leading expert at picking cities within a destination country taking into account the travel parameters such as
                traveler's interests, travel month and trip duration. You have decades of experience doing this work and select cities
                that are sure to amaze the traveler."""),
            goal=dedent(
                f"""Select the best cities based on weather, season, prices, traveler interests, travel month and trip duration."""),
            tools=[SearchTools.search_internet],
            verbose=True,
            llm=self.OpenAIGPT4Mini,
        )

    def local_tour_guide(self):
        return Agent(
            role="Local Tour Guide",
            backstory=dedent(
                f"""You are a superb local guide with extensive information
                about the cities around the world, their attractions and customs"""),
            goal=dedent(
                f"""Provide the BEST insights about the selected cities"""),
            tools=[SearchTools.search_internet],
            verbose=True,
            llm=self.OpenAIGPT4Mini,
        )
    
    def travel_planner(self):
        return Agent(
            role="Travel planner agent",
            backstory=dedent(
                f"""You are a leading expert on planning travel from an origin to destination. 
                You are able to find the best mode of transportation and are able to make
                reasonable trade off decisions between the cheapest options and comfort."""),
            goal=dedent(
                f"""Provide the best travel plan that is a good balance between cheap and comfort."""),
            tools=[SearchTools.search_internet, CalculatorTools.calculate],
            verbose=True,
            llm=self.OpenAIGPT4Mini,
        )

    def compiler(self):
        return Agent(
            role="Travel plan complier",
            backstory=dedent(
                f"""You are the best trip compiler who can take information and prepare a travel plan
                that is well structured and easy to understand."""),
            goal=dedent(
                f"""Provide a travel plan that is well structured and easy to understand."""),
            tools=[SearchTools.search_internet, CalculatorTools.calculate],
            verbose=True,
            llm=self.OpenAIGPT4Mini,
        )
