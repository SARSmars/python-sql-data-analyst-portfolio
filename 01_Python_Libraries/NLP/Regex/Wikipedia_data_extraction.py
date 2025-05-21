import re
# Example text info from wikipedia for regex practice
text = """Senior Advisor to the President
Incumbent
Assumed office
January 20, 2025
Serving with Massad Boulos, Boris Epshteyn
President	Donald Trump
Preceded by	Tom Perez
Personal details
Born	Elon Reeve Musk
June 28, 1971 (age 53)
Pretoria, South Africa
Citizenship	
South Africa
Canada
United States (from 2002)
Political party	Independent
Spouses	
Justine Wilson
​
​(m. 2000; div. 2008)​
Talulah Riley
​
​(m. 2010; div. 2012)​
​
​(m. 2013; div. 2016)​
Domestic partner	Grimes (2018–2021)
Children	At least 14, including Vivian Wilson[1]
Parents	
Errol Musk (father)
Maye Musk (mother)
Relatives	Musk family
Education	University of Pennsylvania (BA, BS)
Occupation	
CEO and product architect of Tesla
Founder, CEO, and chief engineer of SpaceX
Founder and CEO of xAI
Founder of the Boring Company and X Corp.
Co-founder of Neuralink, OpenAI, Zip2, and X.com (part of PayPal)
President of the Musk Foundation
De facto leader of the Department of Government Efficiency
Awards	Full list
Signature	
Elon Musk's voice
D

Elon Reeve Musk (/ˈiːlɒn/ EE-lon; born June 28, 1971) is a businessman known for his leadership of Tesla, SpaceX, and X (formerly Twitter). Since 2025, he has been a senior advisor to United States president Donald Trump and the de facto head of the Department of Government Efficiency (DOGE). Musk has been considered the wealthiest person in the world since 2021; as of May 2025, Forbes estimates his net worth to be US$424.7 billion. He was named Time magazine's Person of the Year in 2021.

Born to a wealthy family in Pretoria, South Africa, Musk emigrated in 1989 to Canada. He graduated from the University of Pennsylvania in the U.S. before moving to California to pursue business ventures. In 1995, Musk co-founded the software company Zip2. Following its sale in 1999, he co-founded X.com, an online payment company that later merged to form PayPal, which was acquired by eBay in 2002. That year, Musk also became a U.S. citizen.

In 2002, Musk founded the space technology company SpaceX, becoming its CEO and chief engineer; the company has since led innovations in reusable rockets and commercial spaceflight. Musk joined the automaker Tesla as an early investor in 2004 and became its CEO and product architect in 2008; it has since become a leader in electric vehicles. In 2015, he co-founded OpenAI to advance artificial intelligence research but later left; growing discontent with the organization's direction in the 2020s led him to establish xAI. In 2022, he acquired the social network Twitter, implementing significant changes and rebranding it as X in 2023. In January 2025, he was appointed head of Trump's newly created DOGE. His other businesses include the neurotechnology company Neuralink, which he co-founded in 2016, and the tunneling company the Boring Company, which he founded in 2017.

Musk's political activities and views have made him a polarizing figure. He has been criticized for making unscientific and misleading statements, including COVID-19 misinformation and promoting conspiracy theories, and affirming antisemitic, racist, and transphobic comments. His acquisition of Twitter was controversial due to a subsequent increase in hate speech and the spread of misinformation on the service. Especially since the 2024 U.S. presidential election, Musk has been heavily involved in politics as a vocal supporter of Trump. Musk was the largest donor in the 2024 U.S. presidential election and is a supporter of global far-right figures, causes, and political parties. His role in the second Trump administration, particularly in regards to DOGE, has attracted public backlash.

Early life
See also: Musk family
Elon Reeve Musk was born on June 28, 1971, in Pretoria, South Africa's administrative capital.[2][3] He is of British and Pennsylvania Dutch ancestry.[4][5] His mother, Maye (née Haldeman), is a model and dietitian born in Saskatchewan, Canada, and raised in South Africa.[6][7][8] His father, Errol Musk, is a South African electromechanical engineer, pilot, sailor, consultant, emerald dealer, and property developer, who partly owned a rental lodge at Timbavati Private Nature Reserve.[9][10][11][12] His maternal grandfather, Joshua N. Haldeman, who died in a plane crash when Elon was a toddler, was an American-born Canadian chiropractor, aviator and political activist in the Technocracy movement[13][14] who moved to South Africa in 1950.[15] Haldeman's anti-government, anti-democratic and conspiracist views, which included the promotion of far-right antisemitic conspiracy theories,[16][17] "fanatical" support of apartheid,[17] and according to Errol Musk, support of Nazism[18] have been suggested as an influence on Elon.[19][20][21][22] During his childhood, Elon was told stories by his grandmother of Haldeman's travels and exploits, and Elon has suggested that all of Haldeman's descendants have his "desire for adventure, exploration – doing crazy things".[23]

Elon has a younger brother, Kimbal, a younger sister, Tosca, and four paternal half-siblings.[24][25][8][26] Musk was raised in the Anglican Church, in which he was baptized.[27][28] The Musk family was wealthy during Elon's youth.[12] Despite both Elon and Errol previously stating that Errol was a part owner of a Zambian emerald mine,[12] in 2023, Errol recounted that the deal he made was to receive "a portion of the emeralds produced at three small mines".[29][30] Errol was elected to the Pretoria City Council as a representative of the anti-apartheid Progressive Party and has said that his children shared their father's dislike of apartheid.[2]

After his parents divorced in 1980,[clarification needed] Elon, who was about 10 at the time, chose to live with his father because he had an Encyclopaedia Britannica and a computer.[31][4][9] Elon later regretted his decision and became estranged from his father.[32] Elon has recounted trips to a wilderness school that he described as a "paramilitary Lord of the Flies" where "bullying was a virtue" and children were encouraged to fight over rations.[33] In one incident, after an altercation with a fellow pupil, Elon was thrown down concrete steps and beaten severely, leading to him being hospitalized for his injuries.[34] Elon described his father berating him after he was discharged from the hospital.[34] Errol denied berating Elon and claimed, "The boy had just lost his father to suicide and Elon had called him stupid. Elon had a tendency to call people stupid. How could I possibly blame that child?"[35]

Elon was an enthusiastic reader of books, and had attributed his success in part to having read The Lord of the Rings, the Foundation series, and The Hitchhiker's Guide to the Galaxy.[11][36] At age ten, he developed an interest in computing and video games, teaching himself how to program from the VIC-20 user manual.[37] At age twelve, Elon sold his BASIC-based game Blastar to PC and Office Technology magazine for approximately $500.[38][39]

Education
An ornate school building
Musk graduated from Pretoria Boys High School in South Africa.
Musk attended Waterkloof House Preparatory School, Bryanston High School, and then Pretoria Boys High School, where he graduated.[40] Musk was a good but unexceptional student, earning a 61 in Afrikaans and a B on his senior math certification.[41] Musk applied for a Canadian passport through his Canadian-born mother to avoid South Africa's mandatory military service,[42][43] which would have forced him to participate in the apartheid regime,[2] as well as to ease his path to immigration to the United States.[44] While waiting for his application to be processed, he attended the University of Pretoria for five months.[45]

Musk arrived in Canada in June 1989, connected with a second cousin in Saskatchewan,[46][47] and worked odd jobs including at a farm and a lumber mill.[48] In 1990, he entered Queen's University in Kingston, Ontario.[49][50] Two years later, he transferred to the University of Pennsylvania, where he studied until 1995.[51] Although Musk has said that he earned his degrees in 1995, the University of Pennsylvania did not award them until 1997 – a Bachelor of Arts in physics and a Bachelor of Science in economics from the university's Wharton School.[52][53][54][55][56] He reportedly hosted large, ticketed house parties to help pay for tuition, and wrote a business plan for an electronic book-scanning service similar to Google Books.[57]

In 1994, Musk held two internships in Silicon Valley: one at energy storage startup Pinnacle Research Institute, which investigated electrolytic supercapacitors for energy storage, and another at Palo Alto–based startup Rocket Science Games.[58][59] In 1995, he was accepted to a graduate program in materials science at Stanford University, but did not enroll.[54][52][60] Musk decided to join the Internet boom, applying for a job at Netscape, to which he reportedly never received a response.[61][42] The Washington Post reported that Musk lacked legal authorization to remain and work in the United States after failing to enroll at Stanford.[60] In response, Musk said he was allowed to work at that time and that his student visa transitioned to an H1-B. According to numerous former business associates and shareholders, Musk said he was on a student visa at the time.[62]"""

