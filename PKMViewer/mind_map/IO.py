#import xmindparser
from xmindparser import xmind_to_dict
import os
def load_dataset(path,sheet_sub=0):
	if path.endswith(".xmind")==False:
		return
	#xmindparser.config = {
	#	'showTopicId': True, # 是否展示主题ID
	#	'hideEmptyValue': True # 是否隐藏空值
	#}
	sheets = xmind_to_dict(path)
	sheet = sheets[sheet_sub]
	return sheet

'''
def load_dataset(path):
	os.path.splittext(path)[-1]
	filename = "./learn.xmind"
	sheets = xmind_to_dict(filename)
	sheet = sheets[0]
'''