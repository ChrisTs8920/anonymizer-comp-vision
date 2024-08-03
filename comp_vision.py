import cv2 # OpenCV
import os
import time
import matplotlib.pyplot as plt 

# Load pre-trained models for face, face profile and license plate detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml')
face_profile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_profileface.xml')
plate_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_russian_plate_number.xml')


# Function to plot images
def plot_image(img): 
    plt.imshow(img, cmap="gray") 
    plt.axis('off') 
    plt.style.use('seaborn') 
    plt.show()


# Function to blur a region
def blur_region(image, x, y, w, h):
    # Extract region of interest
    ROI = image[y:y+h, x:x+w]
    # Apply blur to the region of interest
    blurred_ROI = cv2.GaussianBlur(ROI, (41, 41), 30)
    # Replace region of interest in image with blurred version
    image[y:y+h, x:x+w] = blurred_ROI


def blur_faces_and_plates(input_path, output_path):
    # Read the input image - OpenCV reads images by default in BGR format 
    image = cv2.imread(input_path)

    # Keep original image and convert BGR format into a RGB format (for plot)
    og_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 

    # Convert to grayscale for detection
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Detect frontal faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=7, minSize=(30, 30))
    # Detect face profiles
    profiles = face_profile_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=7, minSize=(30, 30))
    # Detect license plates
    plates = plate_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=7, minSize=(20, 20))
    
    # Blur frontal faces
    for (x, y, w, h) in faces:
        blur_region(image, x, y, w, h)
    
    # Blur face profiles
    for (x, y, w, h) in profiles:
        blur_region(image, x, y, w, h)

    # Blur license plates
    for (x, y, w, h) in plates:
        blur_region(image, x, y, w, h)

    # Save the output image
    cv2.imwrite(output_path, image)

    # Keep output image and convert BGR format into a RGB format (for plot)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 

    return og_image, image


def image_exists(image_name, input_path):
    # If it's a valid image file
    if os.path.isfile(input_path):
        if image_name.endswith(".jpg") or image_name.endswith(".jpeg") or image_name.endswith(".png") or image_name.endswith(".raw"):
            return True
    else:
        return False


def main():
    image_name = input("Enter image name (with extension): ")

    # Input and Output images will be located in corresponding directories, located in the same directory as python file
    input_path = os.path.join(os.path.dirname(__file__), "input_images/" + image_name)
    output_path = os.path.join(os.path.dirname(__file__), "output_images/" + "output_" + image_name)

    if image_exists(image_name, input_path):
        # Calculate execution time (parameters like image resolution and classifier parameters can affect execution time)
        start = time.time()
        og_image, image = blur_faces_and_plates(input_path, output_path) # anonymization
        end = time.time()

        print("Execution time: ", (round(end - start) * 1000), "ms")
        # Plot original image
        plot_image(og_image)
        # Plot blurred image
        plot_image(image)
    else:
        print("File does not exist or is not a valid image file.")


if __name__ == "__main__":
    main()