# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Characters

define m = Character("Me", who_color="#515076")
define e = Character("...", who_color="#92323c")

# Images

default head = "base"
default torso = "base"
default arms = "base"

# Audio

# define ahh = "ahhh.wav"
define yell = "yell01.wav"
define rewind = "laughandrewind.wav"
# define forming = "monsterforming.wav"
define part = "monsters_newpartappears.ogg"
define m_main = "monsters_music_main_loop.ogg"
define m_1en = "monsters_back_1stencounter_loop.ogg"
define m_2en = "monsters_back_2ndencounter_loop.ogg"
define m_3en = "monsters_back_3rdencounter_loop.ogg"
define m_3en2 = "monsters_music_overlay_third dialogue_loop.ogg"
define m_reveal = "monsters_fullreveal.ogg"
define m_monster = "monsters_music_reveal_loop.ogg"
define m_alarm = "monsters_alarm.ogg"
define m_choice = "monsters_answer.ogg"

# Other variables

define loop = False
define encounter = 0
define goodness = 0
define blackfade = Fade(0.5, 1.5, 0.5)

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # Disclaimer
    play music m_main fadeout 0.5 fadein 0.5
    scene ph_dark

    e "Warning: this game deals with sensitive topics such as mental health. Please be safe."

    scene bg_roomevening

    # Opening scene in the waking world.

    m "I hope I'll get some sleep tonight."

    scene ph_room

    m "There's been so much going on lately that my sleeping schedule has gotten all messed up."
    m "{b}Sigh{/b}. I wish my brain would just shut up..."

label dream:

    # Before encounters start, player sees their own reflection

    $ encounter = 0

    scene bg_mirror with fade

    if loop == False:
        m "...?"
        m "Is this another one of those lucid dreams...?"
    # else:
        # m "I already did this!"
    play sound "introduction.wav"
    e "Ah, great to see you again."

    show c_humanmid with vpunch

    m "Oh no..."
    m "Please just leave me alone already."
    e """Don't think so! Visiting your dreams is a favourite hobby of mine.

    Now let's dive deep into those delicious memories of yours!

    Hmm...

    Which one should I pick?

    A-ha! This one!"""

label first_encounter:

    # Scene at house during the night

    $ encounter = 1

    play m_layer m_1en fadein 1.0
    scene ph_streetnight with fade
    # show ph_humancrop at right

    e """You were having a lovely little party with a few of your friends.

    Relaxing, joshing around. Just a barrel of laughs, really.

    You decided to try your hand at joking. Remind me, what is it that you said?"""
    m """...

    I said... That Sam is way too busy with his dogs to get a date.

    I wasn't being serious!"""
    e """Well, Sam didn't seem to find your joke funny, and neither did any of the others.

    I'm ever so forgetful, what is it that you did next?"""

menu:

    "I called myself a disappointment.": # Self hatred
        $ arms = "hatred"
        stop m_layer
        jump mirror

    "I accused Sam of not being able to take a joke.": # Lashing out
        $ arms = "lashing"
        stop m_layer
        jump mirror

    "I said that I neededed to pee, but actually left the party.": # Avoidance
        $ arms = "avoidance"
        stop m_layer
        jump mirror

label second_encounter:

    # House during the day

    $ encounter = 2

    play m_layer m_2en fadein 1.0
    scene ph_streetday with fade
    # show ph_humancrop at right

    e """You were really eager to ask for a hang out

    but once they told you about their other plans, you just couldn't take it.

    You pitied yourself so much that you let your emotions get the best of you.

    Refresh my memory, what is it that you told them?"""

menu:

    "Why does nobody like me...?": # Self hatred
        $ torso = "hatred"
        stop m_layer
        jump mirror

    "Honestly, you never have time for me! Why the hell is that??": # Lashing out
        $ torso = "lashing"
        stop m_layer
        jump mirror

    "Whatever, I have better things to do anyway...": # Avoidance
        $ torso = "avoidance"
        stop m_layer
        jump mirror

label third_encounter:

    # Scene at picnic

    $ encounter = 3

    play m_layer m_3en fadein 1.0
    play m_layer2 m_3en2 fadein 1.0
    scene ph_picnic with fade
    # show ph_humancrop at right

    e """You let it slip that River is bi.

    Of course everyone took it well, you absolutely {i}knew{/i} that they would.

    Not your secret to tell, though. And you blamed it on poor Wesley.

    That lie didn't hold up for very long.

    When River found out, you did the {i}funniest{/i} thing."""

menu:

    "I said that maybe they should throw me out of their life since I'm so horrible.": # Self hatred
        $ head = "hatred"
        jump mirror

    "I accused River of burdening me with their secrets.": # Lashing out
        $ head = "lashing"
        jump mirror

    "I claimed it was no big thing, really.": # Avoidance
        $ head = "avoidance"
        jump mirror

