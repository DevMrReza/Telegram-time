# Telegram Auto Name & Bio Updater

This Python script automatically updates your Telegram profile's last name and bio every minute with the current time in various custom fonts. The time is based on the Asia/Tehran timezone and updates in real-time using cron jobs.

## Features

- **Auto Profile Update**: Changes your Telegram profile's last name and bio every minute.
- **Multiple Fonts**: Randomly selects from a list of custom fonts for the time digits.
- **Real-time Updates**: Uses cron scheduling to update the time every minute.
- **Timezone**: The script works based on the Asia/Tehran timezone.

## Requirements

- Python 3.7 or higher
- A Telegram API ID and API Hash (you can get them from [my.telegram.org](https://my.telegram.org/))
- The following Python libraries:
  - `pyrogram`
  - `aiocron`
  - `pytz`

## Installation

Follow these steps to set up and run the script on your local machine:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/DevMrReza/Telegram-time.git
   cd Telegram-time

