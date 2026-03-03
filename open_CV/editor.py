import cv2
import numpy as np
import os
import ctypes

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".tif", ".webp"}
VIDEO_EXTENSIONS = {".mp4", ".avi", ".mov", ".mkv", ".wmv", ".flv", ".mpeg", ".mpg", ".m4v"}


def show_image(win_name, image_data):
    cv2.imshow(win_name, image_data)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def process_video_stream(video_path, frame_transform=None, window_name="video"):
    capture = cv2.VideoCapture(video_path)
    if not capture.isOpened():
        print("Could not open video.")
        return

    while True:
        ok, frame = capture.read()
        if not ok:
            break

        output_frame = frame_transform(frame) if frame_transform else frame
        cv2.imshow(window_name, output_frame)

        key = cv2.waitKey(25) & 0xFF
        if key == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()


def save_video_file(video_path, output_path, frame_transform=None, is_gray=False):
    capture = cv2.VideoCapture(video_path)
    if not capture.isOpened():
        raise ValueError("Could not open video for saving.")

    fps = capture.get(cv2.CAP_PROP_FPS)
    if fps <= 0:
        fps = 25.0

    width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height), not is_gray)
    if not writer.isOpened():
        capture.release()
        raise ValueError("Could not create output video file. Check output path/extension.")

    while True:
        ok, frame = capture.read()
        if not ok:
            break

        output_frame = frame_transform(frame) if frame_transform else frame

        if is_gray and len(output_frame.shape) == 3:
            output_frame = cv2.cvtColor(output_frame, cv2.COLOR_BGR2GRAY)
        elif not is_gray and len(output_frame.shape) == 2:
            output_frame = cv2.cvtColor(output_frame, cv2.COLOR_GRAY2BGR)

        writer.write(output_frame)

    writer.release()
    capture.release()


