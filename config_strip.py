config_file = open('config.txt')
config_list = config_file.readlines()
config_file.close

# Now open again and overwrite
config_file = open('config_scrubbed.txt', 'w')
for i in range(4,len(config_list)-2):
	config_line = config_list[i].rstrip()
	config_line = config_line.replace('\r','')
	if 'no aaa new-model' in config_line or 'login' in config_line:
		pass
	else:
		config_file.write(config_line + '\n')
config_file.close()

