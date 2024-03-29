from yolov3.yolo import object_tracking_table
import time

if __name__ == "__main__":
    INPUT_FILE = 'WalkByShop1cor-cut.mp4'
    output_name = INPUT_FILE.split('.')[0]
    OUTPUT_FILE = output_name + '-output.avi'

    start_time = time.time()
    frame = object_tracking_table(
        INPUT_FILE, # Входное видео
        OUTPUT_FILE, # Видео с разметкой
        show_output_image=False, # Отображение каждого фрейма с детекцией
        save_csv=True # CSV-файл сохраняется в папку csv-files
    )

    print("--- %s seconds ---" % (time.time() - start_time))
