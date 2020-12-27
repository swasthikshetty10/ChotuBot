import praw
import random
reddit = praw.Reddit(client_id = "api-client-id-here", 
                    client_secret = "Reddit-api-client_secret",
                    username = "(reddit)username",
                    password = "(reddit)passwed",
                    user_agent = 'pythonbot')





#MEME #MEME #MEME #MEME #MEME #MEME #MEME #MEME #MEME #MEME   #MEME #MEME #MEME #MEME #MEME                

kills = [
    "died from a creeper explosion",
    "died from lack of quality memes on Dank Memer",
    "disappeared from the universe.",
    "died from subscribing to t-series",
    "died from not subscribing to Pewdiepie",
    "ripped their own heart out to show their love for jhonny sins",
    "dies because they were just too angry😡 ",
    "chokes on cheerios and dies. What an idiot...",
    "died from patta se head shot 🔫",
    "was killed for being too noob.. what a noob",
    "died after fapping 50 times in a row with no break.",
    "because they were just too Lazy.",
    "was killed by imposter",
    "died from lack of ***, U got that 😁",
    "drowned in their own tears 😭.",
    "was eaten by the duolingo owl🦉 ",
    "dies, but don't let this distract you from the fact that in 1998, The Undertaker threw",
    "died from a nightmare👻 dream",
    "died while playing hopscotch on seemingly deactivated land mines.",
    "loses the will to live🤥",
    "died from whacking it too much. (There's a healthy balance, boys)",
    "eats too much copypasta and explodes",
    "reads memes till they die.",
    "dies of starvation.",
    "died somehow 🤷‍♂️",
    "died by taking sefi🤳 with lion🦁 ..such a idiot ",
    "died in 2020 for not wearing mask😷",
    "died from subscribing to t-series",
    "is dead. How 🤷🏼‍♂️",
    "died of scurvy, eat oranges kids",
    "cranks up the music system only to realize the volume was at max and the song playing was Baby by Justin Beiber..",
    'died from watching to much of P**n ',
]
def randmeme(meme_name):
    meme = reddit.subreddit(meme_name)
    top = meme.top(limit = 100)
    all_meme_subs = []
    for submission  in top:
        all_meme_subs.append(submission)
    meme = random.choice(all_meme_subs)
    meme_title = meme.title
    meme_url = meme.url
    return [meme_url,meme_title]


#MEME #MEME #MEME #MEME #MEME   #MEME #MEME #MEME #MEME #MEME   #MEME #MEME #MEME #MEME #MEME   
def massmemes(meme_name , amount):
    meme = reddit.subreddit(meme_name)
    top = meme.top(limit = amount)
    all_meme_subs = []
    for submission  in top:
        all_meme_subs.append(submission)
    meme_title =[]
    meme_url = []
    for i in all_meme_subs:

        meme_title.append(i.title)
        meme_url.append(i.url)
    return [meme_title,meme_url]

