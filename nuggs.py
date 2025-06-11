#this is an implementation of the mc nuggets problem:
"""
The Chicken McNugget problem, also known as the Frobenius coin problem or postage stamp problem, asks for the largest integer that cannot be expressed as a linear combination
of two given relatively prime integers with non-negative coefficients.

Chicken McNuggets can be purchased in quantities of 6, 9, and 20 pieces. You can buy exactly 15 pieces by purchasing a 6 and a 9, but you can't buy exactly 10 McNuggets.
What is the largest number of McNuggets that can NOT be purchased?
"""
#this is a combination sum apporach, creating a tree to store every combination of summed coefficients.

coeffs=[6,9,20]

#recursive decision tree with 3 branches
tree=[[6,9,20]]

#recusive algorithm to create the tree:
def NewLayer(tree):
    layer = len(tree) #running the function creates a new layer to the tree, this determines which layer we are on
    tree.append([])#create new layer
    for stem in range(len(tree[layer-1])): #stem is the branch we are forking out from, we need to iterate through and fork out from each branch in the above layer
        for branch in range(len(coeffs)): #then create a new branches for the addition of each coeff from the layer above
            count=tree[layer-1][stem]+coeffs[branch]
            if layer > 12: #this is what breaks the recursion. 12 is a sensible amount of layers
                return "done"
            else:
                tree[layer].append(count)
    NewLayer(tree)
NewLayer(tree)

possibles=[] #create a set of all numbers between 0 and the biggest number in the tree
for z in range(tree[-2][-1]):
    possibles.append(z+1)

for x in range(len(tree)):
    for y in range(len(tree[x])):
        if tree[x][y] in possibles:
            possibles.remove(tree[x][y]) #go through the tree and remove every number in the tree from possibles

b=len(possibles)
popped=0
for a in range(1,b):
    if possibles[a-popped]>coeffs[0]*len(tree): #we cannot know for certain a number has no way of being made up unless we have tried making it every possible way
        possibles.pop(a-popped) #graphically this means we cannot be certain about any number bigger than the leftermost branch of the highest level of the tree
        popped+=1
#so we remove everything bigger than that limit

print(possibles) #output the remaing numbers, the amounts that cannot be bought
print("this is tested absolutely up to: "+str(coeffs[0]*len(tree)))
