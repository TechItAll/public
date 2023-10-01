# NOTE: This is a test of a animation for deleting things!



import time
import os

class Animation():
    def delete_animation(file_name):
        animation_frames = [
            r"""
    _________________________
    |                       |
    |                       |
    |                       |
    |                       |
    |                       |
    |                       |
    |                       |
    |                       |
    |                       |
    |                       |
    |                       |
    |_______________________|""",
            r"""
    _________________________
    | \                 /   |
    |   \             /     |
    |     \         /       |
    |       \     /         |
    |         \ /           |
    |          X            |
    |         / \\          |
    |       /     \\        |
    |     /         \\      |
    |   /             \\    |
    | /                 \\  |
    |_______________________|
    """,
            r"""
    ________________________
    |                       |
    |                       |
    |                       |
    |                       |
    |                       |
    |                       |
    |                       |
    |                       |
    |                       |
    |                       |
    |                       |
    |_______________________|""",
            r"""
    _________________________
    | \                 /   |
    |   \             /     |
    |     \         /       |
    |       \     /         |
    |         \ /           |
    |          X            |
    |         / \\          |
    |       /     \\        |
    |     /         \\      |
    |   /             \\    |
    | /                 \\  |
    |_______________________|
    """,
            r"""
    _________________________
    |                       |
    |                       |
    |                       |
    |                       |
    |                       |
    |                       |
    |                       |
    |                       |
    |                       |
    |                       |
    |                       |
    |_______________________|""",
            r"""
    _________________________
    | \                 /   |
    |   \             /     |
    |     \         /       |
    |       \     /         |
    |         \ /           |
    |          X            |
    |         / \\          |
    |       /     \\        |
    |     /         \\      |
    |   /             \\    |
    | /                 \\  |
    |_______________________|
    """,
            r"""
    _________________________
    |                       |
    |                       |
    |                       |
    |                       |
    |                       |
    |                       |
    |                       |
    |                       |
    |                       |
    |                       |
    |                       |
    |_______________________|""",
            r"""
    _________________________
    | \                 /   |
    |   \             /     |
    |     \         /       |
    |       \     /         |
    |         \ /           |
    |          X            |
    |         / \\          |
    |       /     \\        |
    |     /         \\      |
    |   /             \\    |
    | /                 \\  |
    |_______________________|
    """,
        ]

        print("Deleting file: " + file_name)
        time.sleep(1)

        for frame in animation_frames:
            os.system("cls" if os.name == "nt" else "clear")  # Clear the terminal screen
            print(frame)
            time.sleep(0.3)

        time.sleep(1)
        print("File '{}' has been deleted.".format(file_name))

# Usage example
if __name__ == "__main__":
    filename_to_delete = "example.txt"  # Replace this with the file you want to delete
    Animation.delete_animation(filename_to_delete)
