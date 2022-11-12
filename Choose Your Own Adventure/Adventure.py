
#Play again 
def playagain():

    answer = input("Play again? Y or N \n").upper().strip()

    if answer == "Y":

        print("Okay!")
        barkeep_patron_outside()
    
    elif answer == "N":

        print("Goodbye!")

    else:
        print("INVALID ANSWER! GAME OVER!")
        endgame()
        
#Endgame
def endgame():

    print("GAME OVER! THANK YOU FOR PLAYING!")

#Opening paragraph and first choice set
def barkeep_patron_outside():

    print()
    print("""
    You enter a bustling tavern, named Catnip Kitties, that is filled to the brim with all kinds of people.
    You see the bar to the left of you, completly full of patrons laughing, drinking, and eying the pretty
    Tabaxi barkeep who is drying a rack of beer mugs with a white towel. In front of you, you see several
    large table with parties of adventurers who are watching an elven bard on stage performing a tall tale 
    for their viewing pleasure. Above the stage, you see an upper level and hidden slightly in the shadows 
    is a large white Tabaxi, whom you assume to be the patron. \n
    """)

    #User choice
    bar_patron_out = input("""
    Would you like to talk to: the BARKEEP, who seems uncomfortable with the level of attention she's getting;
    the PATRON, who is on the second level above you, surveying his tavern; or exit the tavern and go OUTSIDE
    to enjoy the fresh spring evening air? \n
    """).upper().strip()
    print()

    #If statements
    if bar_patron_out == "BARKEEP":

        barkeep()
    
    elif bar_patron_out == "PATRON":

        patron()
    
    elif bar_patron_out == "OUTSIDE":

        outside()
    
    else:

        print("INVALID ANSWER. GAME OVER!")
        playagain()

#Barkeep Choices
def barkeep():

    print("""
    You approach the barkeep where she is drying the mugs off to the side of where the rowdy men are sitting and
    drinking. You observe her to be of the tabby coloring, with a bright orange fur spot over her left eye and the 
    tips of her ears colored white. Upon your approach, she places down the mug she was drying and slings the drying 
    towel over her shoulder. "What can I get for you this evening?" she asks you. Before you can give her your answer,
    a firm hand grabs your shoulder and forces you to spin around to face a large, brute of an Orc who growls at you 
    before shoving you aside and gruffly stating his drink order. \n
    """)

    #User choices
    wait_brawl = input("Do you WAIT your turn or do you start a BRAWL with the Orc? \n").upper().strip()
    print()

    #If statements
    if wait_brawl == "WAIT":
        wait(second_choice)
    
    elif wait_brawl == "BRAWL":
        second_choice = input("Do you stand in FRONT of the Orc or BEHIND the Orc? \n").upper().strip()
        brawl()
    
    else:

        print("INVALID ANSWER. GAME OVER!")
        playagain()