# get the Birth data search wikipedia text
pattern = 'Born.*\n(.*)'
match = re.findall(pattern, text)
# print("The Birth data of the person is: ", match[0].strip())

# get the net worth data from the Wikipedia text
pattern = 'worth [^0-9]*(\$\d+.\d+)'
match = re.findall(pattern, text)
# print("The net worth of the person is: ", match[0].strip())

# get the eduation of from the text provided

pattern = 'Education(.*\n)'
match = re.findall(pattern, text)
# print("The eduation of the person is", match[0].strip())

# function to get the result based on the pattern and the text input
def get_pattern_match(pattern, text):
    matches = re.findall(pattern, text)
    if matches:
        return matches[0].strip()
    else:
        return None



get_pattern_match('Education(.*\n)', text)
get_pattern_match('Born.*\n(.*)', text)
get_pattern_match('worth [^0-9]*(\$\d+.\d+)', text)


# function to get all the data from the text input
def get_personal_information(text):
    education = get_pattern_match('Education(.*\n)', text)
    net_worth = get_pattern_match('worth [^0-9]*(\$\d+.\d+)', text)
    birth_date = get_pattern_match('Born.*\n(.*)', text)

    return{
        'education': education,
        'birth_date': birth_date,
        'net_worth': net_worth,
    }
    s

print(get_personal_information(text))

