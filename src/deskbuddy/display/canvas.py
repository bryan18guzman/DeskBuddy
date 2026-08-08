from PIL import Image, ImageDraw


DISPLAY_SIZE = (240, 240)


def create_idle_face() -> Image.Image:
    """Create DeskBuddy's first simple face."""

    image = Image.new("RGB", DISPLAY_SIZE, "black")
    draw = ImageDraw.Draw(image)

    eye_width = 42
    eye_height = 62
    eye_y = 89

    left_eye_box = (
        55,
        eye_y,
        55 + eye_width,
        eye_y + eye_height,
    )

    right_eye_box = (
        143,
        eye_y,
        143 + eye_width,
        eye_y + eye_height,
    )

    draw.rounded_rectangle(
        left_eye_box,
        radius=20,
        fill="white",
    )

    draw.rounded_rectangle(
        right_eye_box,
        radius=20,
        fill="white",
    )

    return image