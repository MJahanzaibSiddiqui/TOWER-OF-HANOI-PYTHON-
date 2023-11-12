def hanoi(n, source, target, auxiliary, moves):  #function banaya 
    if n > 0:  #yaha pe condition di take - value na aye, yani -4 number of disc na hoske 
        # Move n-1 discs from source to auxiliary
        hanoi(n-1, source, auxiliary, target, moves)  # function ke variable die or hume list ulti chalani ha
        # ager no of disc 3 ha to use 3-1=2, 2-1=1 to ye is tarah show hoga {3,2,1}
        
        # Move the nth disc from source to target
        target.append(source.pop()) # ab yaha dekh append se list me add krde or pop 
        #list se nikal deta ha, source tere pas given disc   target mtlb last wala pole 
        moves.append((source.copy(), auxiliary.copy(), target.copy())) #ye sirf list brhaega move variable ki 
        # sab se copies leke yani jis jaga jo kaam hua wo isme save hoga to ye move prhaega phr, ager sab zero 
        #ha to koi move nh brhega
        
        # Move the n-1 discs from auxiliary to target
        hanoi(n-1, auxiliary, target, source, moves) #ye sirf display purpose ke lie or function use ke lie ke is tarah value dalni ha 
# ab yaha se kaam shuru ha main ko body. 
# Initialize the towers and moves list
A = [4,3, 2, 1]  # Initial state for N = 6  ye phela pole ha (source)
B = []  #ye auxilary ha
C = []   #ye target ha
moves = [(A.copy(), B.copy(), C.copy())] # move brhane ke lie same uper wala

# Run Towers of Hanoi for N = 6 #ab sawal prh assignment ka usme 4,5,6 ke lie bhi manga ha to ye n ki value change krkr ke chala 
hanoi(4, A, C, B, moves) #function call  

# Print all moves
for move in moves:
    print(f"A: {move[0]}, B: {move[1]}, C: {move[2]}") # ye sirf print dikhane ke lie ha ke ek line me ek move 
    # or ek move a me kia change ha b me kia ha c me kia is tarah jab tak mvoes hen tab tk dikhae

# Print the number of moves
print(f"Number of moves: {len(moves)}")  # yaha pe total number of move dikha die ke bhai itne move lge hen total.
