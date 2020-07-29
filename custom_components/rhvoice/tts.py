"""Support for the RHVoice tts service."""
import logging
from asyncio import TimeoutError as aioTimeoutError

import voluptuous as vol

import async_timeout
from aiohttp import ClientError
from homeassistant.components.tts import PLATFORM_SCHEMA, Provider
from homeassistant.const import CONF_HOST, CONF_PORT, CONF_TIMEOUT
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.aiohttp_client import async_get_clientsession

_LOGGER = logging.getLogger(__name__)

CONF_FORMAT = 'format'
CONF_PITCH = 'pitch'
CONF_RATE = 'rate'
CONF_VOICE = 'voice'
CONF_VOLUME = 'volume'

SUPPORT_LANGUAGES = ['en-US', 'ru-RU']
SUPPORTED_OPTIONS = [CONF_VOICE, CONF_FORMAT, CONF_RATE, CONF_PITCH, CONF_VOLUME]

# Supported languages and voices: https://github.com/Olga-Yakovleva/RHVoice/wiki/Latest-version
DEFAULT_FORMAT = 'mp3'  # wav|mp3|opus|flac
DEFAULT_LANG = 'ru-RU'
DEFAULT_PITCH = 50  # 0..100
DEFAULT_PORT = 8080
DEFAULT_RATE = 50  # 0..100
DEFAULT_VOICE = 'anna'
DEFAULT_VOLUME = 50  # 0..100


PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_HOST): cv.string,
        vol.Optional(CONF_PORT, default=DEFAULT_PORT): cv.port,
        vol.Optional(CONF_FORMAT, default=DEFAULT_FORMAT): cv.string,
        vol.Optional(CONF_PITCH, default=DEFAULT_PITCH): cv.positive_int,
        vol.Optional(CONF_RATE, default=DEFAULT_RATE): cv.positive_int,
        vol.Optional(CONF_VOICE, default=DEFAULT_VOICE): cv.string,
        vol.Optional(CONF_VOLUME, default=DEFAULT_VOLUME): cv.positive_int,
    }
)


async def async_get_engine(hass, config, discovery_info=None):
    """Set up RHVoice speech component."""
    return RHVoiceProvider(hass, config)


class RHVoiceProvider(Provider):
    """RHVoice speech api provider."""

    def __init__(self, hass, conf):
        """Init RHVoice TTS service."""
        self.hass = hass
        self._url = f'http://{conf.get(CONF_HOST)}:{conf.get(CONF_PORT)}/say'
        self._language = DEFAULT_LANG
        self._codec = conf.get(CONF_FORMAT)
        self._pitch = conf.get(CONF_PITCH)
        self._rate = conf.get(CONF_RATE)
        self._voice = conf.get(CONF_VOICE)
        self._volume = conf.get(CONF_VOLUME)
        self.name = 'RHVoice'
        self._timeout = conf.get(CONF_TIMEOUT)

    @property
    def default_language(self):
        """Return the default language."""
        return self._language

    @property
    def supported_languages(self):
        """Return list of supported languages."""
        return SUPPORT_LANGUAGES

    @property
    def supported_options(self):
        """Return list of supported options."""
        return SUPPORTED_OPTIONS

    async def async_get_tts_audio(self, message, language, options=None):
        """Load TTS from RHVoice."""
        websession = async_get_clientsession(self.hass)
        options = options or {}

        try:
            with async_timeout.timeout(self._timeout):
                url_param = {
                    'text': message,
                    'voice': self._voice,
                    'format': self._codec,
                    'rate': self._rate,
                    'pitch': self._pitch,
                    'volume': self._volume,
                }

                request = await websession.get(self._url, params=url_param)

                if request.status != 200:
                    _LOGGER.error(
                        "Error %d on load URL %s", request.status, request.url
                    )
                    return None, None
                data = await request.read()

        except (aioTimeoutError, ClientError):
            _LOGGER.error("Timeout for RHVoice API")
            return None, None

        return self._codec, data
