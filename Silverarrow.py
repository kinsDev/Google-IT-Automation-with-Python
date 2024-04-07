import math


def reward_function(params):
    """
    Reward function for the AWS DeepRacer track.
    """

    # Retrieve the necessary input parameters
    all_wheels_on_track = params["all_wheels_on_track"]
    x = params["x"]
    y = params["y"]
    closest_waypoints = params["closest_waypoints"]
    distance_from_center = params["distance_from_center"]
    heading = params["heading"]
    progress = params["progress"]
    speed = params["speed"]
    steps = params["steps"]
    track_length = params["track_length"]
    track_width = params["track_width"]
    waypoints = params["waypoints"]

    # Initialize the reward
    reward = 1e-3  # Small reward for staying on track

    # Reward for progress
    expected_progress = (steps / (track_length * 3)) * 100
    reward += 0.5 * (progress - expected_progress) / 100  # Reward based on progress relative to expected

    # Reward for speed
    min_speed = 1.0
    max_speed = 4.0
    optimal_speed = 3.5
    speed_reward = max(1 - abs(speed - optimal_speed) / (optimal_speed - min_speed), 0)
    reward += 1.5 * speed_reward  # Increased weight for speed reward

    # Reward for staying on track
    if all_wheels_on_track:
        reward += 1.0
    else:
        reward *= 0.7  # Adjusted penalty for going off track

    # Reward for distance from center
    track_center = track_width / 2
    distance_reward = 1 - (distance_from_center / track_center)
    reward += 0.7 * distance_reward  # Adjusted weight for distance from center

    # Reward for heading alignment
    next_waypoint = waypoints[closest_waypoints[1]]
    track_direction = math.atan2(next_waypoint[1] - y, next_waypoint[0] - x)
    heading_diff = abs(track_direction - math.radians(heading))
    heading_reward = 1 - (heading_diff / math.pi)
    reward += 0.5 * heading_reward  # Adjusted weight for heading alignment

    return float(max(reward, 1e-3))  # Ensure the reward is at least 1e-3