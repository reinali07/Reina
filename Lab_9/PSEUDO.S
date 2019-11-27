//pseudo code for part 1

bubble_sort:
	R4 = LIST
	R5 = R4[0] //NUMBER OF ELEMENTS IN LIST
	R4 = R4[1]
	R0 = 1
	while R0 == 1: //if the previous run, something was swapped
		R0 = 0
		for i = 0 to R5: //not including the last element
			SWAP R4[i] and R4[i+1] //swap if needed
		end for
	end while
end

SWAP:
	if R4[i] > R4[i+1]:
		swap these
		R0 = 1
	end if
end

