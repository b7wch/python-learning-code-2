# -*- coding:utf-8 -*-
# 2017/8/15
import os
import yaml
import shlex
from stat import *
import subprocess
from time import sleep


class Daemon(object):
    def __init__(self, process_path, update_path, sleep_time=2):
        self.process_list = None
        self.process_path = process_path
        self.update_path = update_path
        self.sleep_time = sleep_time
        self.process_list = list()
        os.chmod(self.process_path, 0666)
        # self.load_process()

    def load_process(self):
        """加载要被监控的进程列表（load the list of the processes those needed monitor）"""
        if not os.path.exists(self.process_path):
            return
        if oct(os.stat(self.process_path)[ST_MODE])[-3:] == '666':
            with open(self.process_path) as f:
                self.process_list = yaml.safe_load(f)
            os.chmod(self.process_path, 0555)

    def monitor_update(self):
        """监控列表有更新时执行此过程（When the process list updated, run this function）"""
        if not os.path.exists(self.update_path):
            return
        if oct(os.stat(self.update_path)[ST_MODE])[-3:] == '666':
            with open(self.update_path) as f:
                update_operation = yaml.safe_load(f)
            for each in update_operation:
                self.handle_update(each)
            os.chmod(self.process_path, 0666)
            os.chmod(self.update_path, 0555)
        self.load_process()

    @staticmethod
    def handle_update(update_info):
        """处理更新（handle the update）"""
        name = update_info.get("name")
        update_commands = update_info.get("update")
        for each in update_commands:
            subprocess.Popen(shlex.split(each), shell=False)

    def monitor_run(self):
        """主监控循环（the main loop of the monitor）"""
        while True:
            self.monitor_update()
            self.load_process()
            for each in self.process_list:
                self.monitor(each)
            sleep(self.sleep_time)

    @staticmethod
    def monitor(process_path):
        """对单条监控单元进行检查，如果进程未在运行，则启动该进程
            （check the unit of the process list , if any process is down, pull up it）
        """
        if not process_path.get("command") or not process_path.get('monitor'):
            return
        monitor_result = os.popen(process_path.get("monitor"))
        if len(monitor_result.readlines()) > 0:
            print '[Monitor]Command: "{0}" is running'.format(process_path.get("command"))
        else:
            for each in process_path.get("command"):
                running_result = subprocess.Popen(shlex.split(each), shell=False)
                print running_result

if __name__ == '__main__':
    dic = os.path.dirname(os.path.realpath(__file__))
    process_file = dic+'/process_info.yml'
    update_file = dic+'/process_update.yml'
    monitor = Daemon(process_file, update_file)
    monitor.monitor_run()
