from pathlib import Path

# URLs
FIC_LOGIN = "https://familyinfocenter.brighthorizons.com/okta/login?mode=Okta"
BRIGHT_DAY_HOME = "https://mybrightday.brighthorizons.com/dashboard/parents.html"
PROFILE_API_URL = "https://mybrightday.brighthorizons.com/api/v2/user/profile"

# Configuration
STATE_FILE = Path("bh_state.json")
HEADLESS = True  # set False to watch

# Selectors
LOGIN_SELECTOR = [
    "button:has-text('Log In')",
]

OKTA_USERNAME_SEL = [
    "#username",
    "input[name='username']",
]

OKTA_PASSWORD_SEL = [
    "#password",
    "input[name='password']",
    "input[type='password']",
]

COOKIE_ACCEPT_SEL = [
    "#onetrust-accept-btn-handler",
]
