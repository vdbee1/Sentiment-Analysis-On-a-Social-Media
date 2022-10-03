class blankck:
	def blankcheck(df):
		blank=0
		for row,i in enumerate(df["Message_Original"]):
			i = str(i)
			if i == "0":
				blank+= 1
				df.loc[row , 'NA'] ="Yes"
			else:
				df.loc[row , 'NA'] = "No"
		#Print statement for debugging purposes
			print ('blank check going on')
		return blank