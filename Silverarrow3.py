import math

def reward_function(params):
    """
    Updated reward function for the AWS DeepRacer track.
    """

    # Retrieve the necessary input parameters
    all_wheels_on_track = params["all_wheels_on_track"]
    distance_from_center = params["distance_from_center"]
    heading = params["heading"]
    progress = params["progress"]
    speed = params["speed"]
    steps = params["steps"]
    track_length = params["track_length"]
    track_width = params["track_width"]
    waypoints = params["waypoints"]
    steering_angle = abs(params["steering_angle"])

    # Initialize the reward
    reward = 1e-3  # Small reward for staying on track

    # Distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3

    # Penalize if the car goes off track
    if not all_wheels_on_track:
        reward = 1e-3

    SPEED_THRESHOLD = 3.0
    if speed < SPEED_THRESHOLD:
        reward = 1e-3
    else:
        reward += 1.5

    # Reward for progress
    expected_progress = (steps / (track_length * 3)) * 100
    reward += 1.0 * (progress - expected_progress) / 100

    # Penalize reward if the car is steering too much
    ABS_STEERING_THRESHOLD = 15
    if abs(steering_angle) > ABS_STEERING_THRESHOLD:
        reward *= 0.8

    return float(max(reward, 1e-3))