# generate_mobileconfig

A command-line tool to generate [Apple Configuration Profile](https://support.apple.com/guide/deployment/create-and-edit-configuration-profiles-depf34ebc2ca/web) (`.mobileconfig`) files for deploying Mail account settings to iOS and macOS devices.

- Automates Mail profile creation for enterprise or personal use
- Supports custom organization name and domain in payload identifiers
- Uses a simple `.env` file for configuration
- Output ready for direct use or MDM deployment
- MIT Licensed

---

## Features

- Reads all mail configuration from a `.env` file
- Customizable organization name and profile domain (`com.yourcompany.mobileconfig`)
- Generates unique UUIDs for every profile
- Filename uses email with `@` replaced by `_`
- Command-line usage with `--env` and `--verbose`
- Works on all modern macOS versions (including Sequoia)
- Open source and easily extensible

---

## Requirements

- **Python 3.7+** (Install via [Homebrew](https://brew.sh/): `brew install python`)
- **python-dotenv**  
  Install via pip:
  ```sh
  pip install python-dotenv
