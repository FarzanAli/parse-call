from faster_whisper import WhisperModel

model_size = "large-v3"

# Run on GPU with FP16
# model = WhisperModel(model_size, device="cuda", compute_type="float16")

# or run on GPU with INT8
# model = WhisperModel(model_size, device="cuda", compute_type="int8_float16")
# or run on CPU with INT8
model = WhisperModel(model_size, device="cpu", compute_type="int8")

segments, info = model.transcribe("td.wav", beam_size=5)

print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

transcript = []
time = []

for segment in segments:
    time.append([segment.start, segment.end])
    transcript.append(segment.text)

print(transcript)

print(time)
transcript = ''.join(transcript)

print("")
print(transcript)