"""Constants for the RHVoice tts service."""

CONF_FORMAT = "format"
CONF_PITCH = "pitch"
CONF_RATE = "rate"
CONF_VOICE = "voice"
CONF_VOLUME = "volume"

SUPPORTED_FORMATS = ["flac", "mp3", "opus", "wav"]
SUPPORTED_OPTIONS = [CONF_FORMAT, CONF_PITCH, CONF_RATE, CONF_VOICE, CONF_VOLUME]
SUPPORTED_LANGUAGES = {
    "cs-CZ": (
        "radek",
        "zdenek",
    ),
    "en-US": (
        "alan",
        "bdl",
        "clb",
        "evgeniy-eng",
        "lyubov",
        "slt",
    ),
    "eo": ("spomenka",),
    "es-ES": (
        "latin american spanish",
        "mateo",
    ),
    "hr-HR": (
        "karmela",
        "marija",
    ),
    "ka-GE": ("natia",),
    "ky-KG": (
        "azamat",
        "nazgul",
    ),
    "mk": (
        "kiko",
        "suze",
    ),
    "ne-NP": ("dina",),
    "pl-PL": (
        "alicja",
        "cezary",
        "magda",
        "michal",
        "natan",
    ),
    "pt-BR": ("letícia-f123",),
    "ro-RO": ("paul",),
    "ru-RU": (
        "aleksandr",
        "aleksandr-hq",
        "anna",
        "arina",
        "artemiy",
        "elena",
        "evgeniy-rus",
        "irina",
        "mikhail",
        "pavel",
        "tatiana",
        "timofey",
        "umka",
        "victoria",
        "vitaliy",
        "vitaliy-ng",
        "vsevolod",
        "yuriy",
    ),
    "sk-SK": (
        "jasietka",
        "ondro",
        "radek",
        "zdenek",
    ),
    "sq-AL": ("hana",),
    "sr": ("dragana",),
    "sr-Latn": ("dragana",),
    "tk-TM": ("dunya",),
    "tn-BW": ("dimpho",),
    "tt-RU": ("talgat",),
    "uk-UA": (
        "anatol",
        "marianna",
        "natalia",
        "volodymyr",
    ),
    "uz-UZ": (
        "dil'navoz",
        "islom",
        "sevinch",
    ),
    "vi-VN": ("vi vu",),
}
