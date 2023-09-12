# txt2imgconverter

Convert your text files or command outputs to image formats with ease.

将您的文本文件或命令输出轻松转换为图像格式。

## Features 特点

- Convert large text files into multiple images based on content.
  
  根据内容将大型文本文件转换为多个图像。

- Support custom image sizes.

  支持自定义图像尺寸。

- Works seamlessly for Linux command outputs redirected to text.

  无缝支持重定向到文本的Linux命令输出。

## Installation 安装

### Dependencies 依赖

To run the script, you need to have the following Python libraries:

要运行此脚本，您需要以下Python库：

```
Pillow
```

You can install them using pip:

您可以使用pip安装它们：

```bash
pip3 install Pillow
```

## Usage 使用方法

```bash
python3.6 txt2imgconverter.py -f your_text_file.txt output_image_name.png -font your_font_path.ttf -size font_size
```

Replace `your_text_file.txt`, `output_image_name.png`, `your_font_path.ttf`, and `font_size` with your actual values.

请将`your_text_file.txt`、`output_image_name.png`、`your_font_path.ttf`和`font_size`替换为您的实际值。

## Example 示例

### Scenario 场景

You want to capture the detailed listing of files and directories in your current Linux directory using `ls -lh` and convert the output to an image.


您希望使用`ls -lh`捕获当前Linux目录中的文件和目录的详细列表，并将输出转换为图像。

### Commands 命令

1. First, redirect the output of `ls -lh` to a file:

   首先，将`ls -lh`的输出重定向到文件：

   ```bash
   ls -lh > listing.txt
   ```

2. Then, use the `txt2imgconverter.py` script to convert this file to an image:

   然后，使用`txt2imgconverter.py`脚本将此文件转换为图像：

   ```bash
   python3 txt2imgconverter.py -f listing.txt listing_output.png
   ```

After executing the above commands, you'll have an image named `listing_output.png` containing the detailed file and directory listing from the `ls -lh` command.

执行上述命令后，您将拥有一个名为`listing_output.png`的图像，其中包含来自`ls -lh`命令的文件和目录的详细列表。
![listing_output](https://github.com/wangdaming261/txt2imgconverter/assets/142304595/6615efd3-76a8-462f-b3a4-dc002db17da4)

## 为什么要写此脚本
有时候巡检，需要在word上把命令执行后的结果截图粘上去。每次都很麻烦，所以就用ChatGPT写了个脚本。



