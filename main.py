from kittentts import KittenTTS
import sounddevice as sd
from enum import Enum


class Speakers(Enum):
    ALICE = "expr-voice-4-f"
    BOB = "expr-voice-4-m"


def speak(what: str = "this is a test", speaker: Speakers = Speakers.ALICE):
    samplerate = 24000  # samples per second

    m = KittenTTS("KittenML/kitten-tts-nano-0.1")

    audio = m.generate(f"{what}...", voice=speaker.value)

    # available_voices : [  'expr-voice-2-m', 'expr-voice-2-f', 'expr-voice-3-m', 'expr-voice-3-f',  'expr-voice-4-m', 'expr-voice-4-f', 'expr-voice-5-m', 'expr-voice-5-f' ]

    sd.play(audio, samplerate)
    sd.wait()


if __name__ == "__main__":
    speak(
        "Some men see things as they are and say why. I dream things that never were and say why not",
        speaker=Speakers.BOB,
    )
