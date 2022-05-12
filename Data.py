from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

If you don't trust me, 
1) stop reading this message
2) delete this chat

Still reading?
You can use me to generate pyrogram and telethon string session. Use the below buttons to know more!

    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")],
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")
        ],
    ]

    # Help Message
    HELP = """
» Click the below button or use /generate command to start generating session!
» Click the required button; [Pyrogram/Telethon]
» Enter the required variables when asked.

BTW, if you don’t trust me, you can host [one] like me using my source code provided in my about page; [/about]
"""

    # About Message
    ABOUT = """
**• About Me •** 

• A telegram bot to generate pyrogram and telethon string session...

» Source Code : [Click Here](https://github.com/realeu/StringSessionBot)

» Framework : [Pyrogram](docs.pyrogram.org)

» Language : [Python](www.python.org)

    """
