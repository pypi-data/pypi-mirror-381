#!/usr/bin/env python3
"""
Example script showing how to send audio files to the browser from the backend.
Run this script while the PyLips face server is running to test audio playback.
"""

import socketio
import time
import sys

# Connect to the PyLips server
sio = socketio.Client()

@sio.event
def connect():
    print("Connected to PyLips server")

@sio.event
def disconnect():
    print("Disconnected from PyLips server")

@sio.event
def audio_error(data):
    print(f"Audio error: {data['error']}")

@sio.event
def audio_list(data):
    print(f"Available audio files: {data['files']}")

def send_audio_to_browser(filename, target_face='default'):
    """Send an audio file to the browser for playback"""
    print(f"Sending audio file '{filename}' to face '{target_face}'")

    

    sio.emit('play_audio_file', {
        'filename': filename,
        'name': target_face
    })

def get_audio_list():
    """Request list of available audio files"""
    print("Requesting audio file list...")
    sio.emit('request_audio_list')

if __name__ == '__main__':
    # Connect to the server
    try:
        sio.connect('http://localhost:8000')
    except Exception as e:
        print(f"Failed to connect to server: {e}")
        print("Make sure the PyLips face server is running (python -m pylips.face.start)")
        sys.exit(1)

    # Wait a moment for connection to establish
    time.sleep(1)

    # Example usage
    print("\n=== PyLips Audio Test ===")
    
    # Get list of available files
    get_audio_list()
    time.sleep(1)
    
    # Try to play some common audio files
    test_files = [
        'default_output.wav',
        'com.apple.speech.synthesis.voice.Bubbles_output.wav',
        'com.apple.voice.premium.en-US.Zoe_output.wav'
    ]
    
    for filename in test_files:
        print(f"\nTrying to play: {filename}")
        send_audio_to_browser(filename)
        time.sleep(2)  # Wait between audio files
    
    # Interactive mode
    print("\n=== Interactive Mode ===")
    print("Enter audio filenames to play them, or 'quit' to exit:")
    
    while True:
        try:
            filename = input("Audio filename (or 'list' for available files, 'quit' to exit): ").strip()
            
            if filename.lower() == 'quit':
                break
            elif filename.lower() == 'list':
                get_audio_list()
            elif filename:
                send_audio_to_browser(filename)
            
        except KeyboardInterrupt:
            break
    
    print("\nDisconnecting...")
    sio.disconnect()