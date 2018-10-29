# Location-Assisted authentication in home assistants
Currently, created an enrollment for a single user and have a recorded voice sample for voice verification
**audioFileGeneration.py** records the voice sample using pyaudio and stores it as a `wav` file (make sure to rename the voice sample being generated)
**auth.py** - checks if the audio file provided belongs to the enrolled user or not - returns a JSON object with the result.
