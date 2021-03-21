import pvporcupine

handle = pvporcupine.create(keywords=['picovoice'])

def get_next_audio_frame():
    pass

while True:
    keyword_index = handle.process(get_next_audio_frame())
    if keyword_index >= 0:
        print(keyword_index)
        # Insert detection event callback here
        pass