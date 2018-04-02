with open('assembly', 'r') as file:
	data = file.read()
	cmds = data.split(";\n")
	cmdfile = {}
	for cmd in cmds:
		if cmd == '':
			cmdfile[format(len(cmdfile), 'X')] = "EOF"
			break
		line = cmd.split(" ")
		addr = line[0] + line[1]
		addr = format(int(addr, 2), 'X')
		cmdfile[line[0] + line[1]] = line[2:]
