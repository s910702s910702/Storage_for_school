board = nothing
loop = false


# Message display
function show_msg(which = "welcome")

	welcom_msg = "Welcome! This is 2048."
	control_msg = "Press w for up, s for down, a for left, d for right."
	to_start = "Input s to start the game"

	if which == "welcome"
		println(welcom_msg)
	elseif which == "control"
		println(control_msg)
	elseif which == "to_start"
		println(to_start)
	end
end

# Welcome.
function welcome()
	show_msg("welcome")
	show_msg("to_start")
end

# initial the game
function init()
	global board
	board = [[0 0 0 0]; [0 0 0 0]; [0 0 0 0]; [0 0 0 0]]

	# initial the gameboard
	for i = 1 : 2
		add_24("2")
	end
end

# print board
function printboard()
	global board

	for i = 1 : 4
		for j = 1 : 4
			print(board[i, j], "\t")
		end
		for j = 1 : 3
			println()
		end 
	end
end

# After entering the 
function mover(input)
	global board
	moved = false

	if input == "w"
		for i = 2 : 4
			for j = 1 : 4
				curx = i
				cury = j

				while board[curx, cury] != 0 && curx > 1 && board[curx - 1, cury] == 0
					board[curx - 1, cury], board[curx, cury] = board[curx, cury], board[curx - 1, cury]
					curx -= 1
					moved = true
					# println("MOVED")
				end
			end
		end
	elseif input == "s"
		for i = 3 : -1 : 1
			for j = 1 : 4
				curx = i
				cury = j

				while board[curx, cury] != 0 && curx < 4 && board[curx + 1, cury] == 0
					board[curx + 1, cury], board[curx, cury] = board[curx, cury], board[curx + 1, cury]
					curx += 1
					moved = true
					# println("MOVED")
				end
			end
		end
	elseif input == "a"
		for j = 2 : 4
			for i = 1 : 4
				curx = i
				cury = j

				while board[curx, cury] != 0 && cury > 1 && board[curx, cury - 1] == 0
					board[curx, cury - 1], board[curx, cury] = board[curx, cury], board[curx, cury - 1]
					cury -= 1
					moved = true
					# println("MOVED")
				end
			end
		end
	elseif input == "d"
		for j = 3 : -1 : 1
			for i = 1 : 4
				curx = i
				cury = j

				while board[curx, cury] != 0 && cury < 4 && board[curx, cury + 1] == 0
					board[curx, cury + 1], board[curx, cury] = board[curx, cury], board[curx, cury + 1]
					cury += 1
					moved = true
					# println("MOVED")
				end
			end
		end
	end
	# println("AFTER CHECK, THE MOVED'S VALUE IS ", moved)
	return moved
end	

# Combime the nubmers if they are same and in same direction
function combine(input)
	global board
	if input == "w"
		for i = 2 : 4
			for j = 1 : 4
				if i > 1 && board[i, j] == board[i - 1, j]
					board[i - 1, j] *= 2
					board[i, j] = 0
				end
			end
		end
	elseif input == "s"
		for i = 3 : -1 : 1
			for j = 1 : 4
				if i < 4 && board[i, j] == board[i + 1, j]
					board[i + 1, j] *= 2
					board[i, j] = 0
				end
			end
		end
	elseif input == "a"
		for j = 2 : 4
			for i = 1 : 4
				if j > 1 && board[i, j] == board[i, j - 1]
					board[i, j - 1] *= 2
					board[i, j] = 0
				end
			end
		end
	elseif input == "d"
		for j = 3 : -1 : 1
			for i = 1 : 4
				if j < 4 && board[i, j] == board[i, j + 1]
					board[i, j + 1] *= 2
					board[i, j] = 0
				end
			end
		end
	end
end

function no_blank()
	global board

	has = false

	for i = 1 : 4
		for j = 1 : 4
			if board[i, j] == 0
				has = true
			end
		end
	end
	return !has
end

# Add 2 or 4 on the board
function add_24(element)
	global board

	if no_blank()
		return 
	end

	x = abs(rand(Int)) % 4 + 1
	y = abs(rand(Int)) % 4 + 1

	while board[x, y] != 0
		# println("CHOOSE ANOTHER PLACE")
		# readline()
		x = abs(rand(Int)) % 4 + 1
		y = abs(rand(Int)) % 4 + 1
	end

	if(element == "2")
		board[x, y] = 2
	else
		k = rand(Int) & 1

		if k == 0
			board[x, y] = 2
		else
			board[x, y] = 4
		end
	end
end

function check_end()
	global board

	same = false

	for i = 1 : 4
		for j = 1 : 4
			if board[i, j] == 0
				same = true
			end
			if i > 2 && board[i, j] == board[i - 1, j]
				same = true
			end
			if i < 4 && board[i, j] == board[i + 1, j]
				same = true
			end
			if j > 2 && board[i, j] == board[i, j - 1]
				same = true
			end
			if j < 4 && board[i, j] == board[i, j + 1]
				same = true
			end
		end
	end

	return !same
end

# game loop
function gameloop()
	global loop, board

	while loop == true
		loop = !check_end()

		if loop == false
			println("GAME OVER")
		end

		show_msg("control")
		printboard()
		
		input = readline()


		# input control
		# println("YOU INPUT THE ", input)

		moved = mover(input)
		combine(input)
		moved |= mover(input)
		
		if moved == true
			add_24("24")
			add_24("24")
		end
	end
end

# main function
function main()
	global loop, board

	welcome()

	input = readline()
	# println("YOUR INPUT IS ", input)
	if input == "s" || input == "S"

		init()

		loop = true
		gameloop()
	else
		println("OUT") 
	end
end

main()