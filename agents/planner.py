from agents.spacex import SpaceXAgent
from agents.weather import WeatherAgent
from agents.delay_eval import DelayEvalAgent

class PlannerAgent:
    def create_plan(self, goal):
        return [
            {'agent': SpaceXAgent(), 'output': 'launch_info'},
            {'agent': WeatherAgent(), 'input': 'launch_info', 'output': 'weather_data'},
            {'agent': DelayEvalAgent(), 'input': 'weather_data', 'output': 'final_summary'}
        ]
