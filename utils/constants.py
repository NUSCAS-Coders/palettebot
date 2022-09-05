import os
COMMAND_PREFIX = "> "
DISCORD_CHANNEL_ART_GALLERY = "art-gallery"
DISCORD_CHANNEL_WAIFU_WARS = "waifu-husbando-war"
DIR_OUTPUT = os.path.join(os.getcwd(), "io")
DISCORD_MESSAGES_LIMIT = 500
NOT_APPROVE_SIGN = "❎"
APPROVE_SIGN = "✅"
SET_APPROVE_SIGN = "☑️"
WAIFUWARS_ATTACK_SIGN = "🗡️"
WAIFUWARS_ATTACKED_SIGN = "🚑"
WAIFUWARS_CONCEDE_SIGN = "🏳️"
EXTRAVAGANZA_ROLE = 'Extravaganza 2022 Participant'
MEMBER_ROLE = 'Member'
EXTRAVAGANZA_INVITE_LINK = 'ddekPqAckv'

# Rep Tracker
DRIVE__PALETTE_REP_TRACKER = "1KJjLSjJFKaplcT_Asx3Ftd2VCZHtAk00"

# Image paths
DIR_IMG = os.path.join(os.getcwd(), "assets", "images")
DIR_IMG_BIRTHDAY = os.path.join(DIR_IMG, "birthday")
DIR_IMG_PALETTOBER = os.path.join(DIR_IMG, "palettober")
PATH_IMG_BIRTHDAY = os.path.join(DIR_IMG_BIRTHDAY, "cake_day.gif") 
PATH_IMG_BIRTHDAY_1WEEK = os.path.join(DIR_IMG_BIRTHDAY, "cake_is_a_lie.jpg")
PATH_IMG_PALETTOBER_POSTER = os.path.join(DIR_IMG_PALETTOBER, "PALETTE_INKTOBER.jpg")
PATH_IMG_HAPPY = os.path.join(DIR_IMG_PALETTOBER, "happy.png")

DOCID_PALETTE_PARTICULARS_SURVEY = "DOCID_PALETTE_PARTICULARS_SURVEY"
DOCID_BIRTHDAY_TRACKER = "DOCID_BIRTHDAY_TRACKER"
DOCID_INKTOBER_TRACKER = "DOCID_INKTOBER_TRACKER"
DOCID_WEEKLYPROMPTS_TRACKER = "DOCID_WEEKLYPROMPTS_TRACKER"
DOCID_MASTER_TRACKER = "DOCID_MASTER_TRACKER"

INKTOBER_RECEIVE_CHANNEL = "INKTOBER_RECEIVE_CHANNEL"
INKTOBER_REPORT_CHANNEL = "INKTOBER_REPORT_CHANNEL"
INKTOBER_APPROVE_CHANNEL = "INKTOBER_APPROVE_CHANNEL"

WAIFUWARS_APPROVE_CHANNEL = "WAIFUWARS_APPROVE_CHANNEL"
WAIFUWARS_RECEIVE_CHANNEL = "WAIFUWARS_RECEIVE_CHANNEL"
WAIFUWARS_REPORT_CHANNEL = "WAIFUWARS_REPORT_CHANNEL"

WEEKLYPROMPTS_APPROVE_CHANNEL = "WEEKLYPROMPTS_APPROVE_CHANNEL"
WEEKLYPROMPTS_RECEIVE_CHANNEL = "WEEKLYPROMPTS_RECEIVE_CHANNEL"
WEEKLYPROMPTS_REPORT_CHANNEL = "WEEKLYPROMPTS_REPORT_CHANNEL"

ART_FIGHT_MODE_INKTOBER = "ART_FIGHT_MODE_INKTOBER"
ART_FIGHT_MODE_WAIFUWARS = "ART_FIGHT_MODE_WAIFUWARS"
ART_FIGHT_MODE_WEEKLY_PROMPTS = "ART_FIGHT_MODE_WEEKLY_PROMPTS"
ART_FIGHT_MODE_NOTHING = "ART_FIGHT_MODE_NOTHING"
ART_FIGHT_STATE = "ART_FIGHT_STATE"

BOT_USERNAME="BOT_USERNAME"

ART_FIGHT_MODES = [
  ART_FIGHT_MODE_INKTOBER,
  ART_FIGHT_MODE_WAIFUWARS,
  ART_FIGHT_MODE_WEEKLY_PROMPTS
]

BIRTHDAY_REPORT_CHANNEL = "BIRTHDAY_REPORT_CHANNEL"
ENV = "ENV"
DELAY = "DELAY"