def access_live_webcam():
    capture = cv2.VideoCapture(0)
    if not capture.isOpened():
        print("Could not access webcam.")
        return

    try:
        user32 = ctypes.windll.user32
        screen_w = int(user32.GetSystemMetrics(0))
        screen_h = int(user32.GetSystemMetrics(1))
    except Exception:
        screen_w, screen_h = 1366, 768

    scale_text = input(
        "Enter webcam preview size as % of screen (10-100, Enter for 60): "
    ).strip()

    if scale_text == "":
        scale_percent = 60
    else:
        scale_percent = int(scale_text)
        if scale_percent < 10 or scale_percent > 100:
            raise ValueError("Preview size must be between 10 and 100.")

    target_preview_w = int(screen_w * scale_percent / 100)
    target_preview_h = int(screen_h * scale_percent / 100)

    cv2.namedWindow("live-webcam", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("live-webcam", target_preview_w, target_preview_h)

    print("Live webcam started. Press 'q' to stop.")
    while True:
        ok, frame = capture.read()
        if not ok:
            break

        frame_h, frame_w = frame.shape[:2]
        scale = min(target_preview_w / frame_w, target_preview_h / frame_h)
        display_w = max(1, int(frame_w * scale))
        display_h = max(1, int(frame_h * scale))
        frame = cv2.resize(frame, (display_w, display_h), interpolation=cv2.INTER_AREA)

        cv2.imshow("live-webcam", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()


def edit_image(image_path):
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Invalid image path or unsupported image format.")

    latest_img = img.copy()
    show_image('image', img)

    while True:
        ch = input("""
What operation you want to perform on the image:
1. Get details about the image
2. Resize
3. Shift
4. Rotate
5. Crop
6. Flip
7. Convert to grayscale
8. Convert to binary
9. Thresholding
10. Morphing
11. Edge detection
12. Adding shapes and text
13. Blurring
14. Save image
15. Exit
Enter your choice (1-15):
""").strip()

        if ch == '1':
            print("The height and width of the image is:", img.shape)

        elif ch == '2':
            inp = input("Do you want to maintain the aspect ratio? (y/n): ").strip().lower()
            print("The height and width of the image is:", img.shape)

            if inp == 'y':
                scale = int(input("Enter the scale factor (100 is original): "))
                w = int(img.shape[1] * scale / 100)
                h = int(img.shape[0] * scale / 100)
            else:
                w = int(input("Enter the new width (to remain unchanged enter 0): "))
                h = int(input("Enter the new height (to remain unchanged enter 0): "))
                if w == 0:
                    w = img.shape[1]
                if h == 0:
                    h = img.shape[0]

            resized_img = cv2.resize(img, (w, h), interpolation=cv2.INTER_AREA)
            latest_img = resized_img
            show_image('image', resized_img)

        elif ch == '3':
            x_shift = int(input("Enter the shift in x direction: "))
            y_shift = int(input("Enter the shift in y direction: "))
            m = np.float32([[1, 0, x_shift], [0, 1, y_shift]])
            shifted_img = cv2.warpAffine(img, m, (img.shape[1], img.shape[0]))
            latest_img = shifted_img
            show_image('image', shifted_img)

        elif ch == '4':
            angle = float(input("Enter the angle of rotation (in degrees): "))
            center = (img.shape[1] // 2, img.shape[0] // 2)
            m = cv2.getRotationMatrix2D(center, angle, 1.0)
            rotated_img = cv2.warpAffine(img, m, (img.shape[1], img.shape[0]))
            latest_img = rotated_img
            show_image('image', rotated_img)

        elif ch == '5':
            x1 = int(input("Enter x1 (left): "))
            y1 = int(input("Enter y1 (top): "))
            x2 = int(input("Enter x2 (right): "))
            y2 = int(input("Enter y2 (bottom): "))
            cropped_img = img[y1:y2, x1:x2]
            latest_img = cropped_img
            show_image('image', cropped_img)

        elif ch == '6':
            flip_code = int(input("Enter the flip code (0 vertical, 1 horizontal, -1 both): "))
            flipped_img = cv2.flip(img, flip_code)
            latest_img = flipped_img
            show_image('image', flipped_img)

        elif ch == '7':
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            latest_img = gray_img
            show_image('image', gray_img)

        elif ch == '8':
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            _, binary_img = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)
            latest_img = binary_img
            show_image('image', binary_img)

        elif ch == '9':
            threshold_value = int(input("Enter the threshold value (0-255): "))
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            _, thresholded_img = cv2.threshold(gray_img, threshold_value, 255, cv2.THRESH_BINARY)
            latest_img = thresholded_img
            show_image('image', thresholded_img)

        elif ch == '10':
            kernel_size = int(input("Enter kernel size: "))
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
            operation = int(input("Morph operation (1:Erosion 2:Dilation 3:Opening 4:Closing 5:Gradient 6:TopHat 7:BlackHat): "))
            iter_text = input("Enter iterations (1-10, Enter for default 1): ").strip()
            iterations = 1 if iter_text == "" else int(iter_text)

            if iterations < 1 or iterations > 10:
                raise ValueError("Iterations must be between 1 and 10.")

            if operation == 1:
                morphed_img = cv2.erode(img, kernel, iterations=iterations)
            elif operation == 2:
                morphed_img = cv2.dilate(img, kernel, iterations=iterations)
            elif operation == 3:
                morphed_img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations=iterations)
            elif operation == 4:
                morphed_img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations=iterations)
            elif operation == 5:
                morphed_img = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel, iterations=iterations)
            elif operation == 6:
                morphed_img = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel, iterations=iterations)
            elif operation == 7:
                morphed_img = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel, iterations=iterations)
            else:
                raise ValueError("Invalid morphological operation selected.")

            latest_img = morphed_img
            show_image('image', morphed_img)

        elif ch == '11':
            edges = cv2.Canny(img, 100, 200)
            latest_img = edges
            show_image('image', edges)

        elif ch == '12':
            target = input("Draw on (1) loaded image or (2) blank page? ").strip()
            if target == '2':
                canvas_w = int(input("Enter blank page width: "))
                canvas_h = int(input("Enter blank page height: "))
                bg = input("Enter background color in BGR (default 255,255,255): ").strip()
                bg_color = (255, 255, 255) if bg == "" else tuple(map(int, bg.split(',')))
                img = np.full((canvas_h, canvas_w, 3), bg_color, dtype=np.uint8)

            shape = int(input("Enter shape (1 rectangle, 2 circle, 3 line, 4 text): "))
            if shape == 1:
                x1 = int(input("Enter x1: "))
                y1 = int(input("Enter y1: "))
                x2 = int(input("Enter x2: "))
                y2 = int(input("Enter y2: "))
                color = tuple(map(int, input("Enter BGR color (e.g., 255,0,0): ").split(',')))
                thickness = int(input("Enter thickness: "))
                cv2.rectangle(img, (x1, y1), (x2, y2), color, thickness)
            elif shape == 2:
                center_x = int(input("Enter center x: "))
                center_y = int(input("Enter center y: "))
                radius = int(input("Enter radius: "))
                color = tuple(map(int, input("Enter BGR color (e.g., 255,0,0): ").split(',')))
                thickness = int(input("Enter thickness: "))
                cv2.circle(img, (center_x, center_y), radius, color, thickness)
            elif shape == 3:
                x1 = int(input("Enter x1: "))
                y1 = int(input("Enter y1: "))
                x2 = int(input("Enter x2: "))
                y2 = int(input("Enter y2: "))
                color = tuple(map(int, input("Enter BGR color (e.g., 255,0,0): ").split(',')))
                thickness = int(input("Enter thickness: "))
                cv2.line(img, (x1, y1), (x2, y2), color, thickness)
            elif shape == 4:
                text = input("Enter text: ")
                x = int(input("Enter x: "))
                y = int(input("Enter y: "))
                font_scale = float(input("Enter font scale (e.g., 1.0): "))
                color = tuple(map(int, input("Enter BGR color (e.g., 255,0,0): ").split(',')))
                thickness = int(input("Enter thickness: "))
                cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, font_scale, color, thickness)

            latest_img = img.copy()
            show_image('image', img)

        elif ch == '13':
            blur_type = input("Blur type: 1 average, 2 Gaussian, 3 median: ").strip()
            kernel_size = int(input("Enter kernel size for blurring: "))

            if blur_type == '1':
                blurred_img = cv2.blur(img, (kernel_size, kernel_size))
            elif blur_type == '2':
                blurred_img = cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)
            elif blur_type == '3':
                blurred_img = cv2.medianBlur(img, kernel_size)
            else:
                print("Invalid blur type.")
                continue

            latest_img = blurred_img
            show_image('image', blurred_img)

        elif ch == '14':
            save_path = input("Enter output image path (example: output.jpg): ").strip().strip('"')
            if save_path == "":
                print("Output path cannot be empty.")
                continue

            ok = cv2.imwrite(save_path, latest_img)
            if ok:
                print(f"Image saved to: {save_path}")
            else:
                print("Failed to save image. Check destination path and extension.")

        elif ch == '15':
            print("Exiting image editor.")
            break

        else:
            print("Invalid option. Please choose from 1 to 15.")

