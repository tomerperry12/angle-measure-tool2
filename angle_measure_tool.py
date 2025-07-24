import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from tkinter import Tk, filedialog
from math import atan2, degrees

root = Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select an image",
    filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")]
)

if not file_path:
    raise SystemExit("No image selected.")

image = mpimg.imread(file_path)
clicked_points = []
fig, ax = plt.subplots()
ax.imshow(image)
ax.set_title("Click 4 points: A, B (line 1), C, D (line 2)")

def onclick(event):
    if event.inaxes:
        clicked_points.append((event.xdata, event.ydata))
        ax.plot(event.xdata, event.ydata, 'ro')
        fig.canvas.draw()

        if len(clicked_points) == 4:
            angle = calculate_angle_between_lines(
                clicked_points[0], clicked_points[1],
                clicked_points[2], clicked_points[3]
            )
            ax.plot([clicked_points[0][0], clicked_points[1][0]],
                    [clicked_points[0][1], clicked_points[1][1]], 'b-')
            ax.plot([clicked_points[2][0], clicked_points[3][0]],
                    [clicked_points[2][1], clicked_points[3][1]], 'g-')
            ax.set_title(f"Angle between AB and CD = {angle:.2f}°")
            fig.canvas.draw()

def calculate_angle_between_lines(a, b, c, d):
    v1 = (b[0] - a[0], b[1] - a[1])
    v2 = (d[0] - c[0], d[1] - c[1])
    angle1 = atan2(v1[1], v1[0])
    angle2 = atan2(v2[1], v2[0])
    angle = degrees(abs(angle1 - angle2))
    if angle > 180:
        angle = 360 - angle
    return angle

fig.canvas.mpl_connect('button_press_event', onclick)
plt.axis('on')
plt.show()
