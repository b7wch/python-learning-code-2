#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2017/11/19
import time
import json

a = {'ext': '{}', 'msgType': 'alert', 'threat': 1, 'taskid': u'3faacdcd9db1cdafd05cef242901520b', 'time': 1511084232,
     'desc': u'\u53ef\u7591\u7f51\u7edc\u884c\u4e3a,\u4fee\u6539\u7cfb\u7edf\u914d\u7f6e',
     'type': u'SuspiciousBehavior',
     'detail': '{"threats": {"version": 1, "template": {"name": "windows"}, "categories": [{"name": "high"}, {"name": "medium"}, {"classes": [{"name": "modify_system_config", "details": [{"cr3": "0x0A480280", "name": "registry", "timestamp": 14537, "pid": "1704", "kn": "HKCU\\\\SOFTWARE\\\\MICROSOFT\\\\WINDOWS\\\\CURRENTVERSION\\\\INTERNET SETTINGS\\\\ZONEMAP\\\\", "vn": "ProxyBypass", "vm": "WinXP SP3(o2k7,IE8,r1010,f102152)(1)", "action": "set", "pn": "C:\\\\WINDOWS\\\\Temp\\\\sample\\\\1.exe.bin.exe", "severity": "low"}, {"cr3": "0x0A480280", "name": "registry", "timestamp": 14537, "pid": "1704", "kn": "HKCU\\\\SOFTWARE\\\\MICROSOFT\\\\WINDOWS\\\\CURRENTVERSION\\\\INTERNET SETTINGS\\\\ZONEMAP\\\\", "vn": "IntranetName", "vm": "WinXP SP3(o2k7,IE8,r1010,f102152)(1)", "action": "set", "pn": "C:\\\\WINDOWS\\\\Temp\\\\sample\\\\1.exe.bin.exe", "severity": "low"}, {"cr3": "0x0A480280", "name": "registry", "timestamp": 14538, "pid": "1704", "kn": "HKCU\\\\SOFTWARE\\\\MICROSOFT\\\\WINDOWS\\\\CURRENTVERSION\\\\INTERNET SETTINGS\\\\ZONEMAP\\\\", "vn": "UNCAsIntranet", "vm": "WinXP SP3(o2k7,IE8,r1010,f102152)(1)", "action": "set", "pn": "C:\\\\WINDOWS\\\\Temp\\\\sample\\\\1.exe.bin.exe", "severity": "low"}, {"cr3": "0x0A480280", "name": "registry", "timestamp": 14538, "pid": "1704", "kn": "HKCU\\\\SOFTWARE\\\\MICROSOFT\\\\WINDOWS\\\\CURRENTVERSION\\\\INTERNET SETTINGS\\\\ZONEMAP\\\\", "vn": "AutoDetect", "vm": "WinXP SP3(o2k7,IE8,r1010,f102152)(1)", "action": "set", "pn": "C:\\\\WINDOWS\\\\Temp\\\\sample\\\\1.exe.bin.exe", "severity": "low"}]}, {"name": "whitelist_network", "details": [{"cr3": "0x0A480280", "addr": "", "severity": "low", "timestamp": 16707, "pid": "1704", "vm": "WinXP SP3(o2k7,IE8,r1010,f102152)(1)", "da": "192.168.1.100:80", "action": "connect", "pn": "C:\\\\WINDOWS\\\\Temp\\\\sample\\\\1.exe.bin.exe", "name": "network"}]}], "name": "low"}, {"name": "suspicious"}]}, "env": "winxpsp3cn-1"}',
     'engine_type': 3, 'name': u'\u53ef\u7591\u7f51\u7edc\u884c\u4e3a'}


def check_DIEntry_out(dict_message):
    taskid = dict_message.get('taskid', "")
    task_threat = dict_message.get("threat", 0)
    task_time = dict_message.get('time', 0)
    task_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(task_time))
    detail = json.loads(dict_message.get('detail', dict()))
    detail_categories = detail.get('threats', {}).get("categories", list())
    if not taskid:
        return list()
    result = list()
    for each in detail_categories:
        e = each.get('classes')
        if not e:
            continue
        else:
            for clas in e:
                dtas = clas.get('details', list())
                if not dtas:
                    continue
                else:
                    for d in dtas:
                        domain = d.get('da') if d.get('da') else d.get('addr')
                        if domain:
                            domain = domain.split(':')[0]
                            result.append(
                                {'taskid': taskid,
                                 'task_threat': task_threat,
                                 'check_time': task_time,
                                 'classify': '',
                                 'domain': domain,
                                 'ext': '{}'
                                 }
                            )
                        else:
                            continue
    return result


print check_DIEntry_out(a)
