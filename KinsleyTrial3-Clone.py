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
    reward += 1.0 * (progress - expected_progress) / 100  # Maintain weight for progress

    # Reward for speed
    min_speed = 1.0  # Maintain min_speed for slower speeds in corners
    max_speed = 4.0  # Maintain increased max_speed for higher top speeds

    # Calculate the curvature at the current position
    current_waypoint = waypoints[closest_waypoints[0]]
    next_waypoint = waypoints[closest_waypoints[1]]
    curvature = math.atan2(next_waypoint[1] - current_waypoint[1], next_waypoint[0] - current_waypoint[0])

    # Adjust the optimal speed based on curvature
    optimal_speed = max_speed
    curvature_threshold = math.pi / 4  # Adjust this value as needed
    if abs(curvature) > curvature_threshold:
        # Sharper turn, decrease optimal speed based on curvature
        optimal_speed = min_speed + (max_speed - min_speed) * (1 - abs(curvature) / math.pi)

    speed_reward = max(1 - abs(speed - optimal_speed) / (optimal_speed - min_speed), 0)
    reward += 2.0 * speed_reward  # Maintain weight for speed reward

    # Reward for staying on track
    if all_wheels_on_track:
        reward += 1.0
    else:
        reward *= 0.5  # Maintain penalty for going off track

    # Reward for distance from center
    track_center = track_width / 2
    distance_reward = 1 - (distance_from_center / track_center)
    reward += 0.5 * distance_reward  # Maintain weight for distance from center

    # Reward for heading alignment
    next_waypoint = waypoints[closest_waypoints[1]]
    track_direction = math.atan2(next_waypoint[1] - y, next_waypoint[0] - x)
    heading_diff = abs(track_direction - math.radians(heading))
    heading_reward = 1 - (heading_diff / math.pi)
    reward += heading_reward

    return float(max(reward, 1e-3))  # Ensure the reward is at least 1e-3