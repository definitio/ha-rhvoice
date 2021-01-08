# RHVoice component for Home Assistant

[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/custom-components/hacs)

The `rhvoice` integration uses [RHVoice](https://github.com/Olga-Yakovleva/RHVoice) Text-to-Speech (TTS) engine to read a text with natural sounding voices.

## Installation

1. Run [rhvoice-rest](https://hub.docker.com/r/aculeasis/rhvoice-rest/) Docker container.
2. Install the integration to Home Assistant: use [HACS](https://hacs.xyz/) or copy the contents of `custom_components/rhvoice/` to `<your config dir>/custom_components/rhvoice/`.
3. Configure in the Home Assistant `configuration.yaml` (See the [Configuration](#configuration) and [Configuration Options](#configuration-options) sections below)
4. Restart Home Assistant.

## <a name="configuration"></a> Configuration

To enable text-to-speech with RHVoice, add at a minimum the following lines to your Home Assistant's `configuration.yaml` file:

```yaml
tts:
  - platform: rhvoice
    host: <server hostname, domain name or IP address>
    port: 8080
```

Full configuration example:

```yaml
tts:
  - platform: rhvoice
    host: <server hostname or IP address>
    port: 8080
    format: 'mp3'
    pitch: 50
    rate: 50
    voice: 'anna'
    volume: 50
```

## <a name="configuration-options"></a> Configuration Options

- **host:** *(string) (Required)*

  This is the hostname, domain name or IP address that the `rhvoice-rest` container can be reached at. If you use domain name that is reachable on the Internet for Home Assistant, enter that here.

- **port:** *(string) (Optional)*

  This is the port that the rhvoice-rest container can be reached at.

    *Default value: `8080`*

- **ssl:** *(boolean) (Optional)*

  Use HTTPS instead of HTTP to connect.

    *Default value: `false`*

- **verify_ssl:** *(boolean) (Optional)*

  Enable or disable SSL certificate verification. Set to false if you have a self-signed SSL certificate and haven't installed the CA certificate to enable verification.

    *Default value: `true`*

- **format:** *(string) (Optional)*

  This is the file format used for the TTS files created.

    *Default value: `mp3`*

    *Allowed values: `wav|mp3|opus|flac`*

- **pitch:** *(string) (Optional)*

    This adjust the sound frequency of the TTS voice, lower or higher.

    *Default value: `50`*

    *Allowed values: `0 to 100`*

- **rate:** *(string) (Optional)*

    This adjust the talking speed of the TTS voice, slower or faster.

    *Default value: `50`*

    *Allowed values: `0 to 100`*

- **voice:** *(string) (Optional)*

    This is the voice that is used to create the TTS files. Voices are connected with a language. For best results select a voice for the text language you will use.

    *Default value: `anna` (russian)*

    *Allowed values:*

    | Voices                                           | Language             |
    |--------------------------------------------------|----------------------|
    | `alan`, `bdl`, `clb`, `slt`                      | American English     |
    | `spomenka`                                       | Esperanto            |
    | `natia`                                          | Georgian             |
    | `azamat`, `nazgul`                               | Kyrgyz               |
    | `letícia-f123`                                   | Brazilian Portuguese |
    | `aleksandr`, `artemiy`, `anna`, `elena`, `irina` | Russian              |
    | `talgat`                                         | Tatar                |
    | `anatol`, `natalia`                              | Ukrainian            |

- **volume:** *(string) (Optional)*

    This adjusts the volume of the voice in TTS files created, softer or louder.

    *Default value: `50`*

    *Allowed values: `0 to 100`*
