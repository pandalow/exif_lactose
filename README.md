# exif_lactose

A lightweight and beginner-friendly tool to extract and remove EXIF metadata from images — with a visual twist!
This project is designed as a hands-on way to get familiar with Gradio interfaces and integrating map-based visualizations via Folium.

Upload an image → View its EXIF data (camera, date, GPS) → Remove EXIF metadata → Done!

![EXIF Demo](data/image.png)

## Quick Start
1. Clone the repository
```bash
git clone https://github.com/your-username/exif_lactose.git
cd exif_lactose
```
2. Install dependencies
```bash

pip install -r requirements.txt
```
3. Run the app
```bash
python app.py
```

Then open http://127.0.0.1:7860 in your browser.

## Dependencies
See `requirements.txt` for details.
## Notes
-  Only JPEG and TIFF formats retain EXIF metadata. PNG files will not work for EXIF extraction.
-  Images shared via apps like WeChat or WhatsApp may strip EXIF data by default.

This project is part of my personal learning path in:
Gradio UI development
Handling image metadata in Python
Integrating maps with user interfaces