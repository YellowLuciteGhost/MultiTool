import requests

headers = {
    'authorization': 'NzcwMjA2OTI2NzY3NjUyODc0.YJByng.qAawAGsQWSlX_jHDcuAxvt8Ced4',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.309 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36',
    'content-type': 'application/json'
}

# data = """{"version": "2021-01-08T06:57:32.097000+00:00", "form_fields": [{"field_type": "TERMS", "label": "Read and agree to the server rules", "values": ["Welcome to the Official Fortnite Discord. Please familiarize yourself with the server rules.    Members are expected to follow all Community Rules and guidelines. Failure to do so may result in moderation action being taken against you, potentially up to and including a ban.", "Protect your personal information. Generally, we advise against sharing any personal information with other members.", "Account selling/buying/trading/etc. is against the Epic Games Terms of Service. This is a bannable offense both in-game and in this Discord server.", "Remain on topic and use channels correctly. Check the pinned messages in channels for additional guidance.", "Attempts to exclude community members or seek/form parties based on a player's race, ethnicity, color, religion, gender identity, sexual orientation, ability, national origin, and any other affiliation is prohibited.", "Do not spam messages or encourage spamming.", "Do not discuss Hacking/Cheating.", "No advertising or self-promotion. Do not recruit for clans/team/friend group. Do not promote unapproved Discord Servers. This applies to server messages and DMs.", "Do not link scam websites, encourage other members to break the rules,  or purposely mislead or trick members.", "Do not solicit for or promote free items including in-game cosmetics, seasonal battle passes or redeemable codes.", "All chat rules apply to Voice chat.", "Keep names appropriate or risk removal from the server.", "Keep all actions in the server friendly and appropriate so everyone may enjoy being part of this community."], "required": true}], "description": null}"""
# response = requests.put('https://discord.com/api/v9/guilds/322850917248663552/requests/@me', headers=headers, data=data)

# response = requests.get('https://discord.com/api/v9/invites/fortnite?with_counts=false').json()
# print(response)

# response = requests.get('https://discord.com/api/v9/guilds/322850917248663552/member-verification?with_guild=false&invite_code=fortnite', headers=headers).text
# print(response)

response = requests.post('https://discord.com/api/v9/users/@me/channels', headers=headers, json={'recipient_id': '751443692639879219'}).json()
print(response["id"])
res = requests.post(f'https://discord.com/api/v9/channels/{response["id"]}/messages', headers=headers, json={"content": "f"}).json()
print(res)