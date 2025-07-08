import numpy as np
import cv2
import argparse

def main():
    # Define the parser
    parser = argparse.ArgumentParser(description='Transform camera coordinates to real-world coordinates')
    parser.add_argument('x', type=float, help='x-coordinate in camera space')
    parser.add_argument('y', type=float, help='y-coordinate in camera space')


    # what we show on the DMD, converted into real workd
    pos = 200 * 20.37e-3
    # Projector coordinates (you can adjust these based on your actual data)
    projector_coords = pos * np.array([[-1, -1], [1, -1], [1,1], [-1,1]], dtype=np.float32)
    # starting top left, and then clockwise rotated
    # Corresponding camera coordinates (adjust based on your actual data)
    camera_coords = np.array([[1177, 831], [1655, 843], [1643, 1322], [1168, 1308]], dtype=np.float32)



    pos = 100 * 20.37e-3
    # Projector coordinates (you can adjust these based on your actual data)
    projector_coords = pos * np.array([[-1, -1], [1, -1], [1,1], [-1,1]], dtype=np.float32)
    # starting top left, and then clockwise rotated
    # Corresponding camera coordinates (adjust based on your actual data)
    camera_coords = np.array([[1280, 995], [1519, 1000], [1513, 1238], [1275, 1232]], dtype=np.float32) 



    # Parse the arguments
    args = parser.parse_args()

    # Compute the homography matrix (inverse to map from camera to projector)
    homography_matrix, _ = cv2.findHomography(camera_coords, projector_coords)

    # Point in camera coordinates to be transformed
    camera_point = np.array([[args.x, args.y]], dtype=np.float32)

    # Transform the point using the homography matrix
    projector_point = cv2.perspectiveTransform(camera_point.reshape(-1,1,2), homography_matrix)

    # Print the transformed point
    print("Point in projector coordinates (real-world): ", projector_point.reshape(-1,2))

if __name__ == "__main__":
    main()

