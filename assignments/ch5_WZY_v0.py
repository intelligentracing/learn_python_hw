print("Please enter the range of prime number")
print("Start from?")
sta=input()
print("End in?")
end=input()
sub = int(end) - int(sta)
if (sub > 0) :
	det = int(sta)
	PrimeNumber = []
	tot = 0
	while (det <= int(end)) :
		div = 2
		IsPri = True
		while (div < det) :
			if (det % div == 0) :
				IsPri = False
			div+=1
		if (IsPri == True and det > 1) :
			PrimeNumber.append(det)
			tot+=1
		det+=1
	answer="The prime numbers are"
	print(answer)
	print(str(PrimeNumber))
	print(str(tot))
else :
	print("Error!")