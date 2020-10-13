import numpy as np
import cv2
import random

# Global variables
mouse_is_pressed = False
mode = 1
mouse_start_x = -1
mouse_start_y = -1
color = (255, 255, 255)

# Mouse event callback
def mouse_callback(event, x, y, flags, param):
    global mouse_is_pressed, mouse_start_x, mouse_start_y, color 
    overlay = img_color.copy() 
    alpha = 1
    
    # Left button pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        # Flag on
        mouse_is_pressed = True

        # Record the mouse position
        mouse_start_x = x
        mouse_start_y = y

        # Pick a random color
        color = (random.randrange(256), random.randrange(256), random.randrange(256))
    
    elif event == cv2.EVENT_MOUSEMOVE:
        if mouse_is_pressed == True:
            if mode == 1:
                cv2.rectangle(overlay, (mouse_start_x, mouse_start_y), (x, y), color, -1) 
                cv2.addWeighted(overlay, alpha, overlay, 1-alpha, 0, img2)
                cv2.imshow(winname, img2)

            elif mode == 2:
                cv2.ellipse(overlay, (mouse_start_x, mouse_start_y), (x-(mouse_start_x), y-(mouse_start_y)), 0, 0, 360, color, -1)
                cv2.addWeighted(overlay, alpha, overlay, 1-alpha, 0, img2)
                cv2.imshow(winname, img2)

            elif mode == 3:
                cv2.circle(img_color,(x,y), 5, color, -1)

    # Left button released
    elif event == cv2.EVENT_LBUTTONUP:
        # Flag off
        mouse_is_pressed = False

        # Draw rectangle
        if mode == 1:
            cv2.rectangle(img_color, (mouse_start_x, mouse_start_y), (x, y), color, -1) 

        # Draw ellipse
        elif mode == 2: 
            cv2.ellipse(img_color, (mouse_start_x, mouse_start_y), (x-(mouse_start_x), y-(mouse_start_y)), 0, 0, 360, color, -1)

        # Draw circle
        elif mode == 3:
            cv2.circle(img_color,(x,y), 5, color, -1)


# Create a black image
rows = 480
cols = 640
img_color = np.zeros((rows, cols, 3), np.uint8)
img2 = img_color.copy()

# Create a window
winname = 'Mouse Events'
cv2.namedWindow(winname)

# Register the mouse callback function
cv2.setMouseCallback(winname, mouse_callback)

# Infinite loop
while True: 
    cv2.imshow(winname, img_color) 
    key = cv2.waitKey(1)
    if key == ord('m'): 
        mode += 1
        if mode > 3:
            mode = 1
    elif key == 27: break
    
cv2.destroyAllWindows()