#Wait choices
def wait():

    print("""
    You decide to to politely wait your turn, as the idea of angering this Orc gives you flashbacks to the last time 
    you watched one of your previous party companions anger an Orc. The small Gnome was promptly crushed by a solid
    hammer fist to the top of their head. 

    Once the Orc leaves, you approach the barkeep again and ask if she has anything on the quest board. She nods and
    says that there are two active quests that the tavern is sponsoring. The first quest is locating a missing NECKLACE
    that was lost somewhere between the tavern and the nearest town to the south, about 20 miles away. The second quest
    is to identify and eradicate the MIMICS in the basement that somehow managed to slip in with the last supply shipment. \n
    """) 

    #User choices
    necklace_mimics = input("Do you look for the lost NECKLACE or defeat the MIMICS in the basement? \n").upper().strip()
    print()

    #If statements
    if necklace_mimics == "NECKLACE":

        print(""" 
        You accept the lost necklace quest and after reading the description of the item, you exit the tavern and cast the
        spell, "Locate Object." You get a sense that the necklace is several miles south, towards the nearest town. Traversing
        the worn dirt path, you easily find the necklace on the side of the road and pick it up. You feel your hand and arm 
        that is holding the necklace begin to burn. The feeling of hot daggers digging into your skin, slowly etching runes 
        deep into the tissues of your arm. Screams erupt from your mouth as you writhe in pain on the dirt road, a cloud of 
        dust kicking up in the air from all your movement. After what seems like an eternity, the pain begins to fade until
        it's a subtle heat under your skin. A faint whisper can be heard in the back of your mind that compels you to put on
        the necklace and return it to its rightful owner, who you get the sense is not currently in the tavern. Having picked 
        up a cursed necklace without identifying it first, you are now trapped under its contract until you find its rightful
        owner. \n
        """)

        endgame()
        playagain()

    elif necklace_mimics == "MIMICS":

        print(""" 
        The barkeep leads you to the basement door and unlocks it for you. Lighting a spare torch from your backpack, you head
        down the wooden stairs to the chilly basement below. Drawing your sword, you start poking random boxes, bags, and other
        objects that are in the basement until you find one that snaps back at the tip of your blade with teeth. After a few 
        minutes, you only find four small mimics which were easily eradicated with your blade and you return up the stairs to 
        the barkeep, who is thankful for your help. She gives you 5 silver pieces and offers a meal on the house for your efforts. \n
        """)

        endgame()
        playagain()

    else:
        print("INVALID ANSWER! GAME OVER!")
        playagain()
     
#Brawl Choices
def brawl():

    print(""" 
    How dare this Orc push you aside and interrupt your turn with the barkeep! You were there first, after all. With anger welling
    up inside you, the urge to lash out at this Orc or anyone who dares to cross you right now starts seeming more and more like a
    good idea. \n
    """)

    #User Choice
    fireball_sword = input("Do you cast FIREBALL at the Orc or do you draw your SWORDS? \n").upper().strip()
    print()

    #If statements
    if fireball_sword == "FIREBALL":
        
        print(""" 
        Deciding to cast Fireball at the Orc, you extend your hand and begin to chant quietly. Flames start to gather around your arm
        and lick their way up to the palm of your hand and gather into the shape of a ball. It continues to grow until it is slightly 
        bigger than your hand. Those of the customers that noticed what you were doing rush up to you and try and restrain you before 
        you can launch your spell, but they are just a second too late. 
        
        The fireball hits the Orc quare in the back and expands to what seems to be an infinite size. The light from the explosion 
        blinds you and the force of the spell's shockwave sends you flying backwards through the wall behind you and into the 
        forest surrounding the tavern. After what seems like an eternity, you open your eyes and are greeted by the sight of a 
        giant crater where the tavern used to be. 

        Because of your decision to cast Fireball, all of the customers and staff inside the building were incinerated and the 
        building turned to smoldering rubble. \n
        """)

        endgame()
        playagain()
    
    elif fireball_sword == "SWORDS":

        print(""" 
        As the Orc steps in front of you, you step slightly to his left and draw your twin short swords. "Hey big guy!"
        you shout, catching the Orc's attention. "You don't get to push people around just because you're big. It's 
        gonna cost you dearly one of these days."

        The other customers hear your words and shout in agreement with you, as the Orc seems to be a regular who often
        pushes everyone out of his way, simply because he is bigger than they are. Seeing that your swords are drawn, 
        more people draw their weapons and start attacking the Orc before you can. As more people join, they start to 
        fight customers other than the Orc and a brawl breaks out in the tavern. 
        
        The Orc swings wildly at you in a rage, as you are the once that incited the brawl against him. You manage to
        block the first hit but are too slow to block the second swing, which knocks you off the floor and into an 
        occupied table, knocking you out completely. \n
        """)

        endgame()
        playagain()

    else:
        print("INVALID ANSWER! GAME OVER!")
        playagain()
    