def edit_video(video_path):
    while True:
        ch = input("""
What operation you want to perform on the video:
1. Get video details
2. Play original video
3. Convert to grayscale
4. Convert to binary
5. Edge detection
6. Blurring
7. Flip
8. Rotate
9. Save video
10. Access live webcam
11. Exit
Enter your choice (1-11):
""").strip()

        if ch == '1':
            capture = cv2.VideoCapture(video_path)
            if not capture.isOpened():
                print("Could not open video.")
                continue

            width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
            fps = capture.get(cv2.CAP_PROP_FPS)
            total_frames = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
            capture.release()

            print(f"Resolution: {width}x{height}")
            print(f"FPS: {fps}")
            print(f"Total frames: {total_frames}")

        elif ch == '2':
            print("Press 'q' to stop video playback.")
            process_video_stream(video_path, None, "video")

        elif ch == '3':
            print("Press 'q' to stop video playback.")
            process_video_stream(video_path, lambda frame: cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), "video-gray")

        elif ch == '4':
            threshold_value = int(input("Enter threshold value (0-255): "))

            def to_binary(frame):
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                _, binary_frame = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)
                return binary_frame

            print("Press 'q' to stop video playback.")
            process_video_stream(video_path, to_binary, "video-binary")

        elif ch == '5':
            print("Press 'q' to stop video playback.")
            process_video_stream(video_path, lambda frame: cv2.Canny(frame, 100, 200), "video-edge")

        elif ch == '6':
            blur_type = input("Blur type: 1 average, 2 Gaussian, 3 median: ").strip()
            kernel_size = int(input("Enter kernel size: "))

            if blur_type == '1':
                transform = lambda frame: cv2.blur(frame, (kernel_size, kernel_size))
            elif blur_type == '2':
                transform = lambda frame: cv2.GaussianBlur(frame, (kernel_size, kernel_size), 0)
            elif blur_type == '3':
                transform = lambda frame: cv2.medianBlur(frame, kernel_size)
            else:
                print("Invalid blur type.")
                continue

            print("Press 'q' to stop video playback.")
            process_video_stream(video_path, transform, "video-blur")

        elif ch == '7':
            flip_code = int(input("Enter flip code (0 vertical, 1 horizontal, -1 both): "))
            print("Press 'q' to stop video playback.")
            process_video_stream(video_path, lambda frame: cv2.flip(frame, flip_code), "video-flip")

        elif ch == '8':
            angle = float(input("Enter rotation angle in degrees: "))

            def rotate_frame(frame):
                h, w = frame.shape[:2]
                center = (w // 2, h // 2)
                m = cv2.getRotationMatrix2D(center, angle, 1.0)
                return cv2.warpAffine(frame, m, (w, h))

            print("Press 'q' to stop video playback.")
            process_video_stream(video_path, rotate_frame, "video-rotate")

        elif ch == '9':
            save_path = input("Enter output video path (example: output.mp4): ").strip().strip('"')
            if save_path == "":
                print("Output path cannot be empty.")
                continue

            save_choice = input(
                "Save as: 1 original, 2 grayscale, 3 binary, 4 edge, 5 blur, 6 flip, 7 rotate: "
            ).strip()

            transform = None
            is_gray = False

            if save_choice == '1':
                transform = None
            elif save_choice == '2':
                transform = lambda frame: cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                is_gray = True
            elif save_choice == '3':
                threshold_value = int(input("Enter threshold value (0-255): "))

                def to_binary(frame):
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    _, binary_frame = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)
                    return binary_frame

                transform = to_binary
                is_gray = True
            elif save_choice == '4':
                transform = lambda frame: cv2.Canny(frame, 100, 200)
                is_gray = True
            elif save_choice == '5':
                blur_type = input("Blur type: 1 average, 2 Gaussian, 3 median: ").strip()
                kernel_size = int(input("Enter kernel size: "))

                if blur_type == '1':
                    transform = lambda frame: cv2.blur(frame, (kernel_size, kernel_size))
                elif blur_type == '2':
                    transform = lambda frame: cv2.GaussianBlur(frame, (kernel_size, kernel_size), 0)
                elif blur_type == '3':
                    transform = lambda frame: cv2.medianBlur(frame, kernel_size)
                else:
                    print("Invalid blur type.")
                    continue
            elif save_choice == '6':
                flip_code = int(input("Enter flip code (0 vertical, 1 horizontal, -1 both): "))
                transform = lambda frame: cv2.flip(frame, flip_code)
            elif save_choice == '7':
                angle = float(input("Enter rotation angle in degrees: "))

                def rotate_frame(frame):
                    h, w = frame.shape[:2]
                    center = (w // 2, h // 2)
                    m = cv2.getRotationMatrix2D(center, angle, 1.0)
                    return cv2.warpAffine(frame, m, (w, h))

                transform = rotate_frame
            else:
                print("Invalid save option.")
                continue

            try:
                save_video_file(video_path, save_path, transform, is_gray)
                print(f"Video saved to: {save_path}")
            except Exception as exc:
                print(f"Failed to save video: {exc}")

        elif ch == '10':
            access_live_webcam()

        elif ch == '11':
            print("Exiting video editor.")
            break

        else:
            print("Invalid option. Please choose from 1 to 11.")


def main():
    source_choice = input(
        "Choose source: 1 image file, 2 video file, 3 live webcam: "
    ).strip()

    if source_choice == '3':
        access_live_webcam()
        return

    source_path = input("Enter destination path: ").strip().strip('"')

    if not os.path.isfile(source_path):
        raise FileNotFoundError("Given destination path is wrong or file does not exist.")

    extension = os.path.splitext(source_path)[1].lower()

    if source_choice == '1':
        if extension not in IMAGE_EXTENSIONS:
            raise ValueError("Selected image mode, but file extension is not a supported image type.")
        edit_image(source_path)
    elif source_choice == '2':
        if extension not in VIDEO_EXTENSIONS:
            raise ValueError("Selected video mode, but file extension is not a supported video type.")
        edit_video(source_path)
    else:
        raise ValueError("Invalid source choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"Error: {exc}")