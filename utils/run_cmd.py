# -*- coding: utf-8 -*-
__author__ = 'caden'
"""
description:执行cmd命令
"""
import subprocess


class RunCmd:
    @staticmethod
    def running_cmd(cmd):
        output, errors = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        result = output.decode("utf-8")
        return result

