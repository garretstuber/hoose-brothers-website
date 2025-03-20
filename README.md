# Hoose Brothers Fishing Club Website

A beautiful website showcasing the Hoose Brothers Fishing Club's adventures and memories.

## Features

- Responsive design
- Image gallery with lightbox
- Video content
- Mobile-friendly interface

## Local Development

To run the website locally:

1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Process images:
   ```bash
   python3 process_images.py
   ```

3. Start the server:
   ```bash
   python3 serve.py
   ```

4. Visit `http://localhost:8000` in your browser

## Image Processing

The website includes an image processing script that:
- Creates optimized versions of images
- Generates thumbnails
- Handles image rotation based on EXIF data
- Processes video thumbnails

## Deployment

This website is deployed using GitHub Pages. Visit [https://garretstuber.github.io/hoose-brothers-website/](https://garretstuber.github.io/hoose-brothers-website/) to view it. 