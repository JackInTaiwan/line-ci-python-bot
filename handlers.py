from flask import Flask, request
from linebot import (
    LineBotApi,
    WebhookHandler,
)
from linebot.models import (
    MessageEvent,
    FlexSendMessage,
    BubbleContainer,
)



CHANNEL_TOKEN = "TB5yHtCgFd4bpv74W5C5cBwPVHwjST5/6NntK68od4OTbL2xKqcFja76Yb86BkVtd9AXK431eE7Gs3AfS4yQp573YGXc5U+Llq4g0NKZq5AWCbtoUe3M597QXJfc63ow8fggSRXSp/84MQadzhxeWQdB04t89/1O/w1cDnyilFU="
CHANNEL_SECRET = "c80566dca51b314332768ca929117904"

line_bot_api = LineBotApi(CHANNEL_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)
app = Flask(__name__)


@app.route("/ci", methods=["POST"])
def ci_post():
    data = request.json
    drone_repo_name = data["drone_repo_name"] if "drone_repo_name" in data else ""
    drone_commit_branch = data["drone_commit_branch"] if "drone_commit_branch" in data else ""
    drone_commit_author = data["drone_commit_author"] if "drone_commit_author" in data else ""
    drone_commit_message = data["drone_commit_message"] if "drone_commit_message" in data else ""
    drone_commit_buildevent = data["drone_commit_buildevent"] if "drone_commit_buildevent" in data else ""
    drone_commit_status = data["drone_commit_status"] if "drone_commit_status" in data else ""
    drone_commit_link = data["drone_commit_link"] if "drone_commit_link" in data else ""
    #json = {"type":"bubble","body":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"Git Dev","weight":"bold","wrap":False,"color":"#1DB446","flex":1,"size":"sm","margin":"none","align":"start","gravity":"top"},{"type":"text","text":"DRONE_REPO_NAME","weight":"bold","wrap":False,"color":"#464646","flex":1,"size":"xxl","margin":"md","align":"start","gravity":"top"},{"type":"text","text":"DRONE_COMMIT_MESSAGE","weight":"regular","wrap":True,"color":"#aaaaaa","flex":1,"size":"xs","margin":"md","align":"start","gravity":"top"},{"type":"separator","margin":"md","color":"#555555"},{"type":"box","layout":"vertical","contents":[{"type":"box","layout":"horizontal","contents":[{"type":"text","text":"Branch","weight":"regular","wrap":False,"color":"#555555","flex":0,"size":"sm","margin":"none","align":"start","gravity":"top"},{"type":"text","text":"DRONE_COMMIT_BRANCH","weight":"regular","wrap":False,"color":"#111111","flex":1,"size":"sm","margin":"none","align":"end","gravity":"top"}],"flex":1,"spacing":"none","margin":"md"},{"type":"box","layout":"horizontal","contents":[{"type":"text","text":"Event","weight":"regular","wrap":False,"color":"#555555","flex":0,"size":"sm","margin":"none","align":"start","gravity":"top"},{"type":"text","text":"DRONE_BUILD_EVENT","weight":"regular","wrap":False,"color":"#111111","flex":1,"size":"sm","margin":"none","align":"end","gravity":"top"}],"flex":1,"spacing":"none","margin":"md"},{"type":"box","layout":"horizontal","contents":[{"type":"text","text":"Author","weight":"regular","wrap":False,"color":"#555555","flex":0,"size":"sm","margin":"none","align":"start","gravity":"top"},{"type":"text","text":"DRONE_COMMIT_AUTHOR","weight":"regular","wrap":False,"color":"#111111","flex":1,"size":"sm","margin":"none","align":"end","gravity":"top"}],"flex":1,"spacing":"none","margin":"md"},{"type":"box","layout":"horizontal","contents":[{"type":"text","text":"Build Number","weight":"regular","wrap":False,"color":"#555555","flex":1,"size":"sm","margin":"none","align":"start","gravity":"top"},{"type":"text","text":"CI_BUILD_NUMBER","weight":"regular","wrap":False,"color":"#111111","flex":1,"size":"sm","margin":"none","align":"end","gravity":"top"}],"flex":1,"spacing":"none","margin":"md"},{"type":"box","layout":"horizontal","contents":[{"type":"text","text":"Build Status","weight":"regular","wrap":False,"color":"#555555","flex":1,"size":"sm","margin":"none","align":"start","gravity":"top"},{"type":"text","text":"DRONE_BUILD_STATUS","weight":"regular","wrap":False,"color":"#111111","flex":1,"size":"sm","margin":"none","align":"end","gravity":"top"}],"flex":1,"spacing":"none","margin":"md"}],"flex":1,"spacing":"none","margin":"md"},{"type":"box","layout":"horizontal","contents":[{"type":"button","action":{"type":"uri","label":"See Changes","uri":"https://twst.tewst.tw"},"flex":1,"margin":"none","height":"md","style":"primary","color":"#9b9b9b","gravity":"center"}],"flex":1,"spacing":"none","margin":"xxl"}],"flex":1,"spacing":"none","margin":"md"},"styles":{"header":{"backgroundColor":"#FFFFFF","separator":False,"separatorColor":"#FFFFFF"},"hero":{"backgroundColor":"#FFFFFF","separator":False,"separatorColor":"#FFFFFF"},"body":{"backgroundColor":"#FFFFFF","separator":False,"separatorColor":"#FFFFFF"},"footer":{"backgroundColor":"#FFFFFF","separator":False,"separatorColor":"#FFFFFF"}}}
    json = {"type":"bubble","body":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"Git Dev","weight":"bold","wrap":False,"color":"#1DB446","flex":1,"size":"sm","margin":"none","align":"start","gravity":"top"},{"type":"text","text":"DRONE_REPO_NAME","weight":"bold","wrap":False,"color":"#464646","flex":1,"size":"xxl","margin":"md","align":"start","gravity":"top"},{"type":"text","text":"DRONE_COMMIT_MESSAGE","weight":"regular","wrap":True,"color":"#aaaaaa","flex":1,"size":"xs","margin":"md","align":"start","gravity":"top"},{"type":"separator","margin":"md","color":"#555555"},{"type":"box","layout":"vertical","contents":[{"type":"box","layout":"horizontal","contents":[{"type":"text","text":"Branch","weight":"regular","wrap":False,"color":"#555555","flex":0,"size":"sm","margin":"none","align":"start","gravity":"top"},{"type":"text","text":"DRONE_COMMIT_BRANCH","weight":"regular","wrap":False,"color":"#111111","flex":1,"size":"sm","margin":"none","align":"end","gravity":"top"}],"flex":1,"spacing":"none","margin":"md"},{"type":"box","layout":"horizontal","contents":[{"type":"text","text":"Event","weight":"regular","wrap":False,"color":"#555555","flex":0,"size":"sm","margin":"none","align":"start","gravity":"top"},{"type":"text","text":"DRONE_BUILD_EVENT","weight":"regular","wrap":False,"color":"#111111","flex":1,"size":"sm","margin":"none","align":"end","gravity":"top"}],"flex":1,"spacing":"none","margin":"md"},{"type":"box","layout":"horizontal","contents":[{"type":"text","text":"Author","weight":"regular","wrap":False,"color":"#555555","flex":0,"size":"sm","margin":"none","align":"start","gravity":"top"},{"type":"text","text":"DRONE_COMMIT_AUTHOR","weight":"regular","wrap":False,"color":"#111111","flex":1,"size":"sm","margin":"none","align":"end","gravity":"top"}],"flex":1,"spacing":"none","margin":"md"},{"type":"box","layout":"horizontal","contents":[{"type":"text","text":"Build Number","weight":"regular","wrap":False,"color":"#555555","flex":1,"size":"sm","margin":"none","align":"start","gravity":"top"},{"type":"text","text":"CI_BUILD_NUMBER","weight":"regular","wrap":False,"color":"#111111","flex":1,"size":"sm","margin":"none","align":"end","gravity":"top"}],"flex":1,"spacing":"none","margin":"md"},{"type":"box","layout":"horizontal","contents":[{"type":"text","text":"Build Status","weight":"regular","wrap":False,"color":"#555555","flex":1,"size":"sm","margin":"none","align":"start","gravity":"top"},{"type":"text","text":"DRONE_BUILD_STATUS","weight":"regular","wrap":False,"color":"#111111","flex":1,"size":"sm","margin":"none","align":"end","gravity":"top"}],"flex":1,"spacing":"none","margin":"md"}],"flex":1,"spacing":"none","margin":"md"},{"type":"box","layout":"horizontal","contents":[{"type":"button","action":{"type":"uri","label":"See Changes","uri":"https://a;difj.tw"},"flex":1,"margin":"none","height":"md","style":"primary","color":"#9b9b9b","gravity":"center"}],"flex":1,"spacing":"none","margin":"xxl"}],"flex":1,"spacing":"none","margin":"md"},"styles":{"header":{"backgroundColor":"#FFFFFF","separator":False,"separatorColor":"#FFFFFF"},"hero":{"backgroundColor":"#FFFFFF","separator":False,"separatorColor":"#FFFFFF"},"body":{"backgroundColor":"#FFFFFF","separator":False,"separatorColor":"#FFFFFF"},"footer":{"backgroundColor":"#FFFFFF","separator":False,"separatorColor":"#FFFFFF"}}}

    flex_message = FlexSendMessage(alt_text="flex test", contents=BubbleContainer.new_from_json_dict(json))
    line_bot_api.push_message("C5861144e6e0e940170e6bf485601d169", flex_message)
    return 'OK'