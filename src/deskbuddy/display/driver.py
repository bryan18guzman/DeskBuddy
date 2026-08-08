from pathlib import Path
import sys
from typing import Any

from PIL import Image


# Waveshare's downloaded library is outside our src directory.
PROJECT_ROOT = Path(__file__).resolve().parents[3]
WAVESHARE_PYTHON_DIR = (
    PROJECT_ROOT
    / "third_party"
    / "LCD_Module_RPI_code"
    / "RaspberryPi"
    / "python"
)

if not WAVESHARE_PYTHON_DIR.exists():
    raise FileNotFoundError(
        f"Waveshare library not found at: {WAVESHARE_PYTHON_DIR}"
    )

sys.path.insert(0, str(WAVESHARE_PYTHON_DIR))

from lib import LCD_1inch28  # noqa: E402


class DisplayDriver:
    """Controls the Waveshare 1.28-inch GC9A01 display."""

    def __init__(self) -> None:
        self._display: Any = LCD_1inch28.LCD_1inch28()
        self.width: int = self._display.width
        self.height: int = self._display.height
        self._initialized = False

    def initialize(self) -> None:
        """Initialize the physical display."""
        self._display.Init()
        self._display.bl_DutyCycle(100)
        self._display.clear()
        self._initialized = True

    def show(self, image: Image.Image) -> None:
        """Send a Pillow image to the display."""
        if not self._initialized:
            raise RuntimeError("Display must be initialized before showing an image.")

        if image.size != (self.width, self.height):
            raise ValueError(
                f"Image must be {self.width}x{self.height}, got {image.size}."
            )

        self._display.ShowImage(image)

    def clear(self) -> None:
        """Clear the display."""
        if self._initialized:
            self._display.clear()

    def cleanup(self) -> None:
        """Release GPIO and display resources."""
        if self._initialized:
            self._display.module_exit()
            self._initialized = False