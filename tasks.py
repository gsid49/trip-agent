from crewai import Task
from textwrap import dedent

"""
Creating Tasks Cheat Sheet:
- Begin with the end in mind. Identify the specific outcome your tasks are aiming to achieve.
- Break down the outcome into actionable tasks, assigning each task to the appropriate agent.
- Ensure tasks are descriptive, providing clear instructions and expected deliverables.

Goal:
- Develop a detailed itinerary, including city selection, attractions, and practical travel advice.

Key Steps for Task Creation:
1. Identify the Desired Outcome: Define what success looks like for your project.
    - A detailed 7 day travel itenerary.

2. Task Breakdown: Divide the goal into smaller, manageable tasks that agents can execute.
    - Itenerary Planning: develop a detailed plan for each day of the trip.
    - City Selection: Analayze and pick the best cities to visit.
    - Local Tour Guide: Find a local expert to provide insights and recommendations.

3. Assign Tasks to Agents: Match tasks with agents based on their roles and expertise.

4. Task Description Template:
  - Use this template as a guide to define each task in your CrewAI application. 
  - This template helps ensure that each task is clearly defined, actionable, and aligned with the specific goals of your project.

  Template:
  ---------
  def [task_name](self, agent, [parameters]):
      return Task(description=dedent(f'''
      **Task**: [Provide a concise name or summary of the task.]
      **Description**: [Detailed description of what the agent is expected to do, including actionable steps and expected outcomes. This should be clear and direct, outlining the specific actions required to complete the task.]

      **Parameters**: 
      - [Parameter 1]: [Description]
      - [Parameter 2]: [Description]
      ... [Add more parameters as needed.]

      **Note**: [Optional section for incentives or encouragement for high-quality work. This can include tips, additional context, or motivations to encourage agents to deliver their best work.]

      '''), agent=agent)

"""


class TravelTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def identify_cities(self, agent, destination_country, interests, travel_month, trip_duration, context=[]):
        return Task(
            description=dedent(
                f"""
                    **Task**:  Identify the Best Cities for the Trip
                    **Description**: Given a destination country that a traveler wants to visit, you need to 
                    analyze and select the best cities within that country for the trip based on specific 
                    criteria such as travel month, interests, weather patterns and seasonal events. The 
                    shortlisted cities should be chosen in a way that they are visitable within the trip duration. 


                    **Parameters**: 
                    - Destination Country: {destination_country}
                    - Interests: {interests}
                    - Travel Month: {travel_month}
                    - Trip Duration: {trip_duration}

                    **Note**: {self.__tip_section()}
        """
            ),
            expected_output=dedent(
                f"""
                    A list of shortlisted cities based on the criteria provided by the traveler.
            """),
            agent=agent,
            context=context
        )
    
    
    def plan_cities_itinerary(self, agent, interests, travel_month, trip_duration, context=[]):
        return Task(
            description=dedent(
                f"""
            **Task**: Develop a full travel itinerary visiting the provided cities in the given trip duration
            **Description**: From the list of cities, create a detailed itinerary with per-day plans. 
            The itinerary should take into account traveler's interest. The itinerary should also see
            if there are any interesting events happening during the travel month that the traveler can enjoy.
            The itinerary should include must-go places to visit as well as must-go restaurants.
            This itinerary should also account for all aspects of the trip, including arrival, departure and 
            travelling within the cities. Also, include recommended mode of transport between the cities and 
            potential costs.

            **Parameters**: 
            - Interests: {interests}
            - Travel Month: {travel_month}
            - Trip Duration: {trip_duration}

            **Note**: {self.__tip_section()}
        """
            ),
            expected_output=dedent(
                f"""
                    A detailed day-by-day plan for the trip.
            """),
            agent=agent,
            context=context
        )

    
    def travel_to_country_cost(self, agent, origin, destination_country, travel_month, trip_duration, context=[]):
        return Task(
            description=dedent(
                f"""
            **Task**: Figure out the best optimized travel plan from the origin to the destination country.
            **Description**: Given the origin and the destination country, figure out what is the best and reasonably cheapest way
            to travel from origin to destination country for the trip duration. Plan such that you arrive from the origin 
            to the first city
            and you depart fromt the last city in the list. You have the flexibility to select the travel dates within the travel
            month, so you can try to adjust the travel dates to get the best possible price for the traveler. Where needed make
            generally good travel planning decisions, such as, prefer less number of flight legs if you have to pay a little bit more, 
            use faster mode of transportation if the prices are not too different. 

            Finally return the full travel details - including the projected cost of travel with a breakdown of the costs.

            **Parameters**: 
            - Origin: {origin}
            - Destination country: {destination_country}
            - Travel Month: {travel_month}
            - Trip Duration: {trip_duration}

            **Note**: {self.__tip_section()}
        """
            ),
            expected_output=dedent(
                f"""
                    A detailed optimized travel plan from origin to destination country including the breakdown of the costs.
            """),
            agent=agent,
            context=context
        )

    def final_plan_preparation(self, agent, origin, destination_country, interests, travel_month, trip_duration, context=[]):
        return Task(
            description=dedent(
                f"""
            **Task**: Given all the research, lay out a final plan for the trip.
            **Description**: Compile all the research done - such as cities to visit, day by day travel plans and travel 
            to destination country plans into a well formed final itinerary that can be provided to the traveler so that 
            they can book their travel. It should include the projected costs as well.

            **Parameters**: 
            - Origin: {origin}
            - Destination country: {destination_country}
            - Interests: {interests}
            - Travel Month: {travel_month}
            - Trip Duration: {trip_duration}

            **Note**: {self.__tip_section()}
        """
            ),
            expected_output=dedent(
                f"""
                   A well compiled travel plan.
            """),
            agent=agent,
            context=context
        )

