from kittentts import KittenTTS
import sounddevice as sd
from enum import Enum
import soundfile as sf


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

    sf.write("output.wav", audio, samplerate)


if __name__ == "__main__":
    speak(
        """
		God, what have you done?,
		You're a pink pony girl,
		And you dance at the club,
		Oh mama, I'm just having fun,
		On the stage in my heels,
		It's where I belong down at the Pink Pony Club.
		""",
        speaker=Speakers.ALICE,
    )
