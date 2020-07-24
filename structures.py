# Module contains the data for questions and answers, to be imported by the server file, server.py


question_set = [
("Which American comedian and political commentator hosted the White House correspondent's dinner in 2017?",
	"Hasan",
	"Russell Peters", "John Oliver", "Hasan Minhaj", "Aziz Ansari",
	"Host of the Netflix show titled Patriot Act."),

("Which actor portrayed the role of Dinesh Chugtai in the HBO show 'Silicon valley?'","Kumail",
	"Aasif Mandvi", "Kumail Nanjiani", "Amir Khan", "Ali Kazmi",
	"Also starred as himself in 'The Big Sick.'"),

("Which American Actor is the star of the Netflix series 'Master of None'?","Aziz",
"Aasif Mandvi", "Mohammed Aamer", "Aziz Ansari", "Negin Farsad",
 "Tom Haverford in the NBC show Parks & Recreation."),

("Which of the following Indian actors starred in the movie 'My Name is Khan'?","Shahrukh", 
	"Amitabh Bachchan", "Shahrukh Khan", "Irrfan Khan", "Akshay Kumar",
	"Appeared on My Next Guest with David Letterman."),

("Which actor performed as Dr. Rajith Ratha in the 2012 film - The Amazing Spiderman?","Irrfan",
	"Kumail Nanjiani", "Salman Khan", "Alyy Khan", "Irrfan Khan", 
	"Also appeared as Mr. Masrani in 'Jurassic World' in 2015."),

("Which British Singer-Songwriter is famous for his work 'The Peace Train'?","Yusuf",
	"Sami Yusuf", "Yusuf Islam", "Nadine Shah", "Natasha Khan",
	"Stage name - Cat Stevens, famous song - If You Want to Sing Out, Sing Out"),

("In which year did Soviet Union enter Afghanistan in order to gain control of the land?","SovietYear",
	"1978", "1979", "1980","1981",
	"Late Seventies."),

("Who is the renowned author-book combination is set against the backdrop of the Soviet military intervention?", "Khaled",
	"Andrea Busfield - Born Under a Million Shadows", "James A. Michener - Caravans", "Khaled Hosseini - The Kite Runner", "Mohammed Hanif - A Case of Exploding Mangoes",
	"2007 Movie Adaptation by the same name."),

("Which mathematician's book was titled Algebra (al-jabr)?","AlKhwarizmi",
	"Sind ibn Ali", "Omar Khayyam", "Al-Khwarizmi","Thābit ibn Qurrah",
	"'Algorithm' is the Latinized version of his name!"),

("Can you guess the original name of Avicenna - the father of early modern medicine?", "Avicenna",
	"Sindbad", "Ibn Sina", "Sikander", "Ibn al-Nafis",
	"The word Ibn means 'son-of'."),

("What is the name of the Islamic(Lunar) Calendar?", "Hijri",
	"Hager", "Hijri", "Muslim", "Momin",
	"Begins with an H!"),

("Where was the famous explorer of the medieval world Ibn Battuta born?", "IbnBattuta",
	"Egypt", "Morocco", "Iraq", "Libya",
	"Very popular tourism destination!"),

("Who is the author of the book - 'No god but God'?", "Reza",
	"Mohsin Hamid", "Reza Aslan", "Khaled Hosseini", "Ayisha Malik",
	"Also authored 'Zealot: The Life and Times of Jesus of Nazareth'!"),

("Benazir Bhutto was the Prime Minister of which country?", "Bhutto",
	"Bangladesh", "Malaysia", "Pakistan", "Turkey",
	"In the Indian Subcontinent"),

("US Olympic Medalist Ibtihaj Muhammad is in which sport?", "Ibtihaj",
	"Kickboxing", "Fencing", "Golf", "Archery",
	"En garde!"),

("The Ancient city of Damascus is located in which country?","Damascus",
	"Egypt", "Turkey", "Syria", "Lebanon",
	"Also the Capital of the country."),

("'Queen of Sheba' is associated with which present-day country?","Sheba",
	"Oman", "Bahrain", "Yemen", "Qatar",
	"This country is affected by extreme famine :(")

]

#Answer Data {Key:Value}


answer_set= {

"Sheba":("Yemen","http://www.bbc.co.uk/history/ancient/cultures/sheba_01.shtml"),

"Damascus":("Syria","https://whc.unesco.org/en/list/20/"),

"Ibtihaj":("Fencing","https://www.ibtihajmuhammad.com/"),

"Bhutto":("Pakistan","https://www.history.com/topics/womens-history/benazir-bhutto"),

"Reza":("Reza Aslan", "https://www.goodreads.com/book/show/40411388-no-god-but-god"),

"IbnBattuta": ("Morocco", "https://www.britannica.com/biography/Ibn-Battuta"),

"Hijri": ("Hijri", "https://www.timeanddate.com/calendar/islamic-calendar.html"),

"Avicenna": ("Ibn Sina", "https://plato.stanford.edu/entries/ibn-sina/"),

"AlKhwarizmi":("Al-Khwarizmi","https://www.storyofmathematics.com/islamic_alkhwarizmi.html"),

"SovietYear":("1979",
"https://www.theatlantic.com/photo/2014/08/the-soviet-war-in-afghanistan-1979-1989/100786/"),

"Hasan":("Hasan Minhaj",
"https://www.netflix.com/title/80239931"),

"Kumail":("Kumail Nanjiani",
"https://www.youtube.com/watch?v=Rlwb2WbDWVI"), 

"Irrfan":("Irrfan Khan",
"https://www.firstpost.com/entertainment/irrfan-khan-passes-away-at-53-from-the-amazing-spider-man-to-slumdog-millionaire-a-look-at-the-actors-international-work-8312551.html"),

"Shahrukh":("Shahrukh Khan",
"https://www.huffingtonpost.in/entry/shah-rukh-khan-netflix-david-letterman-show_in_5db2a892e4b0b9ba5c495d68"),

"Aziz":("Aziz Ansari",
"https://www.hollywoodreporter.com/live-feed/aziz-ansari-status-master-season-3-1029170"),

"Yusuf":("Yusuf Islam","https://www.youtube.com/watch?v=vjUyM_xd6IA"),

"Khaled":("Khaled Hosseini - The Kite Runner","https://khaledhosseini.com/books/the-kite-runner/")
}