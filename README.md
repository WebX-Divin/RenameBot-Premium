# Rename Bot Premium Repo. Give a start and Use the Repo as your need.

----

# Features
 - Renames very fast .
 - Permanent Thumbnail support.
 - Supports Broadcasts.
 - Set custom caption.
 - Force subscribe available.
 - Deploy on any PaaS.
 - Developer Service 24x7. 🔥

# Required Configs 

* TOKEN         - Get bot token from @BotFather

* API_ID        - From my.telegram.org 

* API_HASH      - From my.telegram.org 

* ADMIN         - Your User ID 

* DB_URL  - Mongo Database URL from https://cloud.mongodb.com/

* DB_NAME  - ```optional``` Your database name from mongoDB. Default will be 'my'

* STRING -  ```optional``` Session String For Premium Users To Upload 4GB File

* LOG_CHANNEL - Channel Id to Store Files renamed files. Act as a Dump

# Commands

#### Copy and paste the command in Botfather

```
start - Start Messsage 
viewthumb - View Your Saved thumbnail
delthumb - Delete Your Thumbnail
about - About Bot 
broadcast - (Admin Use Only)Send Message To All Users
addpremium - (Admin Use Only)Add Users To Rename More Then 4Gb Files and Remove Time Limit 

```

# Deploy on VPS

* Clone the Repo
```
git clone https://github.com/WebX-Divin/RenameBot-Premium
```
* Move to the Repo Folder
```
cd RenameBot-Premium
```
* Update the instance
```
apt update && upgrade
```
* Install the requirements
```
pip install -r requirements.txt
```
* Create the nested environment
```
apt install tmux
```
* Open the nested environment
```
tmux
```
* Run the Bot
```
python3 bot.py
```

 # Join Telegram Channel 
 - [WebXBots](https://t.me/WebXBots). Bot Updates Channel
 - Support Group [WebX-Support](https://t.me/Web_X_Support). For Bug report.