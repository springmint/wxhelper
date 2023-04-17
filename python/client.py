import requests
import json
import time
from message import get_news
import random


def check_login():
    """
     0.检查是否登录
    :return:
    """
    url = "http://127.0.0.1:19188/api/?type=0"
    payload = {}
    headers = {}
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


def user_info():
    """
    登录用户信息
    :return:
    """
    url = "http://127.0.0.1:19188/api/?type=8"
    payload = {}
    headers = {}
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


def send_text(wxid, txt):
    """
    发送文本filehelper
    :return:
    """
    url = "http://127.0.0.1:19188/api/?type=2"
    payload = json.dumps({
        "wxid": wxid,
        "msg": txt
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


def send_at():
    """
    发送@消息
    :return:
    """
    url = "http://127.0.0.1:19188/api/?type=3"
    payload = json.dumps({
        "chatRoomId": "12333@chatroom",
        "wxids": "notify@all",
        "msg": "12333"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


def send_img():
    """
    发送图片
    :return:
    """
    url = "http://127.0.0.1:19188/api/?type=5"
    payload = json.dumps({
        "wxid": "38979139441@chatroom",
        "imagePath": "C:/123.jpeg"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


def send_file():
    """
    发送文件
    :return:
    """
    url = "http://127.0.0.1:19188/api/?type=6"
    payload = json.dumps({
        "wxid": "filehelper",
        "filePath": "C:/test.txt"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


def hook_msg():
    """
    hook 消息
    :return:
    """
    url = "http://127.0.0.1:19188/api/?type=9"
    payload = json.dumps({
        "port": "19099",
        "ip": "127.0.0.1"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


def unhook_msg():
    """
    取消消息hook
    :return:
    """
    url = "http://127.0.0.1:19188/api/?type=10"
    payload = {}
    headers = {}
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


def hook_img():
    """
    hook 图片
    :return:
    """
    url = "http://127.0.0.1:19188/api/?type=11"
    payload = json.dumps({
        "imgDir": "C:\\img"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


def unhook_img():
    """
    取消hook 图片
    :return:
    """
    url = "http://127.0.0.1:19188/api/?type=12"
    payload = json.dumps({
        "imgDir": "C:\\img"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


def hook_voice():
    """
    hook 语音
    :return:
    """
    url = "http://127.0.0.1:19188/api/?type=56"
    payload = json.dumps({
        "msgId": 322456091115784000
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


def unhook_voice():
    """
    取消hook 语音
    :return:
    """
    url = "http://127.0.0.1:19188/api/?type=14"
    payload = {}
    headers = {}
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


def del_friend():
    """
    删除好友
    :return:
    """
    url = "http://127.0.0.1:19188/api/?type=17"
    payload = json.dumps({
        "wxid": "wxid_1124423322"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


def search_friend():
    """
    网络搜素用户
    :return:
    """
    url = "http://127.0.0.1:19188/api/?type=19"
    payload = json.dumps({
        "keyword": "13812345678"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


def add_friend():
    """
    添加好友
    :return:
    """
    url = "http://127.0.0.1:19188/api/?type=20"
    payload = json.dumps({
        "wxid": "wxid_o11222334422"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


def fetch_chat_room_members():
    """
    群成员
    :return:
    """
    url = "http://127.0.0.1:19188/api/?type=25"
    payload = json.dumps({
        "chatRoomId": "2112222004@chatroom"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


def get_member_nickname():
    """
    群成员昵称
    :return:
    """
    url = "http://127.0.0.1:19188/api/?type=26"
    payload = json.dumps({
        "chatRoomId": "322333384@chatroom",
        "memberId": "wxid_4m1112222u22"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


def del_member():
    """
    删除群成员
    :return:
    """
    url = "http://127.0.0.1:19188/api/?type=27"
    payload = json.dumps({
        "chatRoomId": "31122263384@chatroom",
        "memberIds": "wxid_12223334422"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


def add_member():
    """
    增加群成员
    :return:
    """
    url = "http://127.0.0.1:19188/api/?type=28"
    payload = json.dumps({
        "chatRoomId": "1111163384@chatroom",
        "memberIds": "wxid_o12222222"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


def modify_room_name():
    """
    修改群昵称
    :return:
    """
    url = "http://127.0.0.1:19188/api/?type=31"
    payload = json.dumps({
        "chatRoomId": "222285428@chatroom",
        "wxid": "wxid_222222512",
        "nickName": "qqq"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


def get_db_handlers():
    """
    获取sqlite3的操作句柄
    :return:
    """
    url = "http://127.0.0.1:19188/api/?type=32"
    payload = {}
    headers = {}
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


def query_db_by_sql():
    """
    查询数据库
    :return:
    """
    url = "http://127.0.0.1:19188/api/?type=34"
    payload = json.dumps({
        "dbHandle": 116201928,
        "sql": "select localId from MSG where MsgSvrID= 7533111101686156"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


def hook_log():
    """
    hook 日志
    :return:
    """
    url = "http://127.0.0.1:19188/api/?type=36"
    payload = {}
    headers = {}
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


def unhook_log():
    """
    取消hook日志
    :return:
    """
    url = "http://127.0.0.1:19188/api/?type=37"
    payload = {}
    headers = {}
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


def forward():
    """
    转发消息
    :return:
    """
    url = "http://127.0.0.1:19188/api/?type=40"
    payload = json.dumps({
        "wxid": "filehelper",
        "msgid": "705117679011122708"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


def logout():
    """
    退出登录
    :return:
    """
    url = "http://127.0.0.1:19188/api/?type=44"
    payload = {}
    headers = {}
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


def confirm_receipt():
    """
    确认收款
    :return:
    """
    url = "http://127.0.0.1:19188/api/?type=45"
    payload = json.dumps({
        "wxid": "wxid_1111112622",
        "transcationId": "10000500012312222212243388865912",
        "transferId": "100005000120212222173123036"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


def contact_list():
    """
    好友列表
    :return:
    """
    url = "http://127.0.0.1:19188/api/?type=46"
    payload = {}
    headers = {}
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


def room_detail():
    """
    群详情
    :return:
    """
    url = "http://127.0.0.1:19188/api/?type=47"
    payload = json.dumps({
        "chatRoomId": "199134446111@chatroom"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


def ocr():
    """
    ocr提取文字
    :return:
    """
    url = "http://127.0.0.1:19188/api/?type=49"
    payload = json.dumps({
        "imagePath": "C:\\WeChat Files\\b23e84997144dd12f21554b0.dat"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


def pat():
    """
    拍一拍
    :return:
    """
    url = "http://127.0.0.1:19188/api/?type=50"
    payload = json.dumps({
        "chatRoomId": "211111121004@chatroom",
        "wxid": "wxid_111111111422"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


def top_msg():
    """
    消息置顶
    :return:
    """
    url = "http://127.0.0.1:19188/api/?type=51"
    payload = json.dumps({
        "wxid": "wxid_o11114422",
        "msgid": 3728307145189195000
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


def close_top_msg():
    """
    取消置顶
    :return:
    """
    url = "http://127.0.0.1:19188/api/?type=52"
    payload = json.dumps({
        "chatRoomId": "213222231004@chatroom",
        "msgid": 3728307145189195000
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


def sns_first():
    """
    朋友圈首页
    :return:
    """
    url = "http://127.0.0.1:19188/api/?type=53"
    payload = {}
    headers = {}
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


def sns_next():
    """
    朋友圈下一页
    :return:
    """
    url = "http://127.0.0.1:19188/api/?type=54"
    payload = json.dumps({
        "snsId": "14091988153735844377"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


def query_nickname():
    """
    查询联系人或群名称
    :return:
    """
    url = "http://127.0.0.1:19188/api/?type=55"

    payload = json.dumps({
        "id": "wxid_1112p4422"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


def download_msg_attach():
    """
    下载消息附件
    :return:
    """
    url = "http://127.0.0.1:19188/api/?type=56"
    payload = json.dumps({
        "msgId": 6080100336053626000
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


def get_member_info():
    """
    获取群/群成员信息
    :return:
    """
    url = "http://127.0.0.1:19188/api/?type=57"
    payload = json.dumps({
        "wxid": "wxid_tx8k6tu21112"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


def send_cpbox_news(news_list):
    slogan = "【Crypto Box】致力于成为最专业的Web3投研信息、实用工具、教程百科平台！\n # 公众号:CryptoBox     官网：即将上线"
    try:
        print("begin")
        check_login()
    except requests.exceptions.ConnectionError:
        print("something error!\n")
        # 记录在列表里面，相近的时间可以发送
    else:
        for el in news_list:
            if el["type"] == 1:
                send_contxt = "【标题】" + el["title"] + "\n" + "【内容】" + el["message"] + \
                    "\n" + "------------------------------------\n【发布时间】" + \
                    el["publishedAt"] + \
                    "\n" + slogan
                # print(send_contxt)
                send_text("38979139441@chatroom", send_contxt)  # 测试群
                send_text("48491358084@chatroom", send_contxt)
            elif el["type"] == 2:
                send_contxt = "类型】: 币安公告【内容】" + el["title"] + "\n" + "【链接】" + el["news_url"] + \
                    "\n" + "------------------------------------\n【发布时间】" + \
                    el["publishedAt"] + \
                    "\n" + slogan
                send_text("38979139441@chatroom", send_contxt)  # 测试群


def run_all_time():
    while 1:
        randoma = random.randint(300, 600)
        time.sleep(randoma)
        try:
            print("begin")
            check_login()
        except requests.exceptions.ConnectionError:
            print("something error!\n")
        else:
            rst_list = []
            rst_list = get_news()
        for el in rst_list:
            send_contxt = "【标题】" + el["title"] + "\n" + "【内容】" + el["message"] + \
                "\n" + "------------------------------------\n【发布时间】" + \
                el["publishedAt"] + \
                "\n【CryptoBox】致力于成为最专业的Web3投研信息、实用工具、教程百科平台！\n#公众号:CryptoBox     官网：即将上线"
            # print(send_contxt)
            send_text("38979139441@chatroom", send_contxt)
            send_text("48491358084@chatroom", send_contxt)


# if __name__ == '__main__':
    # hook_msg()
    # unhook_msg()
    # user_info()
    # send_text()
    # run_all_time()