#Patron Choices
def patron():

    print(""" 
    You decide to head up the stairs that are next to the stage and speak with the Tabaxi in the shadows. After
    introducing yourself, it seems that your hunch is correct and this large, white and burly Tabaxi male is
    the patron of the Catnip Kitties. He thanks you for coming here and providing his small tavern your 
    business and offers you a deal for a free two nights of room and board in return for making a deal with him.

    You get the sense that this is a common offer for newcomers to the tavern to procure future business from them.
    He gives you the option to either deliver a particularly important MESSAGE to his ailing mother in the 
    mountainous village to the west, that is several days journey, or you can PERFORM on stage after the current
    performer is over with. If you perform well, he may give you more than two days free stay. \n
    """)

    #User Choice
    msg_perform = input("Will you deliver the MESSAGE or PERFORM on stage? \n").upper().strip()
    print()

    #If statements
    if msg_perform == "MESSAGE":

        message()

    elif msg_perform == "PERFORM":

        perform()
    
    else:
        
        print("INVALID ANSWER! GAME OVER!")
        playagain()
    
#Message Choices
def message():

    print(""" 
    You gladly accept to deliver the message to his ailing mother and agree to start your journey in two days
    time, since you needed to rest from your last quest. As you head out on your journey to deliver the message,
    you come across a crossroads with a path to the LEFT and a path to the RIGHT. \n
    """)

    #User choice
    left_right = input("Will you take the LEFT path or the RIGHT path? \n").upper().strip()
    print()

    if left_right == "LEFT":

        print(""" 
        You decide to take the left path and continue your journey. After three days of following this road, you
        realize that you are headed away from the mountains and are headed in the wrong direction. You attempt to
        correct your path by taking the roads that appear to lead back towards the mountains and after a total of
        two weeks on the road, you eventually find the moutainous village. 

        Entering the small gates, you immediately ask around for the ailing mother and are told that she passed
        away two days ago from her illness. She had sent out a request two weeks ago to see her children again
        before she died. Opening the letter that you weren't able to deliver, you see that her son had written 
        that he was sorry that he couldn't see her right away because business was flourishing more than
        expected, but he promised to pray for her every day and wanted her to know that he loved her very much.

        The guilt of not having taken the correct path weighs heavily on your heart and you dread returning to 
        the tavern to tell the patron that you failed. \n
        """)

        endgame()
        playagain()
    
    elif left_right == "RIGHT":

        print(""" 
        You decide to take the right path and find yourself at the gates of the small village in three days time. 
        Asking around for the ailing mother, you are directed to her home near the center of town and are greeted
        by several small children bursting through the doors before you can knock on it. 

        A sickly grey, female Tabaxi can be seen just on the inside, lying in bed, and coughing up a storm. Her 
        eyes light up as she sets her sights on you and waves you inside. Her excitement is palpable as you offer
        her the letter from her son. She reads it and her smile falters slightly before it grows even wider. 

        "I'm glad my son's tavern is doing well. It was his dream to own one ever since he was little. I knew
        that he couldn't fufill that dream in a small village like this one. We barely every get visitors,"
        she says with a small sigh. "While I am sad that I will not see him in person one last time, I know 
        that his prayers will lift me up and that he loves me very much. Thank you so much for delivering this
        to me."

        She offers you 3 silver pieces and some of the cookies her grandkids made for her. You are filled with 
        joy, knowing that you were able to do this for her son. \n
        """)

        endgame()
        playagain()

    else:

        print("INVALID ANSWER! GAME OVER!")
        playagain()

