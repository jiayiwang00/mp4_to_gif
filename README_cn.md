# MP4 转 GIF 工具

简体中文 | [English](./README.md)

这个 Python 脚本可以把当前文件夹中的所有 `.mp4` 文件转换成 `.gif` 文件。

转换后的 GIF 文件会保存到一个名为 `gif/` 的文件夹中。  
如果 `gif/` 文件夹不存在，脚本会自动创建。

---

## 1. 创建虚拟环境

macOS / Linux：

```bash
python3 -m venv .venv
```

Windows：

```bash
python -m venv .venv
```

## 2. 激活虚拟环境

macOS / Linux：

```bash
source .venv/bin/activate
```

Windows PowerShell：

```bash
.venv\Scripts\Activate.ps1
```

## 3. 安装依赖

```bash
pip install --upgrade pip
pip install moviepy
```

## 4. 运行脚本

```bash
python mp4_to_gif.py
```

把你的 `.mp4` 文件放到这个文件夹里，例如：

```text
mp4_to_gif/
├── README.md
└── mp4/
    ├── video1.mp4
    └── video2.mp4
└── gif/
    ├── video1.gif
    └── video2.gif
```

---

# 5. 项目结构

```text
mp4ToGif/
├── video1.mp4
├── video2.mp4
├── convert_all_mp4_to_gif.py
├── README.md
└── gif/
    ├── video1.gif
    └── video2.gif
```