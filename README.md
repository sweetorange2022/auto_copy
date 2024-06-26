
# <center>自动复制工具
<br>
这是一个在 Windows 上用于自动复制选中文本到剪贴板的小工具。该工具还允许通过右键单击粘贴剪贴板内容。

## 功能

- 当使用鼠标选中文本时，自动将文本复制到剪贴板。
- 使用 `Ctrl+A` 选中文本时，自动将文本复制到剪贴板。
- 右键单击粘贴剪贴板内容。

## 需求

- Python 3.x
- `pyautogui` 库
- `clipboard` 库
- `pynput` 库

## 安装

1. **克隆仓库**：

    ```bash
    git clone https://github.com/sweetorange2022/auto_copy.git
    cd auto-copy-tool
    ```

2. **安装所需库**：

    ```bash
    pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
    ```

    或单独安装它们：

    ```bash
    pip install pyautogui clipboard pynput -i https://pypi.tuna.tsinghua.edu.cn/simple
    ```

## 使用

1. **运行脚本**：

    ```bash
    python auto_copy.py
    ```

2. **如何工作**：
    - **左键单击** 选中文本，文本将自动复制到剪贴板。
    - **Ctrl+A** 选中文本，文本将自动复制到剪贴板。
    - **右键单击** 将剪贴板内容粘贴到光标位置。

## 构建可执行文件

你可以使用 PyInstaller 将此脚本转换为可执行文件。

1. **安装 PyInstaller**：

    ```bash
    pip install pyinstaller -i https://pypi.tuna.tsinghua.edu.cn/simple
    ```

2. **构建可执行文件**：

    ```bash
    pyinstaller --onefile auto_copy.py
    ```

3. **查找可执行文件**：
    可执行文件将位于 `dist` 目录中。

##
  或者你也可以直接使用这个链接里的 Release : [auto_copy](https://github.com/sweetorange2022/auto_copy/releases/tag/A-auto-copy-tool-v1.0.0)
  下载后双击可以直接使用

## 灵感来源：
- 在使用Mobaxterm时，我注意到其软件中具备选中即自动复制和右键直接粘贴的功能。但是，这种选中自动复制的功能仅在软件内部有效。
- 由于这一功能极为便捷，我经常在软件外不自觉地尝试进行选中即复制的操作，然后意识到选中自动复制的功能仅在软件内部有效。
- 因此，我萌生了开发一个工具软件的想法，使整个系统都能实现选中即复制和右键即粘贴的功能。

## 贡献

欢迎贡献！请随时提交 Pull Request。

<hr>
<br>
<br>

# English version ：
<br>

# Auto Copy Tool

This is a simple tool for automatically copying selected text to the clipboard on Windows. The tool also allows you to paste the clipboard content by right-clicking.

## Features

- Automatically copy text to the clipboard when selected using the mouse.
- Copy text to the clipboard when selected using `Ctrl+A`.
- Paste clipboard content by right-clicking.

## Requirements

- Python 3.x
- `pyautogui` library
- `clipboard` library
- `pynput` library

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/sweetorange2022/auto_copy.git
    cd auto-copy-tool
    ```

2. **Install the required libraries**:

    ```bash
    pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
    ```

    Or install them individually:

    ```bash
    pip install pyautogui clipboard pynput -i https://pypi.tuna.tsinghua.edu.cn/simple
    ```

## Usage

1. **Run the script**:

    ```bash
    python auto_copy.py
    ```

2. **How it works**:
    - **Left-click** to select text, and it will be automatically copied to the clipboard.
    - **Ctrl+A** to select all text, and it will be automatically copied to the clipboard.
    - **Right-click** to paste the clipboard content at the cursor position.

## Building an Executable

You can convert this script into an executable file using PyInstaller.

1. **Install PyInstaller**:

    ```bash
    pip install pyinstaller -i https://pypi.tuna.tsinghua.edu.cn/simple
    ```

2. **Build the executable**:

    ```bash
    pyinstaller --onefile auto_copy.py
    ```

3. **Find the executable**:
    The executable will be located in the `dist` directory.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.




