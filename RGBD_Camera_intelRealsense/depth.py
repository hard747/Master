import subprocess

def show_depth_image(depth_image_path):
    # Usar xdg-open para abrir la imagen con el visor predeterminado
    subprocess.run(["xdg-open", depth_image_path])

if __name__ == '__main__':
    show_depth_image('depth_image.jpg')
