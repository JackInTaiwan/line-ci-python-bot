from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import random
import json

from linebot.models import (
    MessageEvent,
    FlexSendMessage,
    TextMessage,
    BubbleContainer,
    CarouselContainer,
)



env = eval(Environment(
    loader=FileSystemLoader('./'),
    autoescape=select_autoescape(['json'])
).get_template("env.json").render())

template_env = Environment(
    loader=FileSystemLoader('./'),
    autoescape=select_autoescape(['json'])
)


BOT_NAME = env["bot_name"]
CHANNEL_TOKEN = env["channel_token"]
CHANNEL_SECRET = env["channel_secret"]

FLEX_JSON_FP = "./template/flex.json"
PROJECTS_FLEX_JSON_FP = "./template/projects_flex.json"

line_bot_api = LineBotApi(CHANNEL_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)
app = Flask(__name__)



@app.route("/callback", methods=["POST"])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except Exception as e:
        print(e)
        abort(400)

    return 'OK'



@app.route("/ci", methods=["POST"])
def ci_post():
    data = request.json
    drone_repo_name = data["drone_repo_name"] if "drone_repo_name" in data else "-"
    drone_commit_branch = data["drone_commit_branch"] if "drone_commit_branch" in data else "-"
    drone_commit_author = data["drone_commit_author"] if "drone_commit_author" in data else "-"
    drone_commit_message = data["drone_commit_message"] if "drone_commit_message" in data else "-"
    drone_build_event = data["drone_build_event"] if "drone_build_event" in data else "-"
    drone_build_status = data["drone_commit_status"] if "drone_commit_status" in data else "-"
    drone_commit_link = data["drone_commit_link"] if "drone_commit_link" in data else "-"
    build_status_color = "#33aa55" if drone_build_status.lower() == "success" else "#cc3d33"
    ci_build_number = data["ci_build_number"] if "ci_build_number" in data else "-"

    template = template_env.get_template(FLEX_JSON_FP)
    rendered_template = template.render(
        build_status_color=build_status_color,
        drone_repo_name=drone_repo_name,
        drone_commit_branch=drone_commit_branch,
        drone_commit_author=drone_commit_author,
        drone_commit_message=drone_commit_message,
        drone_build_event=drone_build_event,
        drone_build_status=drone_build_status,
        drone_commit_link=drone_commit_link,
        ci_build_number=ci_build_number,
    )

    dict_template = eval(rendered_template)

    users = ["Ashley", "Wei", "Jack", "Patrick", "Angela", "Leo"]
    flex_message = FlexSendMessage(alt_text="{} repo 有最新更動！".format(drone_repo_name), contents=BubbleContainer.new_from_json_dict(dict_template))
    text_message = TextMessage( text="請 *@{}*  負責審 PR !".format(random.choice(users)))
    line_bot_api.push_message(GROUP_ID, [flex_message, text_message])

    return 'OK'



@handler.add(MessageEvent, message=TextMessage)
def text_message_handler(event):
    if BOT_NAME.lower() == event.message.text.lower():
        show_menu_handler(event.source.group_id)
    elif event.message.text.lower() == "groupid":
        line_bot_api.reply_message(event.reply_token, TextMessage(text=event.source.group_id))



def show_menu_handler(group_id):
    print("[DEBUG] use show_menu_handler")

    template = template_env.get_template(PROJECTS_FLEX_JSON_FP)
    carousel_list = []
    for proj in env["projects"]:
        if proj["group_id"] == group_id:
            rendered_template = template.render(project_name=proj["name"])
            dict_template = eval(rendered_template)
            carousel_list.append(BubbleContainer.new_from_json_dict(dict_template))

    flex_message = FlexSendMessage(alt_text="請選擇專案加入", contents=CarouselContainer(carousel_list))
    line_bot_api.push_message(group_id, flex_message)