DISCORD_TOKEN = "DISCORD_TOKEN"
DISCORD_GUILD = "DISCORD_GUILD"

NUM_WEEKS = 11
NUM_DAYS = 31

DF_ROW = 0
DF_COL = 1

BOT_DISCORD_ID_WEIRD = "<@&1015662149340774531>"

WEEKLYPROMPTS_UPLOAD_LIMIT = 2

DEFAULT_INKTOBER_STATE_DATA = ("0;" * NUM_DAYS)[:-1]
DEFAULT_WEEKLYPROMPT_STATE_DATA = ("0;" * NUM_WEEKS)[:-1]
DEFAULT_MESSAGES_DATA = {}
DEFAULT_COLUMN_DATA = ''

HOUR_POST_WEEKLYPROMPT_WEEK_MESSAGE = 8
HOUR_WISH_BIRTHDAY = 0

WEEKLYTOBER_WEEKS_TO_IGNORE = [7]

"""
Sheets constants
"""

STATE_NO_SHOUTOUTS = "NO_SHOUTOUTS"
STATE_SHOUTOUT_WEEK = "SHOUTOUT_WEEK"
STATE_SHOUTOUT_DAY = "SHOUTOUT_DAY"

STATE_DID_NOT_ATTEMPT = 0
STATE_UNDER_APPROVAL = 1
STATE_APPROVED = 2

GSHEET_COLUMN_NAME = "Name"

GSHEET_COLUMN_DISCORD = "Discord"

GSHEET_COLUMN_DISCORD = "Discord"
GSHEET_COLUMN_DISCORD_ID = "Discord Id"

GSHEET_COLUMN_NAME = "Name"

# Birthday
GSHEET_BIRTHDAY_COLUMN_STATE = "BIRTHDAY_STATE"
GSHEET_COLUMN_BIRTHDAY = "Birthday (YYYY-MM-DD)"


GSHEET_COMMON_COLUMNS = [
  GSHEET_COLUMN_NAME,
  GSHEET_COLUMN_DISCORD,
  GSHEET_COLUMN_DISCORD_ID,
]

# Waifuwars
GSHEET_WAIFUWARS_COLUMN_STATE_NUMATTACKED = "WAIFUWARS_NUMATTACKED"
GSHEET_WAIFUWARS_COLUMN_STATE_NUMATTACKING = "WAIFUWARS_NUMATTACKING"

GSHEET_WAIFUWARS_COLUMN_REJECTED = "WAIFUWARS_REJECTED"
GSHEET_WAIFUWARS_COLUMN_APPROVED = "WAIFUWARS_APPROVED"
GSHEET_WAIFUWARS_COLUMN_PENDING_APPROVAL = "WAIFUWARS_PENDING_APPROVAL"

GSHEET_WAIFUWARS_COLUMNS_MESSAGE_STATES = [
  GSHEET_WAIFUWARS_COLUMN_APPROVED, 
  GSHEET_WAIFUWARS_COLUMN_PENDING_APPROVAL, 
  GSHEET_WAIFUWARS_COLUMN_REJECTED,
]

# Weekly Prompts
GSHEET_WEEKLYPROMPT_COLUMN_STATE = "WEEKLYPROMPT_STATE"
GSHEET_WEEKLYPROMPT_COLUMN_REJECTED = "WEEKLYPROMPT_REJECTED"
GSHEET_WEEKLYPROMPT_COLUMN_APPROVED = "WEEKLYPROMPT_APPROVED"
GSHEET_WEEKLYPROMPT_COLUMN_PENDING_APPROVAL = "WEEKLYPROMPT_PENDING_APPROVAL"

GSHEET_WEEKLYPROMPT_COLUMNS_MESSAGE_STATES = [
  GSHEET_WEEKLYPROMPT_COLUMN_APPROVED,
  GSHEET_WEEKLYPROMPT_COLUMN_PENDING_APPROVAL,
  GSHEET_WEEKLYPROMPT_COLUMN_REJECTED,
]

# Inktober
GSHEET_INKTOBER_COLUMN_STATE = "INKTOBER_STATE"
GSHEET_INKTOBER_COLUMN_REJECTED = "INKTOBER_REJECTED"
GSHEET_INKTOBER_COLUMN_APPROVED = "INKTOBER_APPROVED"
GSHEET_INKTOBER_COLUMN_PENDING_APPROVAL = "INKTOBER_PENDING_APPROVAL"

