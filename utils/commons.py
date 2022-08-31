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

BIRTHDAY_REPORT_CHANNEL = "BIRTHDAY_REPORT_CHANNEL"
ENV = "ENV"
DELAY = "DELAY"

DISCORD_TOKEN = "DISCORD_TOKEN"
DISCORD_GUILD = "DISCORD_GUILD"

NUM_WEEKS = 13
NUM_DAYS = 31


DF_ROW = 0
DF_COL = 1

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
GSHEET_COLUMN_NAME = "Name"

# Birthday
GSHEET_BIRTHDAY_COLUMN_STATE = "BIRTHDAY_STATE"
GSHEET_COLUMN_BIRTHDAY = "Birthday (DDMMYYYY)"

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
  GSHEET_BIRTHDAY_COLUMN_STATE,
  GSHEET_COLUMN_BIRTHDAY
]

GSHEET_INKTOBER_COLUMNS = [
  GSHEET_INKTOBER_COLUMN_STATE,
  *GSHEET_INKTOBER_COLUMNS_MESSAGE_STATES
]

GSHEET_WAIFUWARS_COLUMNS = [
  GSHEET_WAIFUWARS_COLUMN_STATE_NUMATTACKED,
  GSHEET_WAIFUWARS_COLUMN_STATE_NUMATTACKING,
  *GSHEET_WAIFUWARS_COLUMNS_MESSAGE_STATES
]

GSHEET_WEEKLYPROMPT_COLUMNS = [
  GSHEET_WEEKLYPROMPT_COLUMN_STATE,
  *GSHEET_WEEKLYPROMPT_COLUMNS_MESSAGE_STATES
]

GSHEET_PLAYER_COLUMNS = [
  GSHEET_COLUMN_NAME,
  GSHEET_COLUMN_DISCORD,
  
  *GSHEET_WEEKLYPROMPT_COLUMNS,
  *GSHEET_WAIFUWARS_COLUMNS,
  *GSHEET_BIRTHDAY_COLUMNS,
  *GSHEET_INKTOBER_COLUMNS
]

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
    Prompt("Anitan Sticker Design", ":Anitanyes:"),
    Prompt("Anikun Sticker Design", ":Anikunwink:")
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



