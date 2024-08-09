from crewai import Crew
from textwrap import dedent
from agents import TravelAgents
from tasks import TravelTasks

from dotenv import load_dotenv
load_dotenv()


class TripCrew:
    def __init__(self, origin, destination_country, interests, travel_month, trip_duration):
        self.origin = origin
        self.destination_country = destination_country
        self.travel_month = travel_month
        self.interests = interests
        self.trip_duration = trip_duration

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = TravelAgents()
        tasks = TravelTasks()

        # Define your custom agents and tasks here
        city_selection_expert = agents.city_selection_expert()
        local_tour_guide = agents.local_tour_guide()
        travel_planner = agents.travel_planner()
        trip_compiler = agents.compiler()

        # Custom tasks include agent name and variables as input
        identify_cities = tasks.identify_cities(
            city_selection_expert,
            self.destination_country,
            self.interests,
            self.travel_month,
            self.trip_duration
        )
        


        plan_cities =  tasks.plan_cities_itinerary(
            local_tour_guide,
            self.interests,
            self.travel_month,
            self.trip_duration,
            context=[identify_cities]
        )
        


        travel_plan = tasks.travel_to_country_cost(
            travel_planner,
            self.origin,
            self.destination_country,
            self.travel_month,
            self.trip_duration,
            context=[identify_cities]
        )



        trip_compile = tasks.final_plan_preparation(
            trip_compiler,
            self.origin,
            self.destination_country,
            self.interests,
            self.travel_month,
            self.trip_duration,
            context = [identify_cities, plan_cities, travel_plan]
            )


        # Define your custom crew here
        crew = Crew(
            agents=[city_selection_expert,
                    local_tour_guide,
                    travel_planner,
                    trip_compiler
                    ],
            tasks=[
                identify_cities,
                plan_cities,
                travel_plan,
                trip_compile
            ],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Trip Planner Crew")
    print('-------------------------------')
    origin = input(
        dedent("""
      From where will you be traveling from?
    """))
    country = input(
        dedent("""
      What country are u interested in visiting?
    """))
    month = input(
        dedent("""
      What is the month you are interested in traveling?
    """))
    duration = input(
        dedent("""
               What is your trip duration?
    """))
    interests = input(
        dedent("""
      What are some of your high level interests and hobbies?
    """))

    trip_crew = TripCrew(origin, country, interests, month, duration)
    result = trip_crew.run()
    print("\n\n########################")
    print("## Here is you Trip Plan")
    print("########################\n")
    print(result)