stories = [
    ' Now that’s what I call stupid: In my junior year of high school, this guy asked me on a date. He rented a Redbox movie and made a pizza. We were watching the movie and the oven beeped so the pizza was done. He looked me dead in the eye and said, “This is the worst part.” I then watched this boy open the oven and pull the pizza out with his bare hands, rack and all, screaming at the top of his lungs. We never had a second date.',
    ' The fake report card: I failed the first quarter of a class in middle school, so I made a fake report card. I did this every quarter that year. I forgot that they mail home the end-of-year cards, and my mom got it before I could intercept with my fake. She was PISSED—at the school for their error. The teacher also retired that year and had already thrown out his records, so they had to take my mother’s “proof” (the fake ones I made throughout the year) and “correct” the “mistake.” I’ve never told her the truth. ',
    ' All the fish: I went to this girl’s party the week after she beat the shit out of my friend. While everyone was getting trashed, I went around putting tuna inside all the curtain rods and so like weeks went by and they couldn’t figure out why the house smelled like festering death. They caught me through this video where these guys at the party were singing Beyoncé while I was in the background with a can of tuna. ',
    ' How to win at video games: When I was little, I would go on Nickelodeon.com all the time and they had this game similar to Club Penguin, except it was called Nicktropolis. And if you forgot your password, a security question you could choose was “What is your eye color?” and if you got it right it’d tell you your password. So I would go to popular locations in Nicktropolis and write down random usernames who were also in those areas, and then I would log out and type in the username as if it were my own and see which of these usernames had a security question set to “What is your eye color?” (Which was most of them, since it was easy and we were all kids). I would then try either brown, blue, or green, and always get in, then I would go to their house and send all of their furniture and decorations to my own accounts. And if I didn’t want it, I could sell it for money. ',
    ' Drama at my drama class: One time my drama class’s teacher had gone home sick so we were just put in a classroom with a movie to entertain us for the period when an alarm went off. None of us were sure if it was the fire alarm or the lockdown alarm, so we all head out into the hall to check and no one’s out there, so we head back in and climb under our desks as is lockdown procedure. Cut to an hour or so later when a teacher bursts in and nearly dies of relief because the school was on fire and we were the only students not accounted for and half the faculty and fire department had been searching for us for ages. Literally, the whole school had filled with smoke while we’d kept super safe under our wooden desks. ',
    ' I drew a penis with a glue stick on the whiteboard: My whole class once got detention because I drew a penis with a glue stick on the whiteboard and when the teacher went to wipe off the board all the fluff came off and stuck to the glue. I never got in trouble for it because my whole class found it too funny to tell the teacher it was me. ',
    ' The day my teacher stole my headphones: During my sophomore year of high school, we were doing silent work and my history teacher said that we could listen to music but if it was too loud he would “break our headphones.” so I’m doing my work quietly with my music on low, and this obnoxious kid sitting next to me had his music really loud. I could hear it over my music but ignored it. My teacher thought it was me. So he comes up to me & ripped my BRAND NEW Apple headphones, looking ruthless. He suddenly realized it was the guy next to me and he was completely embarrassed. He came in the next day with a new pair and an apology note taped to them. He couldn’t look me in the eye for the rest of the year. ',
    ' Oh—semen: When I was in high school, I was pretty quiet around people who weren’t my friends. The high school’s wrestling coach also taught geometry, and he was my teacher. This resulted in a lot of wrestlers skipping class and barging into our classroom to hang out and not get in trouble. One day, seven wrestlers come in yelling about new wrestling uniforms, and how excited they were. When they go over and pull out the uniforms, the whole class is kind of side eyeing them. Even without what I mention next, the suits look funny. I mean, it’s tight royal blue Spandex with a suspender style top. Absolutely funny already. But the wrestlers grab the uniforms and rush out of the room to go change in the bathroom, and come back to show them off. Which, is also hysterical because Spandex hides NOTHING; you could see all of their junk '
    ' Anyway, we live in a town called Ocean City. It’s commonly abbreviated as “OC”. On the back of the Spandex uniform, it says Ocean City Men in large letters. Except… they used the abbreviation. On the back, it says OC MEN. Which isn’t awful, but then I sound it out in my head. OC MEN. Oh—semen. I almost spit out the water I was drinking. '
    ' I looked around frantically, trying to find out who I can tell, because I didn’t have any friends to tell in this class. I turn to the girl next to me, and I had no idea who she was and had never talked to her before. I told her what I found and we both cracked up. ',
    ' The whole time she saw me as the quiet teacher’s pet who was shy as hell. The first words out of my mouth were “It says oh semen. '
    ' We’ve been best friends for 7 years now. ',
    ' I swear to God he levitated: I have a friend who I’ve known since I was very little. One day, when he was six, I was at his house when he got this absolutely god-awful stomach pain. I mean, he was literally writhing in pain. So, his mom took him to the doctor’s office, where the doctor took one look and told her to take him to the ER. She feared something along the lines of an intestinal rupture. About half way to the hospital, my friend suddenly let rip the loudest, most powerful fart any of us had ever heard. I swear to God he levitated. We thought the upholstery in the car seat had ripped. After a good 30 seconds of intense farting, he looked at his mom and said, “I feel all better now!” ',
    ' We don’t have a fucking doorbell: So a couple years I moved out of state with a boyfriend. Was super excited about it but with reason had anxiety about being so far from friends and family. One of the ways my anxiety was coming out was with nightmares and night terrors. I’d wake up violently sitting up in a cold sweat, gasping and whatnot. On one particular night I had woken up the sound of our doorbell ringing. Which at 4 in the morning is fucking nerve wracking. So I shook my boyfriend fully awake and told him I heard the doorbell and to go check it because I was scared. He quickly jumps up. Puts on clothes and grabs a bat. Goes all the way to the front door and opens it. I, scared shitless, am peeking around the corner watching it all go down. I see him step outside and I nervously await the verdict of the situation when I hear him call out to me. “Babe?” And I respond real shaky, “Yes?” He stands in the doorway with a real frustrated tired look in his eyes and says, “We don’t have a fucking doorbell.”  ',
    ' The whole school thought I was going to star on Drake and Josh: In second grade, I told everyone that I was leaving school before next semester to move to Hollywood to play Megan’s cousin from Vermont on Drake and Josh. At first I just told my best friend, but then the whole school found out. I had people coming up to me and asking me for my autograph and a teacher even asked for a picture with me. When I showed up on the first day of school in third grade, I told everyone that the show was going off the air after the season finished (even though I had no knowledge of when it was ending), and so they wouldn’t need me. AND THE SHOW ENDED AFTER THAT SEASON AND EVERYONE BELIEVED ME UP UNTIL LIKE 6TH GRADE BUT NOW MY BEST FRIEND WILL NEVER LET ME FORGET ABOUT IT AND I’M SO ANGRY. ',
    ' My favorite teacher: One time in 6th grade we were at recess and while I was running to my friends, I just so happened to kick a HUGE rock (keep in mind, I was wearing flip-flops so it hurt like hell) and without thinking, I shouted at the top of my lungs “MOTHERFUCKER!” And with my god-awful luck, my math teacher was sitting at the bench right BESIDE ME. He then took me inside to what I thought was yell at me but he just couldn’t stop laughing and sent me back outside with a literal candy bar. He is still my favorite teacher I’ve ever had. ',
    ' Why my parents can’t take me seriously: So one time I was home alone and it was around dinnertime when I decided to make myself something to eat. I opened the freezer and dug around until I found what appeared to be chicken nuggets in an unopened plastic bag that for some reason, didn’t have any cooking instructions. Thinking that my parents must have thrown away the box for box tops, I called my mom to ask how long and at what temperature to cook chicken nuggets. She told me both of them, I laid out about 20 on a tray and stuck it in the oven, setting the timer before I walked out of the kitchen. When it was almost time to get my chicken nuggets, I walked into a cinnamon scented kitchen. I searched all over that kitchen, trying to find the cinnamon scent, leading me to the oven. I decide to turn on the oven light to see if maybe my mom had stuck some cookies in the oven and forgot to bake them, but instead, I find that the tray my chicken nuggets were on has cookies on it instead! As I’m trying to process what just happened, I hear the front door open and my mom shout delightedly, “Ooooo what’s that smell?” She walks into the kitchen and catches my confused expression. That’s when the spark ignited and she realized exactly what had happened. Somehow in some form, I had accidentally baked snickerdoodles. And that is why my parents can never take my cooking seriously. ',
    ' Painting a roller coaster: So in my junior year of high school I got a project to make a roller coaster for my physics class. Everything was going fine until the day my partner and I had to paint the thing. We were in my garage spray painting the tubes and these two guys come marching up to the house across the street and start yelling at the top of their lungs, beating on the door. Now let me say in my defense the neighborhood I lived in was in south Dallas and it’s still not a safe place. Well I called the police, closed the garage and parked myself in front of the dining room window. Long story short the police showed up in full gear broke down the door and brought out the two boys at gunpoint. And that’s the story of how my entire block found out that the abandoned house had new owners. ',
    ' I literally “fell” for him: Since my crush sits behind me in class, when we stood up to do the pledge I stood up too fast and I stumbled over to him so to not fall on the ground I reached to grab his desk but I accidentally GRABBED HIM and I ended up falling on top of him and we both screamed. Luckily I didn’t hurt or crush him. My teacher and everyone else started laughing and I got so red afterwards. Now when we stand up for the pledge, he moves all the way to the back of the room away from me… ',
    ' 5th grade teacher: In fifth grade, my teacher loathed me. She would do anything to make me cry and sent me to the principle’s office any chance she got. Don’t believe me? I’m left handed. So still, to this day, I get my hands confused. On this particular day, we were doing the Pledge of Allegiance and I had put my left hand to my chest (it’s supposed to be your right hand over your heart). She got mad at me, telling me that I wasn’t being ‘patriotic’ and sent me to the principal’s office. The principal and I were quite aquatinted at this point and so I told her why I was sent back to her office again, and she laughed. And laughed. I didn’t find it funny at all, I mean all the kids in my school thought I was a delinquent so they didn’t want to be my friend. My principal wrote on the back of my hands, L and R. What I didn’t realize was that she wrote L on my right hand and R on my left hand. She did the same to hers. Then, she walked me back to the classroom, and made our whole class redo the Pledge with our ‘right’ hand, with me leading the class, and it was one of the happiest moments of my elementary experience. ',
    ' How bugs feel: When I was about 5/6 my mom and stepdad bought my sister and I bikes for Easter. After church they were like “do you wanna learn how to ride them?” And I was like??? Duh?? I had finally gotten the hang of it and I was riding around the circle showing off, and my mom was like “say cheese” so I look over at her for a second and I FUCKING RAM INTO A CAR AT FULL SPEED. A parked car that I didn’t even see, like at all, so I just rammed into this car and I fell off my bike and I was crying and all I could think about was “this must be how bugs feel” like they’re flying around living life and then SPLAT. Looking back that was my first existential crisis ',
    ' Skull lover: So I was sitting at a lecture when I feel like being stared at, and in the corner of my eye I see this really handsome guy, who’s literally just staring at me. I don’t think much of it and continue to listen to the professor. After the lecture the guy comes up to me, and lays his hand on head and I’m like “eeeehm, what are you doing” and he stares me dead in the eyes and says “I’ve never seen such a gorgeous skull” and then he turns around and leaves. ',
    ' All glowed up: After the final bell, my friend and I were walking to our buses after school through a crowded hallway. We were talking about childhood and reminiscing about old memories, and we somehow started talking about which people became hot since middle school. My friend mentioned this guy named Keenan and I said “Yeah, he is pretty hot now,” and my friend practically screamed “DUDE HE GLOWED UP SO HARD!” (“Glowed up” means I guess like someone became attractive). Anyway, right as she said that she turned her head and he was RIGHT BEHIND US (this is so so very cliché but I swear to god there he was). Anyway, right as she saw him she screamed “OH! HE’S RIGHT THERE!”. And OF COURSE he heard her, but it was so awkward so he just walked past us looking down at his phone and my friend fell on the ground from embarrassment. ',
    ' Chinese class: I took Chinese at school as a freshman. On one particular day, we didn’t have anything to do in class since we had gone through the whole curriculum for the semester. Our teacher wanted us to watch a Chinese movie in that free time, and I just so happened to watch one recently on YouTube. I offered to find it, and my teacher let me use her computer, that was connected to a Promethean board so that the whole class could see what I was doing on the screen. After a couple of minutes of searching, I couldn’t find the movie since I didn’t know the exact title, so I logged into my YouTube account and decided to find it in my history. When I opened my history I was mortified since stupid me had forgotten that being the awkward virgin that I was at the time I had searched up tutorials on kissing and making out that previous night. The whole class was hysterically laughing, my teacher was extremely confused, and I almost cried as I scrolled past all the kissing tutorials and finally found the movie. I went back to my seat and didn’t speak to anyone in class for the rest of the week. I still haven’t lived it down. ',
    ' Coca-Cola disaster: A couple years ago my friends and I were going to see a movie in the theatre at the mall. Instead of paying the ridiculous movie theatre prices for pop and candy, we decided to go to target to buy some stuff. This was when Coca Cola started to put people’s names on their bottles. My friend told me she had seen a bottle with my name on it inside this bin of Coke. I was weirdly excited since I hadn’t gotten one with my name on it yet. After I had bought the drink, I opened inside target, and it exploded EVERYWHERE. The pop was at least five or six feet in diameter. I watched as people passed the mess and made looks of disgust. Imagine if I had opened it inside of the theatre… ',
    ' The toilet phase: When I was younger, around 3 or 4 years old, I had a phase of flushing things down the toilet. I would flush McDonald’s toys I didn’t want anymore or change I had found in my room. the biggest and most hilarious thing I ever dumped was a gallon of milk. one day I was bored and was looking around in the fridge low and behold there it was, a new gallon of milk. my tiny body dragged the bottle on the floor all the way to the bathroom. I opened the cap, let it go into the toilet, and flushed. I thought I was smart enough to let it go unnoticed but I’ll never forget what my dad yelled out when he walked in. “why in the hell is the water white?!“ my mom found the empty carton and just stared at me. ',
    ' As it turns out, I am gay: When I was around 9 years old I was starting to get confused about my sexuality so I would always look up “Are You Gay” quizzes on our family computer because I was scared and confused, and my mom eventually saw the searches in the history and confronted me about it. I lied about it and said I had accidentally clicked an ad. As it turns out, I am gay.  ',
    ' Foreign student trauma: When I first moved from Lithuania to America I was 5 years old and didn’t speak any English. On the first day of kindergarten I was crying so much that my teacher picked me up and let me sit on her lap, meanwhile the rest of the kids sat on the carpet in front of me and watched me cry while she explained to them what was going on (in a language I didn’t understand). Our school was 3 buildings put together, and the pick up was at the “blue” building but my classroom was at the “red” building, so they put a sign over my neck that said “I don’t speak English and I’m going to the blue building” and sent me away to follow a crowd of other kids. I’m still traumatized… ',
    '',



]
