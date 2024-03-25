import os
import time
import datetime
import picamera

def record_video(duration, output_folder):
    while True:
        with picamera.PiCamera() as camera:
            camera.resolution = (640, 480)
            camera.start_preview()
            time.sleep(2)  # Allow camera to warm up
            start_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            output_file = os.path.join(output_folder, f"video_{start_time}.h264")
            camera.start_recording(output_file)
            camera.wait_recording(duration)
            camera.stop_recording()
            camera.stop_preview()
            print(f"Video recorded: {output_file}")
        time.sleep(1)  # Wait for 1 second before starting the next recording

def main():
    # Create folder with today's date if not exists
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    output_folder = os.path.join(os.getcwd(), today)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Record videos continuously
    record_duration = 30
    record_video(record_duration, output_folder)

if __name__ == "__main__":
    main()
