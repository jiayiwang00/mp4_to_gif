from pathlib import Path
from moviepy import VideoFileClip


# ====== 可以修改的参数 ======
START = 0        # 从第几秒开始
END = None          # 到第几秒结束；如果想转换完整视频，改成 None
FPS = 10         # GIF 帧率，越低文件越小
WIDTH = 480      # GIF 宽度，越小文件越小
OUTPUT_DIR = "gif"
# ==========================


def mp4_to_gif(input_file: Path, output_file: Path):
    """
    把单个 MP4 文件转换成 GIF
    """

    clip = None

    try:
        print(f"正在处理: {input_file.name}")

        clip = VideoFileClip(str(input_file))

        # 截取片段
        if END is not None:
            clip = clip.subclipped(START, END)
        else:
            clip = clip.subclipped(START)

        # 调整大小
        clip = clip.resized(width=WIDTH)

        # 输出 GIF
        clip.write_gif(str(output_file), fps=FPS)

        print(f"完成: {output_file}")

    except Exception as e:
        print(f"转换失败: {input_file.name}")
        print(f"原因: {e}")

    finally:
        if clip is not None:
            clip.close()


def main():
    current_folder = Path(".")
    output_folder = current_folder / OUTPUT_DIR

    # 如果 gif 文件夹不存在，就创建
    output_folder.mkdir(exist_ok=True)

    # 找到当前文件夹下所有 mp4 / MP4 文件
    mp4_files = [
        file
        for file in current_folder.iterdir()
        if file.is_file() and file.suffix.lower() == ".mp4"
    ]

    if not mp4_files:
        print("当前文件夹没有找到 .mp4 文件")
        return

    print(f"找到 {len(mp4_files)} 个 MP4 文件")

    for mp4_file in mp4_files:
        gif_file = output_folder / f"{mp4_file.stem}.gif"
        mp4_to_gif(mp4_file, gif_file)

    print("全部转换完成")


if __name__ == "__main__":
    main()