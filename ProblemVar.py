import cv2
import time
import os
import datetime
import pyaudio
import wave
import threading
import signal

CAMERAID = 0
PATH = 'problem'
SOUND_PATH = os.path.join(PATH, 'ses')
NAMING = '%Y-%m-%d--%H-%M-%S'
EXTENSION_IMG = '.jpg'
EXTENSION_SOUND = '.wav'
INTERVAL = 5
SAMPLE_RATE = 48000  # Ses örnekleme hızı
CHANNELS = 2  # Mono ses
FORMAT = pyaudio.paInt16  # Ses formatı
CHUNK_SIZE = 1024  # Ses parçası boyutu

stop_threads = False

def signal_handler(sig, frame):
    global stop_threads
    stop_threads = True
    print("Program sonlandırılıyor...")

signal.signal(signal.SIGINT, signal_handler)

#ses fonksiyonu
def capture_sound() -> None:
    if not os.path.exists(SOUND_PATH):
        os.makedirs(SOUND_PATH)

    print(f"Recording Parameters: Channels={CHANNELS}, Sample Rate={SAMPLE_RATE}, Chunk Size={CHUNK_SIZE}")


    p = pyaudio.PyAudio()

    try:
        stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=SAMPLE_RATE,
                input=True,
                input_device_index=4,  # Mikrofon cihaz ID'si
                frames_per_buffer=CHUNK_SIZE)

    except Exception as e:
        print(f"Ses cihazı başlatılamadı: {e}")
        return

    frames = []
    print("Ses kaydı başlatıldı. Çıkmak için Ctrl+C'ye basın.")

    try:
        while not stop_threads:
            data = stream.read(CHUNK_SIZE, exception_on_overflow=False)
            frames.append(data)
    except Exception as e:
        print(f"Ses kaydında hata oluştu: {e}")
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()

        sound_name = datetime.datetime.today().strftime(NAMING) + EXTENSION_SOUND
        sound_path = os.path.join(SOUND_PATH, sound_name)
        
        with wave.open(sound_path, 'wb') as wf:
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(p.get_sample_size(FORMAT))
            wf.setframerate(SAMPLE_RATE)
            wf.writeframes(b''.join(frames))
        print(f"Ses kaydı kaydedildi: {sound_path}")

#görüntü fonksiyonu
def capture_image() -> None:
    if not os.path.exists(PATH):
        os.makedirs(PATH)

    cap = cv2.VideoCapture(CAMERAID)
    ret, frame = cap.read()
    cap.release()

    if ret and frame is not None:
        image_name = datetime.datetime.today().strftime(NAMING) + EXTENSION_IMG
        cv2.imwrite(os.path.join(PATH, image_name), frame)
        print(f"Görüntü kaydedildi: {os.path.join(PATH, image_name)}")
    else:
        print("Kamera görüntüsü alınamadı.")

def start_image_capture():
    while not stop_threads:
        capture_image()
        time.sleep(INTERVAL)

def start_audio_capture():
    capture_sound()

if __name__ == "__main__":
    # Görüntü ve ses işlemleri için thread oluşturuluyor
    image_thread = threading.Thread(target=start_image_capture)
    audio_thread = threading.Thread(target=start_audio_capture)

    # Thread'ler başlatılıyor
    image_thread.start()
    audio_thread.start()

    # Thread'ler bekleniyor
    image_thread.join()
    audio_thread.join()

    print("Program sonlandırıldı.")