#Perform Choices
def perform():

    print(""" 
    You agree to perform on stage after the bard is finished with her story in hopes of gaining more free nights
    of room and board out of this deal. Confident in your abilities to tell a story and weave illusion magic,
    you step up on stage as the bard exits and wait until the crowd's applause dies down.

    Roll a d20. \n
    """)

    #User Choice
    higher_lower = input("Did you get HIGHER or LOWER than a 15? \n").upper().strip()
    print()

    #If statements
    if higher_lower == "LOWER":

        print(""" 
        While your ability to cast illusion magic is solid, your storytelling is currently lacking. The crowd
        can follow the story you tell, but you pause a lot and lose track of where you are in the story - you
        find yourself ranting about an entirely different story than what you started with. After managing to 
        somehow tie it all together, you give a small bow and quickly run off stage, the sounds of hesistant 
        clapping echoing in your ears. Returning upstairs to the patron, you find him laughing at your 
        performance and you feel yourself flush with embarrassment as his large hand claps onto your shoulder.

        "You gave it a solid try and I applaud you for that," he says with a fanged grin. "A deals a deal. You
        get two nights of free room and board." \n
        """)

        endgame()
        playagain()
    
    elif higher_lower == "HIGHER":

        print(""" 
        As the bard exits the stage, you wait for the clapping to die down before you walk onto the stage. 
        You cast your illusion magic and with your most dramatic and compelling voice, you capture your 
        audience's attention as you weave a magical and dangerous tale able fighting wyverns and befriending
        Kobolds in the last dungeon you had traversed. You tell of your party members' bravery during the 
        battle and their clever tactics that helped you to win the day, surviving the fight with some
        wounded, but no losses. 

        As you end the story, the audience roars with delight and rises to their feet to give you a standing
        ovation. Bowing quickly, you exit the stage and pass by a sour bard, who's performance you have 
        upstaged and head upstairs to the patron. His hands on his hips, he declares that you're the best
        storyteller he has ever heard and offers you two weeks free room and board and half-off meals 
        whenever you return to his tavern to eat and rest. 

        Pride fills your chest at your accomplishments and you sleep happily for the entire night. 
        """)

        endgame()
        playagain()
    
    else:

        print("INVALID ANSWER! GAME OVER!")
        playagain()
        
#Outside Choices
def outside():

    print(""" 
    You exit the bustling tavern and into the quiet and slightly chilly spring night. Feeling
    a slight breeze against your face, you lean against the windowsill behind you and sigh. 
    One of the barkeeps' staff, a smaller Halfling male, offers you a warm drink on the house
    while you enjoy the evening stars.

    After a few minutes of stargazing and letting your thoughts wander, you hear a scuffle 
    nearby and the sounds of a small child crying out. \n
    """)

    #User Choice
    sounds_stay = input("Do you go investigate the SOUNDS or do you STAY put at the windowsill? \n").upper().strip()
    print()

    #If statements
    if sounds_stay == "SOUNDS":
        
        sounds()
    
    elif sounds_stay == "STAY":

        stay()
    
    else:

        print("INVALID ANSWER! GAME OVER!")
        playagain()

