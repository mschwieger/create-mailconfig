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
  ```
- (Recommended) Use a [virtual environment](https://docs.python.org/3/library/venv.html)

---

## Installation

1. **Clone this repository**
   ```sh
   git clone https://github.com/yourorg/generate_mobileconfig.git
   cd generate_mobileconfig
   ```

2. **Create and activate a Python virtual environment (recommended):**
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the required package:**
   ```sh
   pip install python-dotenv
   ```

4. **(Optional) Make the script executable:**
   ```sh
   chmod +x generate_mobileconfig.py
   ```

---

## Usage

### 1. Prepare your `.env` file

Create a `.env` file in the same directory as the script, for example:

```env
PROFILE_DOMAIN=com.example.mobileconfig
ORGANIZATION_NAME=Your Company Name
EMAIL_ACCOUNT_NAME=John Doe
EMAIL_ADDRESS=johndoe@example.com
MAIL_PASSWORD=supersecret
MAIL_SERVER=mail.example.com
IMAP_PORT=993
IMAP_SSL=True
SMTP_PORT=465
SMTP_SSL=True
EMAIL_ACCOUNT_DESCRIPTION=Work Email
```

---

### 2. Generate your `.mobileconfig` file

In your terminal, run:

```sh
# Standard usage (uses .env in the current directory)
./generate_mobileconfig.py

# Specify a custom .env file
./generate_mobileconfig.py --env myother.env

# Verbose mode (shows more details)
./generate_mobileconfig.py -v
```

- The generated file will be named like `johndoe_example.com.mobileconfig`.

---

### 3. Deploy

- **Manual:** Double-click the `.mobileconfig` on a Mac, or AirDrop/email it to iOS devices.
- **MDM:** Upload or push via your organization’s Mobile Device Management solution (Jamf, Intune, Mosyle, Kandji, etc).

---

## Customization

- **Organization name:** Set `ORGANIZATION_NAME` in your `.env` file.
- **Profile domain:** Edit `PROFILE_DOMAIN` for the root of your payload identifiers.
- **Mail server and ports:** Use your own IMAP/SMTP info in the `.env` file.
- **Want to batch generate profiles?**  
  The script is easily adapted for batch mode using CSV. Contact the author or see the project issues for examples.

---

## Troubleshooting

- **python-dotenv not found?**  
  Make sure you activated your venv, or run `pip install python-dotenv`.
- **pip errors ("externally managed environment")?**  
  Use a venv (recommended), or install with  
  `pip install --break-system-packages python-dotenv` *(not recommended)*.
- **Bad interpreter after Homebrew Python upgrade?**  
  Delete and recreate your venv:
  ```sh
  rm -rf venv
  python3 -m venv venv
  source venv/bin/activate
  pip install python-dotenv
  ```

---

## License

MIT License.  
See [LICENSE](LICENSE) for details.

---

## Credits

- Written by [Your Name or Organization]
- Powered by [python-dotenv](https://github.com/theskumar/python-dotenv)
- Inspired by Apple’s MDM and Configuration Profile documentation

---

## Contributions

Pull requests, bug reports, and feature requests are welcome!