label mirror:

    # Scene where you return from the encounters to chat with your monster

    scene bg_mirror

    show c_humanmid

    if encounter == 1:
        m "... And it solved nothing..."
        play sound part
        show image "c_[arms]armsmid.png" with vpunch
        hide image "c_[arms]armsmid.png"
        e "Of course it didn't."
        e "How about another one?"
        e "You were feeling a bit lonely and reached out to your dear friend Tanner."
        jump second_encounter
    elif encounter == 2:
        m "I know I'm not the only person in their life..."
        m "My actions are only driving them further away from me..."
        play sound part
        show image "c_[torso]torsomid.png" with vpunch
        hide image "c_[torso]torsomid.png"
        e """{font=RockSalt-Regular.ttf}Keep this up and you'll end up all alone.{/font}

        You can think all you want about not knowing better or good intentions.

        Ignorance and intentions don’t excuse you.

        Now, let's see."""
        m "Isn't this enough already? I know what I did..."
        e "No getting out of this one. It's my favourite!"
        jump third_encounter
    elif encounter == 3:
        m "I wish I'd never done it..."
        play sound part
        show image "c_[head]headmid.png" with vpunch
        hide image "c_[head]headmid.png"
        e "Wishing doesn't change the fact that you {i}really{/i} fucked up"
        show ph_vignette1
        e "{font=RockSalt-Regular.ttf}Now...{/font}" # glitch text?
        stop music
        stop m_layer
        stop m_layer2
        show ph_vignette2
        m "..."
        jump conclusion

label conclusion:

    # Scene where you face your monster

    scene ph_dark with fade

    play music m_monster fadein 1.0 fadeout 1.0
    play sound m_reveal

    show image "c_[torso]torsomid.png" with vpunch
    show image "c_[torso]torsomid.png" with hpunch
    show image "c_[torso]torsomid.png" with pixellate
    show image "c_[arms]armsmid.png" with vpunch
    show image "c_[arms]armsmid.png" with hpunch
    show image "c_[arms]armsmid.png" with pixellate
    show image "c_[head]headmid.png" with vpunch
    show image "c_[head]headmid.png" with hpunch
    show image "c_[head]headmid.png" with pixellate

    e """{font=RockSalt-Regular.ttf}Ahh that feels better.{/font}

    You might just regret letting me all the way in.

    I'm here to deliver your final {font=RockSalt-Regular.ttf}judgement{/font}

    Let's see if you've learned anything!

    Oh, I do {i}love{/i} a good hypothetical.

    Now, Imagine somebody owes you money.
    You need the money back badly, but they can’t afford it. What would you do?"""

    define second = "I see. Oh, this is one that happened to me the other day. Your friend has made you some bone ‘n gut soup with eyes on top. That stuff definitely isn’t for you humans. What would you do?"
    define third = "Your friend posts on social media that their landlord illegally cut their water. What would you do?"

menu:
    "As I know they’ll pay me back as soon as they can, I’ll figure out something else.":
        $ goodness = goodness + 20
        e "[second]"
        jump B
    "Well I guess we’re both fucked then. What could I even do?":
        $ goodness = goodness + 5
        e "[second]"
        jump B
    "I’d go rob a bank.":
        $ goodness = goodness - 20
        e "[second]"
        jump B

menu B:
    "I would thank them for the kind gesture, but decline the soup.":
        $ goodness = goodness + 20
        e "Last one. Better be careful."
        e "Your eyes would make for lovely garnish."
        e "[third]"
        jump C
    "I’d take the soup and throw it away.":
        $ goodness = goodness + 5
        e "Last one. Better be careful."
        e "Your eyes would make for lovely garnish."
        e "[third]"
        jump C
    "I’d take it and feed it to puppies and orphans.":
        $ goodness = goodness - 20
        e "Last one. Better be careful."
        e "Your eyes would make for lovely garnish."
        e "[third]"
        jump C

menu C:
    "I’ll offer them the use of my water in the meantime, it’s no problem for me.":
        $ goodness = goodness + 20
        if goodness < 15:
            jump ending_bad
        elif goodness < 30:
            e "Seems you need a refresher."
            e "It’s almost like you don’t even want this to end."
            play sound rewind
            m "No, please don't! I can't do this ag..."
            $ loop = True
            play music m_main fadein 1.0
            jump dream
        else:
            jump ending_good
    "React with a sad emoji. Sucks to be them.":
        $ goodness = goodness + 5
        if goodness < 15:
            jump ending_bad
        elif goodness < 30:
            e "Seems you need a refresher."
            e "It’s almost like you don’t even want this to end."
            play sound rewind
            m "No, please don't! I can't do this ag..."
            $ loop = True
            play music m_main fadein 1.0
            jump dream
        else:
            jump ending_good
    "Oh, I dunno, I guess I’ll go poison the town water supply!":
        $ goodness = goodness - 20
        if goodness < 15:
            jump ending_bad
        elif goodness < 30:
            e "Seems you need a refresher."
            e "It’s almost like you don’t even want this to end."
            play sound rewind
            m "No, please don't! I can't do this ag..."
            $ loop = True
            play music m_main fadein 1.0
            jump dream
        else:
            jump ending_good

label ending_good:

    # Good ending where you wake up happy


    e """How curious... It seems like there is some hope for you after all.

    You’re just a human. Of course you’re going to make mistakes.

    Though I’ll be a bit bored if I can’t visit you anymore…

    But I suppose it’s interesting seeing you come to some realisations.

    Now...

    It's time for you to {b}Wake Up{/b}"""

    stop music fadeout 0.5
    play sound m_alarm
    scene bg_roomday with blackfade

    m """Huh?

    How strange...

    But at the same time...

    I feel like I just opened my eyes for the first time."""

    return

label ending_bad:

    # Bad ending where you get eaten?

    e "After everything, you’re still not taking this seriously?"

    scene ph_bad with vpunch

    play sound yell
    e "{color=#c50000}{font=RockSalt-Regular.ttf}You’ve disappointed me for the last time.{/font}{/color}" with vpunch

    show image "torso_[torso]_end.png" with vpunch
    show image "arms_[arms]_end.png" with vpunch
    show image "head_[head]_end.png" with vpunch

    m "AARGH!!!"

    scene ph_dark with fade

    return
return
