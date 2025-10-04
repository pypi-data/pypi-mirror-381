"""Constants for the CLI module."""

CLI_CFG_FILE = ".env"
CLI_DEFAULT_ENV_VARS = {
    "FLICK_API_KEY": "flock-api-key",
    "FLICK_API_URL": "https://api.flock.com",
    "FLICK_API_VERSION": "v1",
    "FLICK_API_KEY": "flock-api-key",
    "FLICK_API_URL": "https://api.flock.com",
    "FLICK_API_VERSION": "v1",
}
CLI_DEFAULT_FOLDER = ".flock"

CLI_CREATE_AGENT = "Create an agent"
CLI_CREATE_FLOCK = "Create a new Flock"
CLI_LOAD_AGENT = "Load an agent"
CLI_LOAD_FLOCK = "Load a *.flock file"
CLI_THEME_BUILDER = "Theme builder"
CLI_LOAD_EXAMPLE = "Load a example"
CLI_SETTINGS = "Settings"
CLI_NOTES = "'Magpie' release notes"
CLI_START_WEB_SERVER = "Start web server"
CLI_REGISTRY_MANAGEMENT = "Registry management"
CLI_EXIT = "Exit"
CLI_CHOICES = [
    CLI_CREATE_AGENT,
    CLI_CREATE_FLOCK,
    CLI_LOAD_AGENT,
    CLI_LOAD_FLOCK,
    CLI_LOAD_EXAMPLE,
    CLI_THEME_BUILDER,
    CLI_REGISTRY_MANAGEMENT,
    CLI_SETTINGS,
    CLI_START_WEB_SERVER,
    CLI_EXIT,
]
