from vosk import Model, KaldiRecognizer
import sounddevice as sd
import queue
import sys
import json


IS_STREAM_ACTIVE = True # you can use this to dynamically pause/resume the input stream
DEVICE = 1 # set to your input device ID (try -1, 0, 1, 2...)

#### 1. Sets up streaming queue

q = queue.Queue()

def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    if IS_STREAM_ACTIVE:
        q.put(bytes(indata))


#### 2. Sets up audio input

device_info = sd.query_devices(DEVICE, "input")
samplerate = int(device_info["default_samplerate"])
model = Model(lang="en-us")  

rec = KaldiRecognizer(model, samplerate)


#### 3. Main loop

with sd.RawInputStream(samplerate=samplerate, blocksize=8000, device=DEVICE,
            dtype="int16", channels=1, callback=callback):
        print("#" * 80)
        print("Press Ctrl+C to stop the recording")
        print("#" * 80)

        while True:
            data = q.get()
            if rec.AcceptWaveform(data): # Called if the recognizer detects a complete utterance
                result = rec.Result()  # Get the result as a JSON string
                result_dict = json.loads(result)  # Parse the JSON string into a dictionary
                utterance = result_dict.get('text', '')
                print(utterance)
                