from itertools import *
from operator import *
def main():

	card = get_card()
	
	print(card)
	#if 24 in ez_solve(card):
	#	return ez_solve(card)  
	
	

	#solve([6,6,4,8])
	
	

def get_card():
	nums = input("plz input 4 numbers: ").split(chr(32))
	card = [] 
	for i in nums:
		if i == chr(32):
			pass
		else:
			try:
				card.append(int(i))
			except:
				pass	
	return list(card)

def ez_solve(ln):
	mulltiply_all = lambda x: x[0] * x[1] * x[2] * x[3]

	if mulltiply_all(ln) == 24 : 
		return [24,"mulltiply all numbers "]


	add_all = lambda x: x[0] + x[1] + x[2] + x[3]
	if add_all(ln) == 24:
		return [24,"add all numbers"] 
	else:
		return "error"	

def solve(ln):
	
	ops = [mul,add,sub,truediv]

	for i in permutations(ln):
	
		for j in product(ops,repeat=3):
			cur_num = 0
			card = list(i)
			#print(card)
			cur_num += list(j)[0](card.pop(0),card.pop(0))

			card.insert(0,cur_num)


			cur_num =  list(j)[1](card.pop(0),card.pop(0))

			(card).insert(0,cur_num)
			
			cur_num = list(j)[2](card.pop(0),card.pop(0))

			

			if cur_num == 24:
				print("we have found the number", cur_num, i ,j )
				break

		break
			
			
def operations(nums):
	#card_nums = nums
	ops = ['*','+','/','-']
	#cur_opp = 0 
	

	for i in product(ops,repeat = 3):
		cur_opp = 0
		card_nums = nums

	
		
		#if card_nums == []:
			#continue


		try:	
			while cur_opp != 3:	
				card_nums = nums
				
				if i[cur_opp] == '+':
					try:
					
						print(card_nums)
						print(i)
						card_nums.insert(0, add(card_nums.pop(0),card_nums.pop(0) ))
						cur_opp += 1 
						if card_nums[0] == 24:
							return i,card_nums
					
					except:
						continue 	
				
				elif i[cur_opp] == '*':
					try:
						
						print(card_nums)
						print(i)

						card_nums.insert(0, mul(card_nums.pop(0),card_nums.pop(0))) 
						cur_opp += 1
						if card_nums[0] == 24:
							return i,card_nums	
					except:
						continue 
				
				elif i[cur_opp] == '/':
					
					try:
						
						print(card_nums)
						print(i)

						card_nums.insert(0,truediv(card_nums.pop(0),card_nums.pop(0)))
						cur_opp += 1 
						
						if card_nums[0] == 24:
							return i,card_nums
					except: 
						continue 		
				

				elif i[cur_opp] == '-':
					try:

						print(card_nums)
						print(i)

						card_nums.insert(0,sub(card_nums.pop(0),card_nums.pop(0)))
						
						if card_nums[0] == 24:
							return i,card_nums
					except:
						continue	
	

		except:
			continue 			
		
		if card_nums == []:
			continue	
			
if __name__ == "__main__":
	print(main())

