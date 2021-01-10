# def deleteNode(head, val):
#     """
#     :type head: ListNode
#     :type val: int
#     :rtype: ListNode
#     """
#     value = 0
#     for i in head:
#         if i == val:
#             head.pop(head[value + 1])
#         else:
#             value += 1
#     return head

# print(deleteNode([4,5,1,3], 5))

# def run_in_series(self, next_waypoint: Transform, **kwargs) -> VehicleControl:
#     throttle = self.long_pid_controller.run_in_series(next_waypoint=next_waypoint,
#                                                         target_speed=kwargs.get("target_speed", self.max_speed))
#     steering,x,y,z= self.lat_pid_controller.run_in_series(next_waypoint=next_waypoint)
#     if y>0.8 or (x>-390 and x<0 and z<91):
#         if steering>0:
#             steering=0.01
#         else:
#             steering=-0.01


# if steering>-0.4 and steering<-0.05 and y<0.8 and x<0:
#         steering=steering*1.3
#     if x> 360 and x<390 and z>-60 and z<20:
#         throttle=0.9
#         steering = 0.9
#     if x> -570 and x<-420 and z<80 and z>10:
#         # throttle=0.9
#         steering = -0.4

from ROAR.agent_module.special_agents.waypoint_generating_agent import WaypointGeneratigAgent

def main():
    agent_config = AgentConfig.parse_file(Path("./ROAR_Sim/configurations/agent_configuration.json"))
    carla_config = CarlaConfig.parse_file(Path("./ROAR_Sim/configurations/configuration.json"))

    carla_runner = CarlaRunner(carla_settings=carla_config,
                               agent_settings=agent_config,
                               npc_agent_class=PurePursuitAgent)
    try:
        my_vehicle = carla_runner.set_carla_world()
        agent = WaypointGeneratigAgent(vehicle=my_vehicle, agent_settings=agent_config)
        carla_runner.start_game_loop(agent=agent, use_manual_control=True)
    except Exception as e:
        logging.error(f"Something bad happened during initialization: {e}")
        carla_runner.on_finish()
        logging.error(f"{e}. Might be a good idea to restart Server")


class WaypointGeneratigAgent(Agent):
    def __init__(self, vehicle: Vehicle, agent_settings: AgentConfig, **kwargs):
        super().__init__(vehicle=vehicle, agent_settings=agent_settings, **kwargs)
        self.output_file_path: Path = self.output_folder_path / "easy_map_waypoints.txt"
        self.output_file = self.output_file_path.open('w')

