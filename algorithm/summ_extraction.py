import nltk
import numpy as np

# Could be required
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

operators = ("!", ".", "?", "...", ",","-");
example_text = "Angela Merkel returned to the international stage on Friday with a path to her fourth term opening up and her enemies in retreat. A week that began with the collapse of coalition talks, intrigue and finger-pointing ended with the chancellor telling her European Union partners that Germany is back to business as usual. The Social Democrats, her government partner during two of her three terms, backed off from their not-this-time attitude to another coalition deal and polls suggest Merkel's popularity among party supporters is intact. It may be another defining moment for the 63-year-old chancellor who has defied expectations of her demise before, even as strategic defeats and enemies pile up after 12 years in office. The latest left licking its wounds is the Free Democratic Party, a one-time ally of her Christian Democratic Union that walked out of coalition talks this week in a blaze of anger. The breakdown definitely left Merkel damaged, but I don't believe it's the beginning of the end of the Merkel era, Oskar Niedermayer, a political scientist at Free University in Berlin, said in an interview. There's nobody in the CDU right now who would dare to challenge her. Plot Against Merkel? The FDP exposed the soft underside to Merkel's power base with its decision to abandon talks with her Christian Democratic-led bloc and the Green party. Two senior CDU officials said they judged the FDP leader Christian Lindner was trying to stir up a party revolt against Merkel after her group's vote slumped by almost 9 percentage points in September's vote. The allegation was echoed publicly by Green negotiator Juergen Trittin. The FDP denied trying to bring down Merkel, saying the talks foundered over policy disagreements. That's truly silly, FDP negotiator Alexander von Lambsdorff told the General-Anzeiger newspaper, saying the party had no intention of stoking a palace revolt. One CDU official said Merkel's backers are concerned that 38-year-old Lindner could grow in stature to become Germany's version of Sebastian Kurz, the 31-year-old Austrian chancellor-elect who won his country's election in October on an anti-immigration platform. But the episode appeared to harm the FDP more than Merkel. Her approval rating after the coalition fiasco slipped 3 percentage points to 54 percent, while Lindner's tumbled 13 points to 32 percent, according to an Infratest Dimap poll taken Monday, a day after the talks collapsed. Old Allies. Merkel meanwhile headed to Brussels Friday to renew her contacts with senior EU officials and the Ukrainian leadership, who she helped during the 2014 tensions with Russia. I was able to tell them that we, as the acting German government, will fully fulfill our European obligations and that we will actively engage, Merkel said in a statement to reporters, adding that her comments had been well received. Yet the struggle to form a government may still embolden critics within Merkel's party such as Deputy Finance Minister Jens Spahn, 37, who took part in the failed coalition talks. Two weeks after the election, Spahn blamed other party leaders for bungling its response to Germany's refugee influx, which propelled the anti-immigration Alternative for Germany party into parliament in September. Nobody really felt like addressing this topic, he said to thunderous applause at a convention of the CDU's youth wing in Dresden. Public Support The fact is that Merkel did not handle the talks very well, Niedermayer said. Everybody made mistakes. She is headed for safer territory now though as the Social Democrats, her junior partner during two of her three previous terms, opened the door to a governing coalition for Europe's biggest economy. That lessens the risk of an unprecedented repeat election. Once again, she appears to have dodged a bullet. And even if she did have to face voters again, she still has the backing of her base. Eighty-five percent of CDU supporters say they would want Merkel to run again if the vote were to take place, according to a Forsa poll conducted Monday. As long as Merkel remains so popular with voters, people like Lindner and Spahn won't succeed, Forsa head Manfred Guellner said in an interview."
#example_text = "Jeff Bezos is the world's newest $100 billion mogul. The Amazon.com Inc. founder's fortune is up $2.4 billion to $100.3 billion, as the online retailer's shares jumped more than 2 percent on optimism for Black Friday sales. Online purchases for the day are up 18.4 percent over last year, according to data from Adobe Analytics, and investors are betting the company will take an outsized share of online spending over the gifting season. The $100 billion milestone makes Bezos, 53, the first billionaire to build a 12-figure net worth since 1999, when Microsoft Corp. co-founder Bill Gates hit the mark. Bezos's fortune rose $32.6 billion this year through Thursday, the largest increase of anyone on the Bloomberg Billionaires Index, a daily ranking of the world's 500 richest people. Amazon have climbed 5 percent this week alone. As Bezos's wealth flirts with new heights, there's likely to be more questions about what he intends to do with it. Unlike Gates, who was the world's richest person until Bezos passed him in October, or U.S. investor Warren Buffett, the world's third-richest person with $78.9 billion, Bezos has given relatively little of his fortune to charity. Bezos is only just starting to focus on philanthropy, and in June tweeted a request for ideas on how to help people. Since 2002, Bezos has given away Amazon shares worth about $500 million at current prices, according to a Bloomberg analysis of Form 4 filings. The billionaire said in April that he sells $1 billion of Amazon stock every year to fund his space business Blue Origin LLC. Gates, 62, who has a net worth of $86.8 billion according to the Bloomberg index, would be worth more than $150 billion if he hadn't given away almost 700 million Microsoft Corp. shares and $2.9 billion of cash and other assets to charity, according to an analysis of his publicly disclosed giving since 1996. The index numbers are based on the close of trading in New York Wednesday. Bezos's fortune and Amazon share data reflect Friday's closing trading prices in New York."

