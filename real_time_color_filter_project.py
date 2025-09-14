import cv2
from matplotlib import pyplot as plt

def display_image(title, image):
    plt.figure(figsize=(8, 8))
    if len(image.shape) == 2:
        plt.imshow(image, cmap='gray')
    else:
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()

def apply_color_filter(image, filter_type):
    filtered_image = image.copy()
    if filter_type == 'red_tint':
        filtered_image[:, :, 1] = 0
        filtered_image[:, :, 0] = 0
    elif filter_type == 'blue_tint':
        filtered_image[:, :, 1] = 0
        filtered_image[:, :, 2] = 0
    elif filter_type == 'green_tint':
        filtered_image[:, :, 0] = 0
        filtered_image[:, :, 2] = 0
    elif filter_type == "increase_red":
        filtered_image[:, :, 2] = cv2.add(filtered_image[:, :, 2], 50)
    elif filter_type == "decrease_blue":
        filtered_image[:, :, 0] = cv2.subtract(filtered_image[:, :, 0], 50)
    return filtered_image

image_path = "fire-dragon-menacing-black-body-uqp2uj30eoedyoob.jpg"
image = cv2.imread(image_path)
if image is None:
    print("Error: Could not load image.")
else:
    filter_type = "original"

    print("Select a color filter to apply:")
    print("r - Red Tint")
    print("g - Green Tint")
    print("b - Blue Tint")
    print("i - Increase Red Channel")
    print("d - Decrease Blue Channel")
    print("q - Quit")

    while True:
        if filter_type == "original":
            filtered_image = image.copy()
        else:
            filtered_image = apply_color_filter(image, filter_type)

        cv2.imshow("Filtered image", filtered_image)

        key = cv2.waitKey(0) & 0xFF

        if key == ord('r'):
            filter_type = 'red_tint'
        elif key == ord('g'):
            filter_type = 'green_tint'
        elif key == ord('b'):
            filter_type = 'blue_tint'
        elif key == ord('i'):
            filter_type = 'increase_red'
        elif key == ord('d'):
            filter_type = 'decrease_blue'
        elif key == ord('q'):
            print("Exiting...")
            cv2.destroyAllWindows()
            break
        else:
            print("Invalid key. Please select a valid option.")
    cv2.destroyAllWindows()