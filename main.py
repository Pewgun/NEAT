from population import Population
summ = 0
pop = Population()
for i in range(200):
	print(f"gen: {i}")
	for g in pop.genomes:
		ins = [[0,0],[0,1],[1,0],[1,1]]
		outs = [0,1,1, 0]
		diff = 0.0
		g.prepareNetwork()
		for inn, out in zip(ins, outs):
			o = g.feedForward(inn)
			diff += (o[0]-out)**2
		g.fitness = (4.0 - diff)/4.0

	pop.naturalSelection()
	if pop.bestScore > 0.95:
		break

pop.showSpeciesMemNum()
pop.showBestGenomeOuputMap()
pop.showBestGenomeNeuralNet()
pop.showFitnessGrowth()

g = pop.bestGenome
g.prepareNetwork()
ins = [[0,0],[0,1],[1,0],[1,1]]
outs = [0,1,1, 0]
diff = 0.0
for inn, out in zip(ins, outs):
	o = g.feedForward(inn)
	print(inn)
	print(o[0])
	diff += (o[0]-out)**2
print((4.0 - diff)/4.0)