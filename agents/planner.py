from agents.spacex_agent import SpaceXAgent
from agents.weather_agent import WeatherAgent
from agents.delay_eval_agent import DelayEvalAgent

class PlannerAgent:
    def create_plan(self, goal):
        return [
            {'agent': SpaceXAgent(), 'output': 'launch_info'},
            {'agent': WeatherAgent(), 'input': 'launch_info', 'output': 'weather_data'},
            {'agent': DelayEvalAgent(), 'input': 'weather_data', 'output': 'final_summary'}
        ]
