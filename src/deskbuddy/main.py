import time

from deskbuddy.display.canvas import create_idle_face
from deskbuddy.display.driver import DisplayDriver


def main() -> None:
    display = DisplayDriver()

    try:
        print("Initializing DeskBuddy display...")
        display.initialize()

        face = create_idle_face()
        display.show(face)

        print("DeskBuddy is awake. Press Ctrl+C to exit.")

        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nShutting down DeskBuddy...")

    finally:
        display.clear()
        display.cleanup()


if __name__ == "__main__":
    main()