GSHEET_INKTOBER_COLUMNS_MESSAGE_STATES = [
  GSHEET_INKTOBER_COLUMN_APPROVED, 
  GSHEET_INKTOBER_COLUMN_PENDING_APPROVAL, 
  GSHEET_INKTOBER_COLUMN_REJECTED,
]

GSHEET_BIRTHDAY_COLUMNS = [
  *GSHEET_COMMON_COLUMNS,
  GSHEET_BIRTHDAY_COLUMN_STATE,
  GSHEET_COLUMN_BIRTHDAY
]

GSHEET_INKTOBER_COLUMNS = [
  *GSHEET_COMMON_COLUMNS,
  GSHEET_INKTOBER_COLUMN_STATE,
  *GSHEET_INKTOBER_COLUMNS_MESSAGE_STATES
]

GSHEET_WAIFUWARS_COLUMNS = [
  *GSHEET_COMMON_COLUMNS,
  GSHEET_WAIFUWARS_COLUMN_STATE_NUMATTACKED,
  GSHEET_WAIFUWARS_COLUMN_STATE_NUMATTACKING,
  *GSHEET_WAIFUWARS_COLUMNS_MESSAGE_STATES
]

GSHEET_WEEKLYPROMPT_COLUMNS = [
  *GSHEET_COMMON_COLUMNS,
  GSHEET_WEEKLYPROMPT_COLUMN_STATE,
  *GSHEET_WEEKLYPROMPT_COLUMNS_MESSAGE_STATES
]

# dict.fromkeys is needed to preserve the order of the list after removal of duplicates.
# https://stackoverflow.com/questions/480214/how-do-i-remove-duplicates-from-a-list-while-preserving-order
GSHEET_PLAYER_COLUMNS = list(dict.fromkeys([
  *GSHEET_COMMON_COLUMNS, 
  *GSHEET_BIRTHDAY_COLUMNS,
  *GSHEET_WEEKLYPROMPT_COLUMNS,
  *GSHEET_WAIFUWARS_COLUMNS,
  *GSHEET_INKTOBER_COLUMNS
]))

GSHEET_COLUMNS_MESSAGE_STATES = [
  *GSHEET_INKTOBER_COLUMNS_MESSAGE_STATES,
  *GSHEET_WEEKLYPROMPT_COLUMNS_MESSAGE_STATES,
  *GSHEET_WAIFUWARS_COLUMNS_MESSAGE_STATES
]


class Prompt():
  def __init__(self, prompt, emoji):
    self.prompt = prompt
    self.emoji = emoji


WEEKLYPROMPT_DICT_WEEK_TO_PROMPT = {
  3: [
    Prompt("Welcome Back", ":wave:"),
    Prompt("The Return", ":partying_face:")
  ],
  4: [
    Prompt("Hawker", ":poultry_leg:"),
    Prompt("The City", ":cityscape:"),
    Prompt("The Sea", ":ocean:")
  ],
  5: [
    Prompt("Anitan Sticker Design", '''<:Anitanyes:744473390999666698>'''),
    Prompt("Anikun Sticker Design", '''<:Anikunwink:744474562913370153>''')
  ],
  6: [
    Prompt("An Anime/Manga that inspired me", ":star: :blue_book:"),
    Prompt("The coolest character", ":man_juggling:"),
    Prompt("Childhood crush", ":couple_with_heart_woman_man: :couple_ww: :couple_mm:")
  ],
  8: [
    Prompt("Travel", ":luggage:"),
    Prompt("Video Games", ":video_game:"),
    Prompt("Hobbies", ":bowling:")
  ],
  9: [
    Prompt("Training", ":runner:"),
    Prompt("Hard at Work", ":military_helmet:"),
    Prompt("The Challenge", ":muscle:")
  ],
  10: [
    Prompt("[LOCKED]", ":lock:")
  ],
  11: [
    Prompt("[LOCKED]", ":lock:")
  ],
}

PAYLOAD_PARAM_MESSAGE_TO_SUBMITTED_ARTWORK = "message_artwork"
PAYLOAD_PARAM_MESSAGE_TO_APPROVE_ARTWORK = "message_approve_artwork"
PAYLOAD_PARAM_MESSAGE_TO_APPROVE_ARTWORK_STATUS = "message_approval_status"

PAYLOAD_PARAMS = [
  PAYLOAD_PARAM_MESSAGE_TO_SUBMITTED_ARTWORK,
  PAYLOAD_PARAM_MESSAGE_TO_APPROVE_ARTWORK,
  PAYLOAD_PARAM_MESSAGE_TO_APPROVE_ARTWORK_STATUS
]



