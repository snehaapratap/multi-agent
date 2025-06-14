from agents.planner import PlannerAgent
from agents.spacex import SpaceXAgent
from agents.weather import WeatherAgent
from agents.delay_eval import DelayEvalAgent

def main():
    user_goal = "Find the next SpaceX launch, check weather at that location, then summarize if it may be delayed."

    planner = PlannerAgent()
    plan = planner.create_plan(user_goal)

    context = {}
    for task in plan:
        agent = task['agent']
        input_key = task.get('input')
        input_data = context.get(input_key) if input_key else None
        output = agent.run(input_data)
        context[task['output']] = output

    print("Final Summary:", context['final_summary'])

if __name__ == "__main__":
    main()
