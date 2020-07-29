# HomeAssistant - RHVoice component

This is a custom component for local TTS engine [RHVoice](https://github.com/Olga-Yakovleva/RHVoice).

## Usage

1. Run [rhvoice-rest](https://hub.docker.com/r/aculeasis/rhvoice-rest/) docker container.
2. Add component to Home Assistant.
3. Add to configuration.yaml:
```yaml
tts:
  - platform: rhvoice
    host: rhvoice
    format: 'mp3'  # Optional, wav|mp3|opus|flac
    pitch: 50  # Optional, 0..100
    rate: 50  # Optional, 0..100
    voice: 'anna' # Optional
    volume: 50  # Optional, 0..100
```
[List of languages and voices.](https://github.com/Olga-Yakovleva/RHVoice/wiki/Latest-version)
