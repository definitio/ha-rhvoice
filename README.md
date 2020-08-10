# RHVoice component for Home Assistant

[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/custom-components/hacs)

The `rhvoice` integration uses [RHVoice](https://github.com/Olga-Yakovleva/RHVoice) Text-to-Speech engine to read a text with natural sounding voices.

## Usage

1. Run [rhvoice-rest](https://hub.docker.com/r/aculeasis/rhvoice-rest/) Docker container.
2. Install the integration to Home Assistant: use [HACS](https://hacs.xyz/) or copy the contents of `custom_components/rhvoice/` to `<your config dir>/custom_components/rhvoice/`.
3. Add to configuration.yaml:

```yaml
tts:
  - platform: rhvoice
    host: <server hostname or IP address>
    port: 8080 # Optional
    format: 'mp3' # Optional, wav|mp3|opus|flac
    pitch: 50 # Optional, 0..100
    rate: 50 # Optional, 0..100
    voice: 'anna' # Optional, default is 'anna' (russian)
    volume: 50 # Optional, 0..100
```

4. Restart Home Assistant.

[List of languages and voices.](https://github.com/Olga-Yakovleva/RHVoice/wiki/Latest-version)
