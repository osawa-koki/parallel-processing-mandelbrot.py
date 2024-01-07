import concurrent.futures

from PIL import Image


def multi_thread():
    width, height = 1024, 1024
    x_min, x_max = -2.5, 1.5
    y_min, y_max = -2.0, 2.0

    max_iter = 256
    threshold = 50

    image = Image.new("RGB", (width, height))

    def mandelbrot(x, y):
        c_im = y_min + (y_max - y_min) * y / height
        c_re = x_min + (x_max - x_min) * x / width

        z_re = c_re
        z_im = c_im

        is_inside = True
        iter = 0

        while iter < max_iter:
            z_re2 = z_re * z_re
            z_im2 = z_im * z_im

            if z_re2 + z_im2 > threshold * threshold:
                is_inside = False
                break

            z_im = 2.0 * z_re * z_im + c_im
            z_re = z_re2 - z_im2 + c_re

            iter += 1

        if is_inside:
            return (x, y, (0, 0, 0))
        else:
            color = iter * 16 % 256
            return (x, y, (color, color, color))

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(
            lambda x: mandelbrot(*x),
            [(x, y) for y in range(height) for x in range(width)],
        )

        for result in results:
            image.putpixel(result[:2], result[2])

    image.save("mandelbrot-multi_thread.png")
