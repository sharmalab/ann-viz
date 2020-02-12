import pandas as pd
import seaborn as sns
def main():
	sns.set(style="whitegrid")
	tips = sns.load_dataset("tips")
	ax = sns.violinplot(x=tips["total_bill"])
	plot = ax.plot()
	#fig = plot.get_figure()
	plot.savefig("plot.png")
main()