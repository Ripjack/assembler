#python versoin 3.6
with open('assembly', 'r') as file:
	data = file.read()
	lines = data.split(";\n")
	commands = {
	'add': '0000 0000',
	'set': '0000 0000',
	'out': '0000 0000'
	}
	cmds = {}
	for cmd in lines:
		if cmd == '':
			cmds[format(len(cmds), 'x')] = ["EOF"]
			break
		line = cmd.split(" ")
		addr = line[0]
		cmds[addr] = line[1:]
	print(cmds)