def calculateWordFrequency(wi, Cj):
	word_vec = [l.lower() for l in nltk.word_tokenize(Cj) if l not in operators]
	return word_vec.count(wi)

def summ_extraction(text):
	C = nltk.sent_tokenize(text)
	lenC = len(C)
	maxLen = 0
	for sent in C:
		if len(sent) > maxLen:
			maxLen = len(sent)

	# Get the meaningful words that are in any of the sentences
	w = set(nltk.word_tokenize(text))
	w = sorted([e for e in w if e not in operators])
	meaningless_verbs = ["n't",'is', 'said', 'are', 'was', 'be', 'has', 'have', 'will', 'says', 'would','were', 'had', 'been', 'could', "'s", 'can', 'do', 'say', 'make', 'may','did', 'made', 'does', 'get', 'might','should', 'reported', 'citing']
	meaningless = ['a', 'is', 'was', 'are', "'s", 'the', 'his', 'her', 'on', 'with', 'to', 'that', 'of', 'and', 'as', 'in', 'from', 'according']
	#meaningless = ['CDU', 'official', 'Lindner', 'Germany', 'Austrian']
	valid_tags = ['JJ', 'JJR', 'JJS', 'NN', 'NNS', 'NNP', 'NNPS', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
	w = [e for e in w if e not in set().union(meaningless, meaningless_verbs)]
	POS_tags = nltk.pos_tag(w)
	for (word,tag) in POS_tags:
		if tag not in valid_tags:
			w.remove(word)
	w = [e.lower() for e in w]
	lenw = len(w)

	# 2. and 3. Calculate word frequency and define term frequency
	freq_mat = np.zeros((lenC, lenw))
	term_freq_mat = np.zeros((lenC, lenw))
	for j in range(0,lenC):
		for i in range(0,lenw):
			freq_mat[j, i] = calculateWordFrequency(w[i],C[j])
		termj_max = max(freq_mat[j])
		for i in range(0,lenw):
			term_freq_mat[j, i] = 0.5 + 0.5*freq_mat[j,i]/termj_max

	# 4. Defined idf
	idf_mat = np.zeros(lenw)
	for i in range(0,lenw):
		n_docs = 0
		for j in range(0,lenC):
			if freq_mat[j,i] != 0:
				n_docs += 1
		idf_mat[i] = np.log(lenC/(1.0 + n_docs))

	# 5. Defined tf-idf
	tf_idf_mat = np.zeros((lenC, lenw))
	for j in range(0,lenC):
		for i in range(0,lenw):
			tf_idf_mat[j,i] = term_freq_mat[j,i]*idf_mat[i]

	# 6. Rank the sentences
	r_val_mat = np.zeros(lenC)
	for j in range(0,lenC):
		word_vec = [l.lower() for l in nltk.word_tokenize(C[j]) if l not in operators]
		for i in range(0,lenw):
			cnt = word_vec.count(w[i])
			r_val_mat[j] += tf_idf_mat[j,i]*cnt
		r_val_mat[j] = (r_val_mat[j]/len(word_vec))/(0.1 + np.abs(lenC/2 - j))

	print r_val_mat
	print C[np.argmin(r_val_mat)]
	r_val_mat[np.argmin(r_val_mat)] = 1
	print C[np.argmin(r_val_mat)]
	r_val_mat[np.argmin(r_val_mat)] = 1
	print C[np.argmin(r_val_mat)]

	return w

summ_extraction(example_text)

