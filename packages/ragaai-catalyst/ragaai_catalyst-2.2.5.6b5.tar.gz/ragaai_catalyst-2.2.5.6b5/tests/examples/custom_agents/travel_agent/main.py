import argparse
from dotenv import load_dotenv
from tools import (
    llm_call,
    weather_tool,
    currency_converter_tool,
    flight_price_estimator_tool,
)
from agents import ItineraryAgent
from config import initialize_tracing

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))

from ragaai_catalyst import trace_agent, current_span

load_dotenv()

tracer = initialize_tracing()

@trace_agent(name="travel_agent")
def travel_agent(model_name: str = "gpt-4o-mini", provider: str = "openai"):
    current_span().add_metrics(
        name="travel_planning_session",
        score=0.9,
        reasoning="Main travel planning session",
        cost=0.05,
        latency=1.0,
    )
    
    print("Welcome to the Personalized Travel Planner!\n")

    # Get user input
    # user_input = input("Please describe your ideal vacation: ")
    user_input = "karela, 10 days, 1000$, nature"

    # Extract preferences
    preferences_prompt = f"""
    Extract key travel preferences from the following user input:
    "{user_input}"

    Please provide the extracted information in this format:
    Destination:
    Activities:
    Budget:
    Duration (in days):
    """
    extracted_preferences = llm_call(preferences_prompt, name="extract_preferences", model_name=model_name, provider=provider)
    print("\nExtracted Preferences:")
    print(extracted_preferences)

    # Parse extracted preferences
    preferences = {}
    for line in extracted_preferences.split("\n"):
        if ":" in line:
            key, value = line.split(":", 1)
            preferences[key.strip()] = value.strip()

    # Validate extracted preferences
    required_keys = ["Destination", "Activities", "Budget", "Duration (in days)"]
    if not all(key in preferences for key in required_keys):
        print("\nCould not extract all required preferences. Please try again.")
        return

    # Fetch additional information
    weather = weather_tool(preferences["Destination"])
    print(f"\nWeather in {preferences['Destination']}: {weather}")

    # Get departure city
    # print("Please enter your departure city: ")
    # origin = input()
    origin = "delhi"
    flight_price = flight_price_estimator_tool(origin, preferences["Destination"])
    print(flight_price)

    # Plan itinerary
    itinerary_agent = ItineraryAgent()
    itinerary = itinerary_agent.plan_itinerary(
        {
            "destination": preferences["Destination"],
            "origin": origin,
            "budget": float(preferences["Budget"].replace("$", "")),
            "budget_currency": "USD",
        },
        int(preferences["Duration (in days)"]),
    )
    print("\nPlanned Itinerary:")
    print(itinerary)

    budget_amount = float(preferences["Budget"].replace("$", "").replace(",", ""))
    converted_budget = currency_converter_tool(budget_amount, "USD", "INR")
    if converted_budget:
        print(f"\nBudget in INR: {converted_budget:.2f} INR")
    else:
        print("\nCurrency conversion not available.")

    summary_prompt = f"""
    Summarize the following travel plan:

    Destination: {preferences['Destination']}
    Activities: {preferences['Activities']}
    Budget: {preferences['Budget']}
    Duration: {preferences['Duration (in days)']} days
    Itinerary: {itinerary}
    Weather: {weather}
    Flight Price: {flight_price}

    Travel Summary:
    """
    travel_summary = llm_call(summary_prompt, name="generate_summary", model_name=model_name, provider=provider)
    print("\nTravel Summary:")
    print(travel_summary)

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Run the travel agent.")
    parser.add_argument("--model", type=str, default="gpt-4o-mini", help="The model to use (e.g., gpt-4o-mini).")
    parser.add_argument("--provider", type=str, default="openai", help="The LLM provider (e.g., openai).")
    args = parser.parse_args()


    with tracer:
        travel_agent(model_name=args.model, provider=args.provider)
    
