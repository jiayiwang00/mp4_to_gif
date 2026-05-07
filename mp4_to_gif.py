from pathlib import Path
from moviepy import VideoFileClip


# ====== Editable parameters ======
START = 0        # Start time in seconds
END = None      # End time in seconds; use None to convert the full video
FPS = 10        # GIF frame rate; lower FPS means smaller file size
WIDTH = 480     # GIF width; smaller width means smaller file size
INPUT_DIR = "mp4"
OUTPUT_DIR = "gif"
# ================================


def mp4_to_gif(input_file: Path, output_file: Path):
    clip = None

    try:
        print(f"Processing: {input_file.name}")

        clip = VideoFileClip(str(input_file))

        # Trim video clip
        if END is not None:
            clip = clip.subclipped(START, END)
        else:
            clip = clip.subclipped(START)

        # Resize video
        clip = clip.resized(width=WIDTH)

        # Export as GIF
        clip.write_gif(str(output_file), fps=FPS)

        print(f"Done: {output_file}")

    except Exception as e:
        print(f"Failed to convert: {input_file.name}")
        print(f"Reason: {e}")

    finally:
        if clip is not None:
            clip.close()


def main():
    current_folder = Path(".")
    input_folder = current_folder / INPUT_DIR
    output_folder = current_folder / OUTPUT_DIR

    if not input_folder.is_dir():
        print(f"Input folder not found: {input_folder}")
        return

    output_folder.mkdir(exist_ok=True)

    # Find all mp4 / MP4 files in the input folder
    mp4_files = [
        file
        for file in input_folder.iterdir()
        if file.is_file() and file.suffix.lower() == ".mp4"
    ]

    if not mp4_files:
        print(f"No .mp4 files found in {input_folder}")
        return

    print(f"Found {len(mp4_files)} MP4 file(s) in {input_folder}")

    for mp4_file in mp4_files:
        gif_file = output_folder / f"{mp4_file.stem}.gif"
        mp4_to_gif(mp4_file, gif_file)

    print("All conversions completed")


if __name__ == "__main__":
    main()
