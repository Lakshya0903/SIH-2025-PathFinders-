import whisper

INPUT_FILE = "recording.mp3"
OUTPUT_FILE = "transcript.txt"

# Load Whisper model
model = whisper.load_model("medium")

# Transcribe
result = model.transcribe(
    INPUT_FILE,
        language="en",
            fp16=False
            )


            def format_timestamp(seconds):
                hours = int(seconds // 3600)
                    minutes = int((seconds % 3600) // 60)
                        seconds_int = int(seconds % 60)

                            return f"{hours:02d}:{minutes:02d}:{seconds_int:02d}"


                            # Save timestamped transcript as TXT
                            with open(OUTPUT_FILE, "w", encoding="utf-8") as f:

                                for segment in result["segments"]:

                                        start = format_timestamp(segment["start"])
                                                end = format_timestamp(segment["end"])
                                                        text = segment["text"].strip()

                                                                f.write(f"[{start} - {end}] {text}\n")


                                                                print(f"Done! Transcript saved to {OUTPUT_FILE}")