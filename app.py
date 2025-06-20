import gradio as gr
import folium
import tempfile
from piexif import ImageIFD
from image_exif_tool import get_exif_meta_data, remove_metadata, get_gps


def extract_exif(image):
    if not image.lower().endswith((".jpg", ".jpeg", ".tif", ".tiff")):
        return "❌ Only JPEG or TIFF images are supported.", "", "", ""
    
    exif_data = get_exif_meta_data(image)
    image_info = exif_data["0th"]

    
    brand = image_info.get(ImageIFD.Make, b"").decode(errors="ignore")
    model = image_info.get(ImageIFD.Model, b"").decode(errors="ignore")
    datetime = image_info.get(ImageIFD.DateTime, b"").decode(errors="ignore")
    
    
    map_html = showup_map(image)
    
    return brand, datetime, model, map_html
    

def remove_exif(image):
    image_without_exif = remove_metadata(image)
    
    return image_without_exif
    
def showup_map(image):
    lat, lon = get_gps(image)
    if lat is None or lon is None:
        return "<p style='color:red'>No GPS data found in this image.</p>"

    m = folium.Map(location=[lat, lon], zoom_start=12)
    folium.Marker([lat, lon], popup="Image Location").add_to(m)

    return m._repr_html_()
    
    


with gr.Blocks() as demo:
    gr.Markdown("## 📷 EXIF Handler — View and Remove Photo Metadata")
    gr.Markdown("**Note:** Only `.jpg`, `.jpeg`, or `.tiff` images will work with EXIF extraction.")


    # Image input (upload or use example)
    inp = gr.Image(type='filepath', label="Upload an image")


    gr.Examples(
        examples=["data/DSCN0010.jpg","data/DSCN0040.jpg","data/jolla.jpg"],
        inputs=inp,
        label="Example Image"
    )

    # Action buttons
    with gr.Row():
        extract_button = gr.Button("🔍 Extract EXIF")
        remove_button = gr.Button("🧹 Remove EXIF")

    # EXIF display fields
    with gr.Row():
        brand = gr.Label(label='📸 Camera Brand')
        date = gr.Label(label='📅 Date Taken')
        model = gr.Label(label='📷 Camera Model')
    with gr.Row():
        map = gr.HTML(label="Map View")

    # Output image display
    output_image = gr.Image(label="🧼 Image without EXIF")

    # Button callbacks
    extract_button.click(fn=extract_exif, inputs=inp, outputs=[brand, date, model, map])
    remove_button.click(fn=remove_exif, inputs=inp, outputs=output_image)

demo.launch()