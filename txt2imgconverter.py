import os
import argparse
from PIL import Image, ImageDraw, ImageFont

def txt_to_image(txt_file, output_prefix, output_extension, font_path="SourceHanSansCN-Normal.otf", font_size=15, custom_width=None, custom_height=None):
    try:
        with open(txt_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        font = ImageFont.truetype(font_path, font_size)
        left_margin = 50
        max_image_height = custom_height if custom_height else 1500
        y = 0
        current_image_lines = []
        image_count = 0

        for line in lines:
            line = line.rstrip()
            _, line_height = font.getsize(line)

            if y + line_height > max_image_height:
                image_count += 1
                max_width = custom_width if custom_width else max([font.getsize(l)[0] for l in current_image_lines]) + left_margin
                image = Image.new("RGB", (max_width, y), "white")
                draw = ImageDraw.Draw(image)
                y_offset = 0
                for l in current_image_lines:
                    draw.text((left_margin, y_offset), l, font=font, fill="black")
                    _, lh = font.getsize(l)
                    y_offset += lh
                dpi_value = 300
                
                if image_count == 1 and len(lines) == len(current_image_lines):
                    output_filename = f"{output_prefix}.{output_extension}"
                else:
                    output_filename = f"{output_prefix}_{image_count}.{output_extension}"

                image.save(output_filename, dpi=(dpi_value, dpi_value))
                
                y = 0
                current_image_lines = []

            current_image_lines.append(line)
            y += line_height

        if current_image_lines:
            image_count += 1
            max_width = custom_width if custom_width else max([font.getsize(l)[0] for l in current_image_lines]) + left_margin
            image = Image.new("RGB", (max_width, y), "white")
            draw = ImageDraw.Draw(image)
            y_offset = 0
            for l in current_image_lines:
                draw.text((left_margin, y_offset), l, font=font, fill="black")
                _, lh = font.getsize(l)
                y_offset += lh
            dpi_value = 300
            if image_count == 1 and len(lines) == len(current_image_lines):
                output_filename = f"{output_prefix}.{output_extension}"
            else:
                output_filename = f"{output_prefix}_{image_count}.{output_extension}"

            image.save(output_filename, dpi=(dpi_value, dpi_value))

    except Exception as e:
        print(f"An error occurred: {e}")

def estimate_image_count(lines, font, max_image_height):
    total_height = sum([font.getsize(line.rstrip())[1] for line in lines])
    return total_height // max_image_height + (total_height % max_image_height > 0)

def main():
    parser = argparse.ArgumentParser(description="Convert txt to image with content awareness.")
    parser.add_argument("-f", "--file", required=True, help="Path to the text file.")
    parser.add_argument("output", nargs="?", default="image.png", help="Output image file name with extension (e.g., image.png).")
    parser.add_argument("-font", "--font_path", default="SourceHanSansCN-Normal.otf", help="Path to the font file.")
    parser.add_argument("-size", "--font_size", type=int, default=15, help="Font size.")
    parser.add_argument("--width", type=int, help="Custom width for the image.")
    parser.add_argument("--height", type=int, help="Custom height for the image.")
    args = parser.parse_args()

    SUPPORTED_FORMATS = ["png", "jpg", "jpeg", "bmp", "tiff"]
    output_extension = os.path.splitext(args.output)[1][1:]
    if output_extension not in SUPPORTED_FORMATS:
        print(f"Error: Unsupported image format '{output_extension}'. Supported formats are: {', '.join(SUPPORTED_FORMATS)}")
        return
    output_prefix = os.path.splitext(args.output)[0]

    with open(args.file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    font = ImageFont.truetype(args.font_path, args.font_size)
    estimated_count = estimate_image_count(lines, font, args.height if args.height else 1500)
    if estimated_count > 2:
        print(f"Warning: Your text might be split into {estimated_count} images.")
        proceed = input("Do you wish to proceed? (yes/no): ").strip().lower()
        if proceed != "yes":
            print("Aborted by user.")
            return

    txt_to_image(args.file, output_prefix, output_extension, args.font_path, args.font_size, args.width, args.height)

if __name__ == "__main__":
    main()

