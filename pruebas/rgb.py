import subprocess

def show_rgb_image(rgb_image_path):
    # Usar xdg-open para abrir la imagen con el visor predeterminado
    subprocess.run(["xdg-open", rgb_image_path])

if __name__ == '__main__':
    show_rgb_image('rgb_image.jpg')

