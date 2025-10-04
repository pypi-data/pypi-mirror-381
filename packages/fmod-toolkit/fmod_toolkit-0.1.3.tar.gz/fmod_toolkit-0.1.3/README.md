# fmod_toolkit

`fmod_toolkit` is a lightweight Python package designed to extract and export audio from FMOD files to WAV format.
It includes pre-bundled FMOD libraries for Windows, macOS, and Linux, enabling seamless cross-platform usage without manual library installation.

The libraries shipped with the package are FMOD Engine 2.00.10,
which is one of the last versions that used u16 instead of f32 for sampling.

The linux libraries have their executable stack flag cleared.
(``execstack -c libfmod.so``)

## usage

FSB files can be loaded, RIFF based ``.bank`` files fail at the moment.
It's possible to use a different FMOD library by setting the environment variable ``PYFMODEX_DLL_PATH``.
This is necessary on platforms this package doesn't ship FMOD libraries for.

```py
from fmod_toolkit import raw_to_wav

# fsb_data: bytes containing the FMOD sound bank (FSB) file
fsb_data: bytes = ...  # Load your FSB file data here
# fsb_basename: base name for output WAV files (e.g., "soundbank")
fsb_basename: str = "soundbank"
# channels: number of audio channels (e.g., 2 for stereo)
channels: int = 2
# sample_rate: desired output sample rate (e.g., 44100 Hz)
sample_rate: int = 44100

# Convert FSB data to WAV files
for filename, filedata in raw_to_wav(fsb_data, fsb_basename, channels, sample_rate):
    # Save each WAV file to disk
    with open(filename, "wb") as f:
        f.write(filedata)
```