#Sound Choices
def sounds():

    print(""" 
        Setting your almost empty mug on the windowsill, you unsheathe your sword and rush into 
        the forest that surrounds the tavern towards where you believe the sound to be coming 
        from. As you arrive in a small clearing, you see several bandits surrounding a couple. 

        One of the bandits is holding a small child that is visibly upset in their arms, a 
        sharp blade pressed flat against the child's belly. You wait in the shadows for a 
        moment to observe the situation and notice that these bandits aim to rob the couple
        of their valuables, but are threatening to seriously injure the child if they don't
        cooperate. 

        You decide to step in and attempt to rescue the child, which should hopefilly scare
        off the bandits. 

        Roll a d20. \n
        """)

    #User Choice
    higher_lower = input("Did you roll HIGHER than a 13 or LOWER than a 13? \n").upper().strip()
    print()

    if higher_lower == "LOWER":

        print(""" 
        Your attack comes as a surprise to the group of bandits, most of whom scatter 
        when you rush out from the tree line. However, your attack towards the bandit 
        holding the child misses and the bandit manages to land a solid kick to your
        gut, pushing you away. 

        Realizing that this situation has now become more of a hassle than he previously
        thought, the bandit drops the child and scurries off into the night. You pick up
        the crying child and hand her to her mother, who begins to attempt to soothe her 
        daughter. The husband approaches you and thanks you for the assistance and notes
        that even though all their money had been stolen, they are grateful that their 
        daughter was unharmed. 

        You usher the family to the tavern to stay the night on your dime and keep watch
        over their room till the morning. \n
        """)

        endgame()
        playagain()
    
    elif higher_lower == "HIGHER":

        print(""" 
        Your attack comes as a surprise to the group of bandits, most of whom scatter 
        when you rush out from the tree line. Before the bandit holding the child can
        do anything, the hilt of your sword comes crashing down on the top of his 
        helmet, knocking him out cold. 

        You carefully take the crying child from the bandit's arms and hand her back
        to her mother before searching the bandit's pockets. You find several bags
        of coinage in his pockets and hand them to the couple. They both express
        gratitude to you of saving their daughter and managing to recover what
        had been stolen from them. 

        You usher them back to the tavern to have a safe place to sleep and keep
        watch over their room till morning. \n
        """)
        
        endgame()
        playagain()
    
    else:

        print("INVALID ANSWER! GAME OVER!")
        playagain()
    
#Stay Choices    
def stay():
    
    print("""
    You assume the sounds coming from the forest are that of animals and that the
    crying child you heard was most likely coming from inside the tavern. Perhaps
    there were some inside that you had simply not noticed when you first walked
    in. 

    Setting your empty mug down on the windowsill, you hear the sounds from earlier
    again, but this time there is a distinct sound of a male voice calling out for 
    help. \n
    """)

    #User Choice
    investigate_nothing = input("""
    Do you INVESTIGATE the sounds or do you remain put and do NOTHING? \n
    """).upper().strip()

    #If statements
    if investigate_nothing == "INVESTIGATE":

        print(""" 
        The sound of a male voice calling for help sets your alarm bells off
        and you quickly unsheathe your twin short swords and rush towards where
        you hear the call coming from. Upon entering a clearing, you see the 
        remaining few bandits that you assume just robbed this couple running 
        off through the tree line. 

        Before you, you see a small child sitting on the ground, crying 
        profusely as she sits next to a fallen form. A hunched over figure wails
        in agony as it tries to shake this form. You realize that it's a
        husband grieving the loss of of his wife and their daughter, not
        understanding why her mother isn't responding to her cries like she
        normally would. 

        Guilt seizes your heart as you realize you initially heard them being
        robbed and you take a few steps backward as you come to terms with the
        fact that had you responded sooner, no one would've died. \n
        """)

        endgame()
        playagain()
    
    elif investigate_nothing == "NOTHING":

        print(""" 
        You hear a male voice calling for help and assume that the local guard
        patrol will investigate the situation. Deciding to take a late-night
        stroll in the woods to clear your head before you rest, you walk for 
        a little while before coming to a small clearing. 

        You see a large pool of fresh blood in the center of the clearing and
        in that pool you see three bodies that appear to have been thrown atop
        one another. You hear footsteps approaching you. Looking up, you see 
        a small group of bandits that seem to jeer at you as you realize 
        you're surrounded. 

        One of the bandits steps forward, his sword haphazardly slund behind
        his neck and across his shoulder. He comments on how stupid you are to
        be walking around these parts late at night alone and brags about a 
        couple they just robbed.

        "One of them was stupid enough to run right into my buddy's blade here,
        trying to save their daughter. Look what happened to them after they decided
        not to listen," he says with a sneer and a laugh, before pointing his 
        sword at you and placing the tip under your chin. "Now it's your turn. 
        Give me everything valuable that's on you, or your life is mine." \n
        """)

        endgame()
        playagain()
    
    else:

        print("INVALID ANSWER! GAME OVER!")
        playagain()

#Start Game
if __name__ == "__main__":
    barkeep_patron_outside()