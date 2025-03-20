import os
from PIL import Image, ExifTags
import shutil
from pathlib import Path
import moviepy.editor as mp

def setup_image_directories():
    # Create directories for processed images
    directories = ['web', 'web/gallery', 'web/thumbnails']
    for dir in directories:
        Path(dir).mkdir(parents=True, exist_ok=True)

def fix_image_rotation(image):
    try:
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation':
                break
        exif = dict(image._getexif().items())

        if exif[orientation] == 3:
            image = image.rotate(180, expand=True)
        elif exif[orientation] == 6:
            image = image.rotate(270, expand=True)
        elif exif[orientation] == 8:
            image = image.rotate(90, expand=True)
    except (AttributeError, KeyError, IndexError):
        # No EXIF data or no orientation info
        pass
    return image

def process_image(input_path, output_path, size=(1200, 800)):
    try:
        with Image.open(input_path) as img:
            # Fix rotation based on EXIF data
            img = fix_image_rotation(img)
            
            # Convert to RGB if necessary
            if img.mode in ('RGBA', 'P'):
                img = img.convert('RGB')
            
            # Calculate aspect ratio
            aspect = img.width / img.height
            if aspect > 1:  # Landscape
                new_size = (size[0], int(size[0] / aspect))
            else:  # Portrait
                new_size = (int(size[1] * aspect), size[1])
            
            # Resize maintaining aspect ratio
            img = img.resize(new_size, Image.Resampling.LANCZOS)
            
            # Save with optimized quality
            img.save(output_path, 'JPEG', quality=85, optimize=True)
            return True
    except Exception as e:
        print(f"Error processing {input_path}: {e}")
        return False

def create_video_thumbnail(video_path, output_path):
    try:
        clip = mp.VideoFileClip(video_path)
        # Get frame at 1 second
        frame = clip.get_frame(1)
        # Save frame as image
        clip.save_frame(output_path, t=1)
        clip.close()
        return True
    except Exception as e:
        print(f"Error processing video {video_path}: {e}")
        return False

def main():
    # Source directory with original images
    source_dir = "images"
    
    setup_image_directories()
    
    # Process images
    image_files = [f for f in os.listdir(source_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    
    # Hero image (using mountain shot)
    process_image(
        os.path.join(source_dir, "IMAG0258.jpg"),
        "web/hero-bg.jpg",
        (2000, 1200)
    )
    
    # Process gallery images
    for img_file in image_files:
        if img_file.startswith('.'):  # Skip hidden files
            continue
            
        source_path = os.path.join(source_dir, img_file)
        gallery_path = f"web/gallery/{img_file}"
        thumbnail_path = f"web/thumbnails/{img_file}"
        
        process_image(source_path, gallery_path, (1200, 800))
        process_image(source_path, thumbnail_path, (400, 300))
        print(f"Processed: {img_file}")

    print("Image processing complete!")

if __name__ == "__main__":
    main() 