# 1. open camera
# 2. take picture of equation
# 3. send picture to mathpix
# 4. receive latex
# 5. convert latex to sympy
# 6. convert sympy to png
# 7. display png
import cv2
import requests
import sympy
from sympy.printing.preview import preview
from PIL import Image


# Step 1: Open Camera
# def open_camera():
#     # Initialize webcam
#     # cap = cv2.VideoCapture(0)
#     cap = cv2.VideoCapture("http://192.168.1.100:4747/video")

#     # Capture an image when space key is pressed
#     while True:
#         ret, frame = cap.read()
#         cv2.imshow("Image Capture", frame)
#         if cv2.waitKey(1) == ord(" "):
#             cv2.imwrite("captured_image.png", frame)
#             break

#     # Release webcam
#     cap.release()
#     cv2.destroyAllWindows()

#     # Return captured image
#     return frame


# # Step 3: Send Picture to Mathpix and receive LaTeX
# def send_to_mathpix(image_path, app_id, app_key):
#     url = "https://api.mathpix.com/v3/text"
#     headers = {
#         "app_id": app_id,
#         "app_key": app_key,
#         "Content-Type": "application/json",
#     }
#     with open(image_path, "rb") as image_file:
#         image_data = image_file.read()
#         r = requests.post(url, headers=headers, data=image_data)
#     return r.json()["text"]


# Step 5: Convert LaTeX to SymPy
def convert_to_sympy(latex_str):
    return sympy.sympify(latex_str)


# Step 6: Convert SymPy to PNG
def convert_to_png(sympy_expr, filename):
    preview(sympy_expr, viewer="file", filename=filename, euler=False)


# Step 7: Display PNG
def display_png(filename):
    img = Image.open(filename)
    img.show()


def main():
    # Step 1: Open Camera
    # image = open_camera()

    # # Step 2: Save Image
    # image_path = "images/captured_image.png"
    # cv2.imwrite(image_path, image)

    # # Step 3: Send Picture to Mathpix and receive LaTeX
    # app_id = "YOUR_MATHPIX_APP_ID"
    # app_key = "YOUR_MATHPIX_APP_KEY"
    # latex_str = send_to_mathpix(image_path, app_id, app_key)

    # Sample LaTeX string representing (a+b)^2 = a^2 + 2ab + b^2
    latex_str = r"\left(a + b\right)^{2} = a^{2} + 2 a b + b^{2}"

    # Step 4: Receive LaTeX and convert to SymPy
    sympy_expr = sympy.sympify(latex_str)

    # Step 5: Convert SymPy to PNG
    png_filename = "output.png"
    preview(sympy_expr, viewer="file", filename=png_filename, euler=False)

    # Step 6: Display PNG
    Image.open(png_filename).show()


if __name__ == "__main__":
    main()
