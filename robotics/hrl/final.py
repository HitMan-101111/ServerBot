import os
from gym import utils
from gym.envs.robotics import fetch_env


MODEL_XML_PATH = os.path.join("hrl", "final.xml")


class FinalEnv(fetch_env.FetchEnv, utils.EzPickle):
    def __init__(self, reward_type="dense"):
        initial_qpos = {
            "robot0:slide0": 0.405,
            "robot0:slide1": 0.48,
            "robot0:slide2": 0.0,
            "target_object:joint": [1.45, 0.74, 0.4, 1.0, 0.0, 0.0, 0.0],
            "obstacle_0:joint": [1.395, 0.74, 0.42, 1.0, 0.0, 0.0, 0.0],
            "obstacle_1:joint": [1.45, 0.74, 0.45, 1.0, 0.0, 0.0, 0.0],
            "obstacle_2:joint": [1.505, 0.74, 0.42, 1.0, 0.0, 0.0, 0.0],
            "obstacle_3:joint": [1.45, 0.795, 0.42, 1.0, 0.0, 0.0, 0.0],
            "obstacle_4:joint": [1.45, 0.685, 0.42, 1.0, 0.0, 0.0, 0.0],
        }
        fetch_env.FetchEnv.__init__(
            self,
            MODEL_XML_PATH,
            has_object=True,
            block_gripper=False,
            n_substeps=20,
            gripper_extra_height=0.2,
            target_in_the_air=True,
            target_offset=0.0,
            obj_range=0.15,
            target_range=0.15,
            distance_threshold=0.05,
            initial_qpos=initial_qpos,
            reward_type=reward_type,
            final_mode=True,
            cube_mode=True,
        )
        utils.EzPickle.__init__(self, reward_type=reward_type)
