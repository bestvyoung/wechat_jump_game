# coding: utf-8
'''
默认PEP8的docstring，文件注释写在这里
'''
import os
import sys
import json
import re


def open_accordant_config():
    screen_size = _get_screen_size()
    # config_file = "{path}/config/{screen_size}/config.json".format(
    #     path=sys.path[0],
    #     screen_size=screen_size
    # )
    config_file = repr(os.path.dirname(os.path.realpath(sys.executable))).split('\'')[1] + "/config/{screen_size}/config.json".format(
        screen_size=screen_size
    )
    
    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            print("Load config file from {}".format(config_file))
            return json.load(f)
    else:
        with open(repr(os.path.dirname(os.path.realpath(sys.executable))).split('\'')[1] + '/config/default.json', 'r') as f:
            print("Load default config")
            return json.load(f)



def _get_screen_size():
    '''
    获取手机屏幕大小
    '''
    size_str = os.popen('adb shell wm size').read()
    if not size_str:
        print('请安装 ADB 及驱动并配置环境变量')
        sys.exit()
    m = re.search(r'(\d+)x(\d+)', size_str)
    if m:
        return "{height}x{width}".format(height=m.group(2), width=m.group(1))
    return "1920x1080"
