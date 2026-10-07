import math
import struct
import wave

def generate_sample_audio(filename="sample_voice_intake.wav"):
    sample_rate = 16000
    duration = 4.0  # seconds
    num_samples = int(sample_rate * duration)
    
    # Generate audio pattern simulating medical intake dictation tones
    with wave.open(filename, "w") as wav_file:
        wav_file.setnchannels(1)  # Mono
        wav_file.setsampwidth(2)  # 16-bit
        wav_file.setframerate(sample_rate)
        
        frames = []
        for i in range(num_samples):
            t = float(i) / sample_rate
            # Voice frequency modulation envelope
            freq = 220 + 60 * math.sin(2 * math.pi * 3 * t) + 30 * math.sin(2 * math.pi * 7 * t)
            # Amplitude cadence mimicking words
            cadence = max(0.0, math.sin(2 * math.pi * 1.5 * t)) * (0.8 + 0.2 * math.sin(2 * math.pi * 12 * t))
            value = int(32767.0 * 0.4 * cadence * math.sin(2 * math.pi * freq * t))
            frames.append(struct.pack("<h", value))
        
        wav_file.writeframes(b"".join(frames))
    print(f"Sample voice intake audio created at: {filename}")

if __name__ == "__main__":
    generate_sample_audio()
