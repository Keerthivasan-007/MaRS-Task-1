import numpy as np

def get_rotation_matrix(angles):
    rx, ry, rz = np.radians(angles)
    
    Rx = np.array([[1, 0, 0], [0, np.cos(rx), -np.sin(rx)], [0, np.sin(rx), np.cos(rx)]])
    Ry = np.array([[np.cos(ry), 0, np.sin(ry)], [0, 1, 0], [-np.sin(ry), 0, np.cos(ry)]])
    Rz = np.array([[np.cos(rz), -np.sin(rz), 0], [np.sin(rz), np.cos(rz), 0], [0, 0, 1]])
    
    return Rz @ Ry @ Rx

def find_object_in_world(obj_cam, rover_pos, rover_rot):
    """
    Transform object from camera frame to world frame.
    
    Assumes: Camera mount at (0,0,0) with no rotation
    Camera Frame → Rover Frame → World Frame
    """
    # Camera to Rover (no offset since camera is at rover origin)
    obj_rover = obj_cam
    
    # Rover to World
    R_rover = get_rotation_matrix(rover_rot)
    obj_world = R_rover @ np.array(obj_rover) + np.array(rover_pos)
    
    return obj_world

def format_coords(coords):
    """Format coordinates to show 3 decimal places."""
    return f"[{coords[0]:.3f} {coords[1]:.3f} {coords[2]:.3f}]"

def main():
    # Get 3 inputs
    obj_cam = tuple(map(float, input("Object Coordinates (camera): ").split(",")))
    rover_pos = tuple(map(float, input("Rover Position: ").split(",")))
    rover_rot = tuple(map(float, input("Rover Rotation (degrees): ").split(",")))
    
    # Calculate result
    world = find_object_in_world(obj_cam, rover_pos, rover_rot)
    
    # Show result
    print(f"\nObject (world):     {format_coords(world)}")
if __name__ == "__main__":
    main()