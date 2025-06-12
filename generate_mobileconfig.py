#!/usr/bin/env python3
import os
import uuid
import argparse
from dotenv import load_dotenv

def bool_xml(val):
    return 'true' if val else 'false'

def main():
    parser = argparse.ArgumentParser(
        description="Generate a .mobileconfig profile for Mail on iOS/macOS."
    )
    parser.add_argument(
        "-e", "--env", 
        help="Path to .env file (default: .env in current dir)",
        default=".env"
    )
    parser.add_argument(
        "-v", "--verbose",
        help="Print details as the profile is generated",
        action="store_true"
    )
    args = parser.parse_args()

    # Load .env
    if not os.path.isfile(args.env):
        print(f"ERROR: .env file '{args.env}' not found.")
        return
    load_dotenv(dotenv_path=args.env)

    # Read from environment
    profile_domain = os.getenv('PROFILE_DOMAIN')
    organization_name = os.getenv('ORGANIZATION_NAME')
    name = os.getenv('EMAIL_ACCOUNT_NAME')
    email = os.getenv('EMAIL_ADDRESS')
    password = os.getenv('MAIL_PASSWORD')
    mail_server = os.getenv('MAIL_SERVER')
    imap_port = int(os.getenv('IMAP_PORT'))
    imap_ssl = os.getenv('IMAP_SSL').lower() == 'true'
    smtp_port = int(os.getenv('SMTP_PORT'))
    smtp_ssl = os.getenv('SMTP_SSL').lower() == 'true'
    description = os.getenv('EMAIL_ACCOUNT_DESCRIPTION')

    # Validate required variables
    required_vars = [
        ('PROFILE_DOMAIN', profile_domain),
        ('ORGANIZATION_NAME', organization_name),
        ('EMAIL_ACCOUNT_NAME', name),
        ('EMAIL_ADDRESS', email),
        ('MAIL_PASSWORD', password),
        ('MAIL_SERVER', mail_server),
        ('IMAP_PORT', imap_port),
        ('IMAP_SSL', imap_ssl),
        ('SMTP_PORT', smtp_port),
        ('SMTP_SSL', smtp_ssl),
        ('EMAIL_ACCOUNT_DESCRIPTION', description),
    ]
    missing = [var for var, val in required_vars if val in [None, '']]
    if missing:
        print(f"ERROR: Missing required variables in .env: {', '.join(missing)}")
        return

    mail_uuid = str(uuid.uuid4())
    root_uuid = str(uuid.uuid4())
    filename = email.replace('@', '_') + '.mobileconfig'

    mobileconfig = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>EmailAccountDescription</key>
            <string>{description}</string>
            <key>EmailAccountName</key>
            <string>{name}</string>
            <key>EmailAccountType</key>
            <string>EmailTypeIMAP</string>
            <key>EmailAddress</key>
            <string>{email}</string>
            <key>IncomingMailServerHostName</key>
            <string>{mail_server}</string>
            <key>IncomingMailServerPortNumber</key>
            <integer>{imap_port}</integer>
            <key>IncomingMailServerUseSSL</key>
            <{bool_xml(imap_ssl)}/>
            <key>IncomingMailServerUsername</key>
            <string>{email}</string>
            <key>IncomingPassword</key>
            <string>{password}</string>
            <key>OutgoingMailServerHostName</key>
            <string>{mail_server}</string>
            <key>OutgoingMailServerPortNumber</key>
            <integer>{smtp_port}</integer>
            <key>OutgoingMailServerUseSSL</key>
            <{bool_xml(smtp_ssl)}/>
            <key>OutgoingMailServerUsername</key>
            <string>{email}</string>
            <key>OutgoingPassword</key>
            <string>{password}</string>
            <key>PayloadDisplayName</key>
            <string>Mail</string>
            <key>PayloadIdentifier</key>
            <string>{profile_domain}.mail.{mail_uuid}</string>
            <key>PayloadType</key>
            <string>com.apple.mail.managed</string>
            <key>PayloadUUID</key>
            <string>{mail_uuid}</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Email Account Profile</string>
    <key>PayloadIdentifier</key>
    <string>{profile_domain}.mailprofile.root.{root_uuid}</string>
    <key>PayloadOrganization</key>
    <string>{organization_name}</string>
    <key>PayloadRemovalDisallowed</key>
    <false/>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>{root_uuid}</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
'''

    with open(filename, 'w') as f:
        f.write(mobileconfig)

    if args.verbose:
        print("Generated .mobileconfig with the following parameters:")
        print(f"  Profile Domain     : {profile_domain}")
        print(f"  Organization Name  : {organization_name}")
        print(f"  Email Name         : {name}")
        print(f"  Email Address      : {email}")
        print(f"  Server             : {mail_server}")
        print(f"  IMAP Port/SSL      : {imap_port} / {imap_ssl}")
        print(f"  SMTP Port/SSL      : {smtp_port} / {smtp_ssl}")
        print(f"  Output file        : {filename}")
    else:
        print(f'Generated {filename}')

if __name__ == "__main__":
    main()
