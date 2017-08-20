#coding=utf-8
__author__ = "4N"
import os
import aiml
os.chdir('C:\\Users\\4N.hp\\AppData\\Roaming\\Python\\Python27\\site-packages\\aiml\\alice') #切换工作目录到alice文件夹下，视具体情况而定
alice = aiml.Kernel()
alice.learn("startup.xml")
alice.respond('LOAD ALICE')
alice.respond('hello')

