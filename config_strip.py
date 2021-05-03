config_file = open('config.txt')
config_list = config_file.readlines()
config_file.close

# Now open again and overwrite
config_file = open('config.txt', 'w')
for i in range(8,len(config_list)-3):
	config_line = config_list[i]
	if 'no aaa new-model' in config_line or 'login' in config_line:
		pass
	else:
		config_file.write(config_line)
config_file.close()

