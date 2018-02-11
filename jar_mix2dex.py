#coding=utf-8
# -*- coding: utf-8 -*-

import os
import sys
import time
import shutil
import argparse

#configure target jar version
DefaultVersion = '9.4.3'

#configure system dex tool path
dxPath = 'E:\\android-sdks\\build-tools\\24.0.0\\dx.bat'

#----------------------------------------------------------------------------------
version = ''
zipCmd = 'jar cvf tmp.jar com/'


	
def init():
	parser = argparse.ArgumentParser(description='manual to this script')
	parser.add_argument('--ver', type=str, default = DefaultVersion)
	args = parser.parse_args()
	global version
	version = args.ver
	
def getJarFileList(dir,fileList=[]):
	for s in os.listdir(dir):
		if s.endswith('.jar'):
			fileList.append(os.path.join(dir,s))
	return fileList
	
def getDirList(dir,fileList=[]):
	for s in os.listdir(dir):
		if s.endswith('.jar'):
			fileList.append(os.path.join(dir,s))
	return fileList
	
def unzip(jardir):
	jars = getJarFileList(jardir);
	for jar in jars:
		os.system('jar xvf '+jar)

def clean():
	os.remove(os.path.join(os.getcwd(),'tmp.jar'))
	shutil.rmtree(os.path.join(os.getcwd(),'com'))
	
def dex():
	timeStr = time.strftime('%Y%m%d%H%M')
	output = 'target_' + version + '_' + timeStr + '.jar'
	print("product jar: "+output)
	zipCmd = dxPath +' --dex --output=' + output + ' tmp.jar'
	os.system(zipCmd)
	clean()
	print("--------------finish----------------")

def start():
	init()
	unzip(os.getcwd())
	os.system(zipCmd)
	dex()
	
start()
