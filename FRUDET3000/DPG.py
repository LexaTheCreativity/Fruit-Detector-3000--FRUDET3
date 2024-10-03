import dearpygui.dearpygui as dpg
import cv2
import numpy as np

dpg.create_context()
dpg.create_viewport(title='FRUDET3', width=1400, height=800)
dpg.setup_dearpygui()
vid = cv2.VideoCapture(0, cv2.CAP_DSHOW)


def live_cam():

    ret, frame = vid.read()
    data = np.flip(frame, 2)
    data = data.ravel()
    texture_data = np.true_divide(data, 255.0)

    with dpg.texture_registry(show=False):
        dpg.add_raw_texture(frame.shape[1], frame.shape[0], texture_data, tag="texture_tag",
                            format=dpg.mvFormat_Float_rgb)


with dpg.window(label="Live camera", width=1400, height=800):
    with dpg.table(header_row=False, row_background=False,
                   borders_innerH=True, borders_outerH=True, borders_innerV=False,
                   borders_outerV=False):
        live_cam()
        # use add_table_column to add columns to the table,
        # table columns use child slot 0
        dpg.add_table_column()
        dpg.add_table_column()

        # add_table_next_column will jump to the next row
        # once it reaches the end of the columns
        # table next column use slot 1
        for i in range(0, 1):
            with dpg.table_row():
                dpg.add_text("Fruit Detector 3000")
                for j in range(0, 1):
                    dpg.add_image("texture_tag")


dpg.show_viewport()
while dpg.is_dearpygui_running():
    ret, frame = vid.read()
    data = np.flip(frame, 2)
    data = data.ravel()
    data = np.asfarray(data, dtype='f')
    texture_data = np.true_divide(data, 255.0)
    dpg.set_value("texture_tag", texture_data)

    dpg.render_dearpygui_frame()


vid.release()

dpg.destroy_context()


def main():
    print("")


if __name__ == "__main__":
    main()