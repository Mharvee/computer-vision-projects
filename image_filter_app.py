import cv2

def apply_filters():
    image = cv2.imread("download.jpeg")

    if image is None:
        print("Error: Could not load image.")
        return

    print("Image loaded successfully!")  # Confirmation message

    # Show original image
    cv2.imshow('Original', image)

    # Apply grayscale filter
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Grayscale', gray)

    # Apply blur filter
    blur = cv2.GaussianBlur(image, (15, 15), 0)
    cv2.imshow('Blurred', blur)

    # Wait until you press a key, then close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    apply_filters()