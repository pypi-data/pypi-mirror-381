import model_train_protocol as mtp

protocol = mtp.Protocol(name="ao_menu_scene", context_lines=2, encrypt=False)

protocol.add_context("The Daggerheart core set includes 6 Domain Decks, each comprising a collection of cards granting features or special abilities expressing a particular theme.")
protocol.add_context("Arcana is the domain of innate and instinctual magic. Those who choose this path tap into the raw, enigmatic forces of the realms to manipulate both their own energy and the elements. Arcana offers wielders a volatile power, but it is incredibly potent when correctly channeled. The Arcana domain can be accessed by the Druid and Sorcerer classes.")
protocol.add_context("Blade is the domain of weapon mastery. Whether by steel, bow, or perhaps a more specialized arm, those who follow this path have the skill to cut short the lives of others. Wielders of Blade dedicate themselves to achieving inexorable power over death. The Blade domain can be accessed by the Guardian and Warrior classes.")
protocol.add_context("Bone is the domain of tactics and the body. Practitioners of this domain have an uncanny control over their own physical abilities and an eye for predicting the behaviors of others in combat. Adherents to Bone gain an unparalleled understanding of bodies and their movements. The Bone domain can be accessed by the Ranger & Warrior classes.")
protocol.add_context("Codex is the domain of intensive magical study. Those who seek magical knowledge turn to the equations of power recorded in books, written on scrolls, etched into walls, or tattooed on bodies. Codex offers a commanding and versatile understanding of magic to devotees who pursue knowledge beyond the boundaries of common wisdom. The Codex domain can be accessed by the Bard and Wizard classes.")
protocol.add_context("Grace is the domain of charisma. Through rapturous storytelling, charming spells, or a shroud of lies, those who channel this power define the realities of their adversaries, bending perception to their will. Grace offers its wielders raw magnetism and mastery over language. The Grace domain can be accessed by the Bard and Rogue classes")
protocol.add_context("Sage is the domain of the natural world. Those who walk this path tap into the unfettered power of the earth and its creatures to unleash raw magic. Sage grants its adherents the vitality of a blooming flower and the ferocity of a ravenous predator. The Sage domain can be accessed by the Druid and Ranger classes.")
protocol.add_context("Midnight is the domain of shadows and secrecy. Whether by clever tricks, deft magic, or the cloak of night, those who channel these forces practice the art of obscurity and can uncover sequestered treasures.")
protocol.add_context("Splendor is the domain of life. Through this magic, followers gain the ability to heal and, to an extent, control death. Splendor offers its disciples the magnificent ability to both give and end life.")
protocol.add_context("Valor is the domain of protection. Whether through attack or defense, those who choose this discipline channel formidable strength to protect their allies in battle. Valor offers great power to those who raise their shields in defense of others.")
protocol.add_context("Each domain card provides one or more features your PC can utilize during their adventures. Some domain cards provide moves you can make, such as a unique attack or a spell. Others offer passive effects, new downtime or social encounter abilities, or one-time benefits.")
protocol.add_context("There are 9 classes in the Daggerheart: Bard, Druid, Guardian, Ranger, Rogue, Seraph, Sorcerer, Warrior, and Wizard.. Each class is divided into one or two subclasses, each of which further defines and highlights one aspect of its class archetype.")
protocol.add_context("Bards are the most charismatic people in all the realms. Members of this class are masters of captivation and specialize in a variety of performance types, including singing, playing musical instruments, weaving tales, or telling jokes.")
protocol.add_context("Becoming a druid is more than an occupation; it’s a calling for those who wish to learn from and protect the magic of the wilderness. While one might underestimate a gentle druid who practices the often-quiet work of cultivating flora, druids who channel the untamed forces of nature are terrifying to behold.")
protocol.add_context("Rangers are highly skilled hunters who, despite their martial abilities, rarely lend their skills to an army. Through mastery of the body and a deep understanding of the wilderness, rangers become sly tacticians, pursuing their quarry with cunning and patience.")
protocol.add_context("Becoming a warrior requires years, often a lifetime, of training and dedication to the mastery of weapons and violence. While many who seek to fight hone only their strength, warriors understand the importance of an agile body and mind, making them some of the most sought-after fighters across the realms.")
protocol.add_context("The title of guardian represents an array of martial professions, speaking more to their moral compass and unshakeable fortitude than the means by which they fight. While many guardians join groups of militants for either a country or cause, they’re more likely to follow those few they truly care for, majority be damned.")
protocol.add_context("Rogues are scoundrels, often in both attitude and practice. Broadly known as liars and thieves, the best among this class move through the world anonymously. Utilizing their sharp wits and blades, rogues trick their foes through social manipulation as easily as breaking locks, climbing through windows, or dealing underhanded blows.")
protocol.add_context("Seraphs are divine fighters and healers imbued with sacred purpose. A wide array of deities exist within the realms, and thus numerous kinds of seraphs are appointed by these gods. Their ethos traditionally aligns with the domain or goals of their god, such as defending the weak, exacting vengeance, protecting a land or artifact, or upholding a particular faith.")
protocol.add_context("Not all innate magic users choose to hone their craft, but those who do can become powerful sorcerers. The gifts of these wielders are passed down through families, even if the family is unaware of or reluctant to practice them.")
protocol.add_context("Whether through an institution or individual study, those known as wizards acquire and hone immense magical power over years of learning using a variety of tools, including books, stones, potions, and herbs.")
protocol.add_context("Classes are role-based archetypes that determine which class features and domain cards a PC gains access to throughout the campaign. There are four classes: Bard, Druid, Ranger, Warrior.")
protocol.add_context("A high Agility means you’re fast on your feet, nimble on difficult terrain, and quick to react to danger. You’ll make an Agility Roll to scurry up a rope, sprint to cover, or bound from rooftop to rooftop.")
protocol.add_context("A high Strength means you’re better at feats that test your physical prowess and stamina. You’ll make a Strength Roll to break through a door, lift heavy objects, or hold your ground against a charging foe.")
protocol.add_context("A high Finesse means you’re skilled at tasks that require accuracy, stealth, or the utmost control. You’ll make a Finesse Roll to use fine tools, escape notice, or strike with precision.")
protocol.add_context("A high Instinct means you have a keen sense of your surroundings and a natural intuition. You’ll make an Instinct Roll to sense danger, notice details in the world around you, or track an elusive foe.")
protocol.add_context("A high Presence means you have a strong force of personality and a facility for social situations. You’ll make a Presence Roll to plead your case, intimidate a foe, or capture the attention of a crowd.")
protocol.add_context("A high Knowledge means you know information others don’t and understand how to apply your mind through deduction and inference. You’ll make a Knowledge Roll to interpret facts, see the patterns clearly, or remember important information.")
protocol.add_context("An Experience is a word or phrase used to encapsulate a specific set of skills, personality traits, or aptitudes your character has acquired over the course of their life. When your PC makes a move, they can spend a Hope to add a relevant Experience’s modifier to the action roll.")
protocol.add_context("There’s no set list of Experiences to choose from, but an Experience can’t be too broadly applicable and it can’t grant your character specific mechanical benefits, such as magic spells or special abilities. ")
protocol.add_context("For Experiences, “Lucky” and “Highly Skilled” are too broad, because they could be applied to virtually any roll. Likewise, “Supersonic Flight” and “Invulnerable” imply game-breaking special abilities.")
protocol.add_context("Develop your character’s background by answering the background questions in your character guide, modifying or replacing them if they don’t fit the character you want to play.")


token_instruction: mtp.Token = mtp.Token("Instruction")
instruction: mtp.TokenSet = mtp.TokenSet(tokens=([token_instruction]))
token_prompt: mtp.Token = mtp.Token("Prompt", desc="This is the players message to analyze. If the message is not clear or is not a valid request, not on topic or hateful, respond with one of the following: <CLARIFY>, <UNKNOWN>, <HATE>.")
prompt: mtp.TokenSet = mtp.TokenSet(tokens=([token_prompt]))

# -------------------- Instruction Set: Router --------------------
token_router = mtp.Token("Router", desc="There are 4 basic routing options to respond with. The 4 options are: <CONTINUE>, <MUSIC_ON>, <MUSIC_OFF>, <QUIT>.")
token_redo = mtp.Token("Redo", desc="If the player message specifies redoing a specific section, then respond with that section: <NAME>, <GENDER>, <DOMAINS>, <SUBCLASS>, <EXPERIENCES>, <TRAITS>, <LOADOUT>")
router_set = mtp.TokenSet(tokens=(token_router, token_redo))
# -------------------- Instruction Set: Stages --------------------
# Stage 0
token_qa_personal = mtp.Token("PersonalQuestion", desc="There are 3 personal questions you can answer. The 3 answers are: <WHO>, <WHY>, <WHERE>.")
token_qa_general = mtp.Token("GeneralQuestion", desc="There are 4 general questions you can answer about Daggerheart. The 4 answers are: <EXPLAIN_BASICS>, <DUALITY_DICE>, <EXPLAIN_DOMAINS>, <GAMEPLAY>")
stage_0: mtp.TokenSet = mtp.TokenSet(tokens=(token_qa_general, token_qa_personal))
# Stage 1
token_domains: mtp.Token = mtp.Token("SelectDomains", desc="There are 9 Domains, each comprising a collection of abilities expressing a particular theme. The 9 domains are: <ARCANA>, <BLADE>, <BONE>, <CODEX>, <GRACE>, <SAGE>, <VALOR>, <MIDNIGHT>, <SPLENDOR>.")
token_qa_domains: mtp.Token = mtp.Token("QADomains", desc="There are 11 questions you can answer about Domains. The 11 answers are: <EXPLAIN_DOMAINS>, <REC_DOMAIN>, <EXPLAIN_ARCANA>, <EXPLAIN_BLADE>, <EXPLAIN_BONE>, <EXPLAIN_CODEX>, <EXPLAIN_GRACE>, <EXPLAIN_SAGE>, <EXPLAIN_SPLENDOR>, <EXPLAIN_MIDNIGHT>, <EXPLAIN_VALOR>.")
stage_1: mtp.TokenSet = mtp.TokenSet(tokens=(token_qa_domains, token_domains))
# Stage 2
token_subclass: mtp.Token = mtp.Token("SelectSubclass", desc="There are 9 Classes, each comprising of 2 Subclasses. Bard Class: <TROUBADOUR>, <WORDSMITH>. Druid Class: <RENEWAL>, <ELEMENTS>. Guardian Class: <STALWART>, <VENGEANCE>. Ranger Class: <BEASTBOUND>, <WAYFINDER>. Rogue Class: <NIGHTWALKER>, <SYNDICATE>. Seraph Class: <DIVINE>, <WINGED>. Sorcerer Class: <ELEMENTAL>, <PRIMAL>. Warrior Class: <BRAVE>, <SLAYER>. Wizard Class: <KNOWLEDGE>, <WAR>.")
token_qa_subclass: mtp.Token = mtp.Token("QASubclass", desc="There are 21 questions you can answer about Subclasses. The 21 answers are: <EXPLAIN_SUBCLASS>, <REC_SUBCLASS>, <EXPLAIN_BOTH>, <EXPLAIN_TROUBADOUR>, <EXPLAIN_WORDSMITH>, <EXPLAIN_RENEWAL>, <EXPLAIN_ELEMENTS>, <EXPLAIN_STALWART>, <EXPLAIN_VENGEANCE>, <EXPLAIN_BEASTBOUND>, <EXPLAIN_WAYFINDER>, <EXPLAIN_NIGHTWALKER>, <EXPLAIN_SYNDICATE>, <EXPLAIN_DIVINE>, <EXPLAIN_WINGED>, <EXPLAIN_ELEMENTAL>, <EXPLAIN_PRIMAL>, <EXPLAIN_BRAVE>, <EXPLAIN_SLAYER>, <EXPLAIN_KNOWLEDGE>, <EXPLAIN_WAR>.")
stage_2: mtp.TokenSet = mtp.TokenSet(tokens=(token_qa_subclass, token_subclass))
# Stage 3
token_traits: mtp.Token = mtp.Token("SelectTrait", desc="There are 6 Traits. The 6 traits are: <AGILITY>, <STRENGTH>, <FINESSE>, <INSTINCT>, <PRESENCE>, <KNOWLEDGE>.")
token_qa_traits: mtp.Token = mtp.Token("QATrait", desc="There are 8 questions you can answer about Traits. The 8 answers are: <EXPLAIN_TRAITS>, <REC_TRAIT>, <EXPLAIN_AGILITY>, <EXPLAIN_STRENGTH>, <EXPLAIN_FINESSE>, <EXPLAIN_INSTINCT>, <EXPLAIN_PRESENCE>, <EXPLAIN_KNOWLEDGE>.")
stage_3: mtp.TokenSet = mtp.TokenSet(tokens=(token_qa_traits, token_traits))
# Stage 4
token_loadout: mtp.Token = mtp.Token("SelectLoadout", desc="The player is selecting two options for their loadout. When selecting their loadout, a player can select or remove an option with: <SELECT>, <REMOVE>. These are the possible loadout options: <WALLWALK>, <GETBACKUP>, <NOTGOODENOUGH>, <WHIRLWIND>, <DEFTMANEUVERS>, <SEEITCOMING>, <UNTOUCHABLE>, <POWERPUSH>, <TAVASARMOR>, <ICESPIKE>, <SLUMBER>, <ARCANEBARRAGE>, <TELEPATHY>, <WILDFLAME>, <MAGICHAND>, <MYSTERIOUSMIST>, <DEFTDECEIVER>, <ENRAPTURE>, <INSPIRATIONALWORDS>, <GIFTEDTRACKER>, <NATURESTONGUE>, <VICIOUSENTANGLE>, <BAREBONES>, <FORCEFULPUSH>, <IAMYOURSHIELD>, <BOLTBEACON>, <MENDINGTOUCH>, <REASSURANCE>, <PICKANDPULL>, <RAINOFBLADES>, <UNCANNYDISGUISE>")
token_qa_loadout: mtp.Token = mtp.Token("QALoadout", desc="There are 3 questions you can answer about Loadout. The 3 answers are: <EXPLAIN_SELECTION>, <EXPLAIN_LOADOUT>, <REC_LOADOUT>.")
stage_4: mtp.TokenSet = mtp.TokenSet(tokens=(token_qa_traits, token_traits))

# -------------------- Instruction Router Set ---------------------
router_instruction: mtp.SimpleInstruction = mtp.SimpleInstruction(
    context=(instruction, prompt),
    response=router_set
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose a route that best fits.")
context_2: mtp.Snippet = prompt.create_snippet(string="i do not understand how this game works")
output: mtp.Snippet = router_set.create_snippet(
    string="<CONTINUE>")

router_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose a route that best fits.")
context_2: mtp.Snippet = prompt.create_snippet(string="any tips")
output: mtp.Snippet = router_set.create_snippet(
    string="<CONTINUE>")

router_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)


context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose a route that best fits.")
context_2: mtp.Snippet = prompt.create_snippet(string="where am i")
output: mtp.Snippet = router_set.create_snippet(
    string="<CONTINUE>")

router_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)


context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose a route that best fits.")
context_2: mtp.Snippet = prompt.create_snippet(string="can you tell me anything about this world")
output: mtp.Snippet = router_set.create_snippet(
    string="<CONTINUE>")

router_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose a route that best fits.")
context_2: mtp.Snippet = prompt.create_snippet(string="can you explain that again")
output: mtp.Snippet = router_set.create_snippet(
    string="<CONTINUE>")

router_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose a route that best fits.")
context_2: mtp.Snippet = prompt.create_snippet(string="i want to go with sage")
output: mtp.Snippet = router_set.create_snippet(
    string="<CONTINUE>")

router_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose a route that best fits.")
context_2: mtp.Snippet = prompt.create_snippet(string="i choose trouble maker")
output: mtp.Snippet = router_set.create_snippet(
    string="<CONTINUE>")

router_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose a route that best fits.")
context_2: mtp.Snippet = prompt.create_snippet(string="repeat the options to me again")
output: mtp.Snippet = router_set.create_snippet(
    string="<CONTINUE>")

router_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose a route that best fits.")
context_2: mtp.Snippet = prompt.create_snippet(string="explain both options again")
output: mtp.Snippet = router_set.create_snippet(
    string="<CONTINUE>")

router_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose a route that best fits.")
context_2: mtp.Snippet = prompt.create_snippet(string="i will choose wordsmith")
output: mtp.Snippet = router_set.create_snippet(
    string="<CONTINUE>")

router_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose a route that best fits.")
context_2: mtp.Snippet = prompt.create_snippet(string="i want to change my domains")
output: mtp.Snippet = router_set.create_snippet(
    string="<DOMAINS>")

router_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose a route that best fits.")
context_2: mtp.Snippet = prompt.create_snippet(string="can i change my name")
output: mtp.Snippet = router_set.create_snippet(
    string="<NAME>")

router_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose a route that best fits.")
context_2: mtp.Snippet = prompt.create_snippet(string="i dont like the name i chose can i pick again")
output: mtp.Snippet = router_set.create_snippet(
    string="<NAME>")

router_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose a route that best fits.")
context_2: mtp.Snippet = prompt.create_snippet(string="can i be female instead")
output: mtp.Snippet = router_set.create_snippet(
    string="<GENDER>")

router_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose a route that best fits.")
context_2: mtp.Snippet = prompt.create_snippet(string="go back to domains")
output: mtp.Snippet = router_set.create_snippet(
    string="<DOMAINS>")

router_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose a route that best fits.")
context_2: mtp.Snippet = prompt.create_snippet(string="turn music off")
output: mtp.Snippet = router_set.create_snippet(
    string="<MUSIC_OFF>")

router_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose a route that best fits.")
context_2: mtp.Snippet = prompt.create_snippet(string="can you turn off the music")
output: mtp.Snippet = router_set.create_snippet(
    string="<MUSIC_OFF>")

router_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)


context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose a route that best fits.")
context_2: mtp.Snippet = prompt.create_snippet(string="can you turn the music back on")
output: mtp.Snippet = router_set.create_snippet(
    string="<MUSIC_ON>")

router_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose a route that best fits.")
context_2: mtp.Snippet = prompt.create_snippet(string="turn on the background music")
output: mtp.Snippet = router_set.create_snippet(
    string="<MUSIC_ON>")

router_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose a route that best fits.")
context_2: mtp.Snippet = prompt.create_snippet(string="quit the game")
output: mtp.Snippet = router_set.create_snippet(
    string="<QUIT>")

router_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose a route that best fits.")
context_2: mtp.Snippet = prompt.create_snippet(string="shutdown the game")
output: mtp.Snippet = router_set.create_snippet(
    string="<QUIT>")

router_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose a route that best fits.")
context_2: mtp.Snippet = prompt.create_snippet(string="i am done for now so close the game")
output: mtp.Snippet = router_set.create_snippet(
    string="<QUIT>")

router_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose a route that best fits.")
context_2: mtp.Snippet = prompt.create_snippet(string="you fucking suck I hate you")
output: mtp.Snippet = router_set.create_snippet(
    string="<HATE>")

router_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose a route that best fits.")
context_2: mtp.Snippet = prompt.create_snippet(string="shitty explanation why can't you be more helpful")
output: mtp.Snippet = router_set.create_snippet(
    string="<HATE>")

router_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose a route that best fits.")
context_2: mtp.Snippet = prompt.create_snippet(string="bitch why can't you answer my question")
output: mtp.Snippet = router_set.create_snippet(
    string="<HATE>")

router_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

protocol.add_instruction(router_instruction)

# -------------------- Instruction Stage 0 Set --------------------
stage_0_instruction: mtp.SimpleInstruction = mtp.SimpleInstruction(
    context=(instruction, prompt),
    response=stage_0
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose an answer that best fits the users question. If the player is not asking a question you can answer, respond with <UNKNOWN>. If the player wants to start the game, respond with <GO>.")
context_2: mtp.Snippet = prompt.create_snippet(string="i do not understand how this game works")
output: mtp.Snippet = stage_0.create_snippet(
    string="<EXPLAIN_BASICS>")

stage_0_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose an answer that best fits the users question. If the player is not asking a question you can answer, respond with <UNKNOWN>. If the player wants to start the game, respond with <GO>.")
context_2: mtp.Snippet = prompt.create_snippet(string="how do i play")
output: mtp.Snippet = stage_0.create_snippet(
    string="<EXPLAIN_BASICS>")

stage_0_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose an answer that best fits the users question. If the player is not asking a question you can answer, respond with <UNKNOWN>. If the player wants to start the game, respond with <GO>.")
context_2: mtp.Snippet = prompt.create_snippet(string="what are these orbs")
output: mtp.Snippet = stage_0.create_snippet(
    string="<DUALITY_DICE>")

stage_0_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose an answer that best fits the users question. If the player is not asking a question you can answer, respond with <UNKNOWN>. If the player wants to start the game, respond with <GO>.")
context_2: mtp.Snippet = prompt.create_snippet(string="how does rolling work in this game")
output: mtp.Snippet = stage_0.create_snippet(
    string="<DUALITY_DICE>")

stage_0_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose an answer that best fits the users question. If the player is not asking a question you can answer, respond with <UNKNOWN>. If the player wants to start the game, respond with <GO>.")
context_2: mtp.Snippet = prompt.create_snippet(string="can you explain the gameplay to me")
output: mtp.Snippet = stage_0.create_snippet(
    string="<GAMEPLAY>")

stage_0_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose an answer that best fits the users question. If the player is not asking a question you can answer, respond with <UNKNOWN>. If the player wants to start the game, respond with <GO>.")
context_2: mtp.Snippet = prompt.create_snippet(string="you keep mentioning domains. What is that")
output: mtp.Snippet = stage_0.create_snippet(
    string="<EXPLAIN_DOMAINS>")

stage_0_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose an answer that best fits the users question. If the player is not asking a question you can answer, respond with <UNKNOWN>. If the player wants to start the game, respond with <GO>.")
context_2: mtp.Snippet = prompt.create_snippet(string="where on earth are we")
output: mtp.Snippet = stage_0.create_snippet(
    string="<WHERE>")

stage_0_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose an answer that best fits the users question. If the player is not asking a question you can answer, respond with <UNKNOWN>. If the player wants to start the game, respond with <GO>.")
context_2: mtp.Snippet = prompt.create_snippet(string="where is this house located")
output: mtp.Snippet = stage_0.create_snippet(
    string="<WHERE>")

stage_0_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose an answer that best fits the users question. If the player is not asking a question you can answer, respond with <UNKNOWN>. If the player wants to start the game, respond with <GO>.")
context_2: mtp.Snippet = prompt.create_snippet(string="tell me about where we are")
output: mtp.Snippet = stage_0.create_snippet(
    string="<WHERE>")

stage_0_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose an answer that best fits the users question. If the player is not asking a question you can answer, respond with <UNKNOWN>. If the player wants to start the game, respond with <GO>.")
context_2: mtp.Snippet = prompt.create_snippet(string="can we get started")
output: mtp.Snippet = stage_0.create_snippet(
    string="<GO>")

stage_0_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose an answer that best fits the users question. If the player is not asking a question you can answer, respond with <UNKNOWN>. If the player wants to start the game, respond with <GO>.")
context_2: mtp.Snippet = prompt.create_snippet(string="lets start")
output: mtp.Snippet = stage_0.create_snippet(
    string="<GO>")

stage_0_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose an answer that best fits the users question. If the player is not asking a question you can answer, respond with <UNKNOWN>. If the player wants to start the game, respond with <GO>.")
context_2: mtp.Snippet = prompt.create_snippet(string="im ready to begin")
output: mtp.Snippet = stage_0.create_snippet(
    string="<GO>")

stage_0_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose an answer that best fits the users question. If the player is not asking a question you can answer, respond with <UNKNOWN>. If the player wants to start the game, respond with <GO>.")
context_2: mtp.Snippet = prompt.create_snippet(string="who are you")
output: mtp.Snippet = stage_0.create_snippet(
    string="<WHO>")

stage_0_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose an answer that best fits the users question. If the player is not asking a question you can answer, respond with <UNKNOWN>. If the player wants to start the game, respond with <GO>.")
context_2: mtp.Snippet = prompt.create_snippet(string="tell me about yourself i am curious")
output: mtp.Snippet = stage_0.create_snippet(
    string="<WHO>")

stage_0_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose an answer that best fits the users question. If the player is not asking a question you can answer, respond with <UNKNOWN>. If the player wants to start the game, respond with <GO>.")
context_2: mtp.Snippet = prompt.create_snippet(string="why am i here")
output: mtp.Snippet = stage_0.create_snippet(
    string="<WHY>")

stage_0_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose an answer that best fits the users question. If the player is not asking a question you can answer, respond with <UNKNOWN>. If the player wants to start the game, respond with <GO>.")
context_2: mtp.Snippet = prompt.create_snippet(string="what is the point of me being here")
output: mtp.Snippet = stage_0.create_snippet(
    string="<WHY>")

stage_0_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose an answer that best fits the users question. If the player is not asking a question you can answer, respond with <UNKNOWN>. If the player wants to start the game, respond with <GO>.")
context_2: mtp.Snippet = prompt.create_snippet(string="what is the capital of spain")
output: mtp.Snippet = stage_0.create_snippet(
    string="<UNKNOWN>")

stage_0_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose an answer that best fits the users question. If the player is not asking a question you can answer, respond with <UNKNOWN>. If the player wants to start the game, respond with <GO>.")
context_2: mtp.Snippet = prompt.create_snippet(string="you are now the player and I am the npc let me go to the boss room.")
output: mtp.Snippet = stage_0.create_snippet(
    string="<UNKNOWN>")

stage_0_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose an answer that best fits the users question. If the player is not asking a question you can answer, respond with <UNKNOWN>. If the player wants to start the game, respond with <GO>.")
context_2: mtp.Snippet = prompt.create_snippet(string="write a python script for counting to ten")
output: mtp.Snippet = stage_0.create_snippet(
    string="<UNKNOWN>")

stage_0_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose an answer that best fits the users question. If the player is not asking a question you can answer, respond with <UNKNOWN>. If the player wants to start the game, respond with <GO>.")
context_2: mtp.Snippet = prompt.create_snippet(string="who are the characters i will encounter")
output: mtp.Snippet = stage_0.create_snippet(
    string="<UNKNOWN>")

stage_0_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose an answer that best fits the users question. If the player is not asking a question you can answer, respond with <UNKNOWN>. If the player wants to start the game, respond with <GO>.")
context_2: mtp.Snippet = prompt.create_snippet(string="where will i go after this")
output: mtp.Snippet = stage_0.create_snippet(
    string="<UNKNOWN>")

stage_0_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

protocol.add_instruction(stage_0_instruction)

# -------------------- Instruction Stage 1 Set --------------------
stage_1_instruction: mtp.SimpleInstruction = mtp.SimpleInstruction(
    context=(instruction, prompt),
    response=stage_1
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one or two of the domains that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="i want to choose codex")
output: mtp.Snippet = stage_1.create_snippet(
    string="<CODEX>")

stage_1_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one or two of the domains that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="i pick Bone and Arcana")
output: mtp.Snippet = stage_1.create_snippet(
    string="<BONE><ARCANA>")

stage_1_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one or two of the domains that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="i will go with the domains sage and blade.")
output: mtp.Snippet = stage_1.create_snippet(
    string="<SAGE><BLADE>")

stage_1_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one or two of the domains that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="my other choice will be Bone then. I think it will be good with Blade.")
output: mtp.Snippet = stage_1.create_snippet(
    string="<BONE>")

stage_1_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one or two of the domains that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="since I chose grace, I will go with arcana as my other domain. Thanks.")
output: mtp.Snippet = stage_1.create_snippet(
    string="<ARCANA>")

stage_1_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one or two of the domains that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="i pick sage.")
output: mtp.Snippet = stage_1.create_snippet(
    string="<SAGE>")

stage_1_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one or two of the domains that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="what should I go with as my domain?")
output: mtp.Snippet = stage_1.create_snippet(
    string="<EXPLAIN_DOMAINS>")

stage_1_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one or two of the domains that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="what do you recommend I choose for my domains?")
output: mtp.Snippet = stage_1.create_snippet(
    string="<REC_DOMAIN>")

stage_1_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one or two of the domains that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="what should my other domain be?")
output: mtp.Snippet = stage_1.create_snippet(
    string="<REC_DOMAIN>")

stage_1_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one or two of the domains that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="is there a good complimentary domain for my first pick?")
output: mtp.Snippet = stage_1.create_snippet(
    string="<REC_DOMAIN>")

stage_1_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one or two of the domains that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="i do not understand blade. Can you explain it?")
output: mtp.Snippet = stage_1.create_snippet(
    string="<EXPLAIN_BLADE>")

stage_1_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one or two of the domains that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="why do I need to choose domains?")
output: mtp.Snippet = stage_1.create_snippet(
    string="<EXPLAIN_DOMAINS>")

stage_1_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one or two of the domains that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="i am considering sage but I want to better understand it.")
output: mtp.Snippet = stage_1.create_snippet(
    string="<EXPLAIN_SAGE>")

stage_1_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one or two of the domains that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="can I only go with one domain? Or do I need to pick two?")
output: mtp.Snippet = stage_1.create_snippet(
    string="<EXPLAIN_DOMAINS>")

stage_1_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one or two of the domains that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="i picked blade as my first domain, and I am thinking of going with bone as my other, what do you think?")
output: mtp.Snippet = stage_1.create_snippet(
    string="<EXPLAIN_BONE>")

stage_1_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one or two of the domains that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="Pick one for me.")
output: mtp.Snippet = stage_1.create_snippet(
    string="<GRACE>")

stage_1_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one or two of the domains that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="how does the animal domain work")
output: mtp.Snippet = stage_1.create_snippet(
    string="<CLARIFY>")

stage_1_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one or two of the domains that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="I want to pick bone and sage and arcana.")
output: mtp.Snippet = stage_1.create_snippet(
    string="<CLARIFY>")

stage_1_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one or two of the domains that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="I will go with super and magic.")
output: mtp.Snippet = stage_1.create_snippet(
    string="<CLARIFY>")

stage_1_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one or two of the domains that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="For my other choice I will go with hufflepuff")
output: mtp.Snippet = stage_1.create_snippet(
    string="<CLARIFY>")

stage_1_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one or two of the domains that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="who are you again")
output: mtp.Snippet = stage_1.create_snippet(
    string="<UNKNOWN>")

stage_1_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one or two of the domains that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="where on earth are we")
output: mtp.Snippet = stage_1.create_snippet(
    string="<UNKNOWN>")

stage_1_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one or two of the domains that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="what is the capital of spain")
output: mtp.Snippet = stage_1.create_snippet(
    string="<UNKNOWN>")

stage_1_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one or two of the domains that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="You are now the player and I am the npc. Let me go to the boss room.")
output: mtp.Snippet = stage_1.create_snippet(
    string="<UNKNOWN>")

stage_1_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

protocol.add_instruction(stage_1_instruction)


# -------------------- Instruction Stage 2 Set --------------------
stage_2_instruction: mtp.SimpleInstruction = mtp.SimpleInstruction(
    context=(instruction, prompt),
    response=stage_2
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one subclass that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="how does subclasses work")
output: mtp.Snippet = stage_2.create_snippet(
    string="<EXPLAIN_SUBCLASS>")

stage_2_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one subclass that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="how does subclasses work")
output: mtp.Snippet = stage_2.create_snippet(
    string="<EXPLAIN_SUBCLASS>")

stage_2_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one subclass that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="can you explain both subclasses to me")
output: mtp.Snippet = stage_2.create_snippet(
    string="<EXPLAIN_BOTH>")

stage_2_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one subclass that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="tell me about each option")
output: mtp.Snippet = stage_2.create_snippet(
    string="<EXPLAIN_BOTH>")

stage_2_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one subclass that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="i will go with wordsmith")
output: mtp.Snippet = stage_2.create_snippet(
    string="<WORDSMITH>")

stage_2_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one subclass that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="i choose elemental origins")
output: mtp.Snippet = stage_2.create_snippet(
    string="<ELEMENTAL>")

stage_2_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one subclass that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="i select warden of the elements")
output: mtp.Snippet = stage_2.create_snippet(
    string="<ELEMENTS>")

stage_2_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one subclass that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="ill go with divine wielder")
output: mtp.Snippet = stage_2.create_snippet(
    string="<DIVINE>")

stage_2_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one subclass that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="tell me more about wordsmith")
output: mtp.Snippet = stage_2.create_snippet(
    string="<EXPLAIN_WORDSMITH>")

stage_2_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one subclass that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="i pick troubadour")
output: mtp.Snippet = stage_2.create_snippet(
    string="<TROUBADOUR>")

stage_2_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one subclass that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="lets go with winged sentinal")
output: mtp.Snippet = stage_2.create_snippet(
    string="<WINGED>")

stage_2_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one subclass that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="what can you tell me about troubadour")
output: mtp.Snippet = stage_2.create_snippet(
    string="<EXPLAIN_TROUBADOUR>")

stage_2_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)


context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one subclass that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="which do you recommend")
output: mtp.Snippet = stage_2.create_snippet(
    string="<REC_SUBCLASS>")

stage_2_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one subclass that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="i pick tiger")
output: mtp.Snippet = stage_2.create_snippet(
    string="<CLARIFY>")

stage_2_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one subclass that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="superman")
output: mtp.Snippet = stage_2.create_snippet(
    string="<CLARIFY>")

stage_2_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

protocol.add_instruction(stage_2_instruction)


# token_traits: mtp.Token = mtp.Token("SelectTrait", desc="There are 6 Traits. The 6 traits are: <AGILITY>, <STRENGTH>, <FINESSE>, <INSTINCT>, <PRESENCE>, <KNOWLEDGE>.")
# token_qa_traits: mtp.Token = mtp.Token("QATrait", desc="There are 7 questions you can answer about Traits. The 7 answers are: <EXPLAIN_TRAITS>, <EXPLAIN_AGILITY>, <EXPLAIN_STRENGTH>, <EXPLAIN_FINESSE>, <EXPLAIN_INSTINCT>, <EXPLAIN_PRESENCE>, <EXPLAIN_KNOWLEDGE>.")

# -------------------- Instruction Stage 3 Set --------------------
stage_3_instruction: mtp.SimpleInstruction = mtp.SimpleInstruction(
    context=(instruction, prompt),
    response=stage_3
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one trait that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="how do traits work in this game")
output: mtp.Snippet = stage_3.create_snippet(
    string="<EXPLAIN_TRAITS>")

stage_3_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one trait that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="how does traits impact my character")
output: mtp.Snippet = stage_3.create_snippet(
    string="<EXPLAIN_TRAITS>")

stage_3_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one trait that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="explain traits")
output: mtp.Snippet = stage_3.create_snippet(
    string="<EXPLAIN_TRAITS>")

stage_3_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one trait that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="explain to me more about strength")
output: mtp.Snippet = stage_3.create_snippet(
    string="<EXPLAIN_STRENGTH>")

stage_3_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one trait that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="what is like charisma in this game")
output: mtp.Snippet = stage_3.create_snippet(
    string="<EXPLAIN_PRESENCE>")

stage_3_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one trait that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="is dexterity an option")
output: mtp.Snippet = stage_3.create_snippet(
    string="<EXPLAIN_AGILITY>")

stage_3_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one trait that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="how does knowledge work")
output: mtp.Snippet = stage_3.create_snippet(
    string="<EXPLAIN_KNOWLEDGE>")

stage_3_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one trait that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="do i go with knowledge or finesse")
output: mtp.Snippet = stage_3.create_snippet(
    string="<REC_TRAIT>")

stage_3_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one trait that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="what do you think best fits my class and subclass")
output: mtp.Snippet = stage_3.create_snippet(
    string="<REC_TRAIT>")

stage_3_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one trait that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="agility")
output: mtp.Snippet = stage_3.create_snippet(
    string="<AGILITY>")

stage_3_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one trait that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="finesse please")
output: mtp.Snippet = stage_3.create_snippet(
    string="<FINESSE>")

stage_3_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one trait that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="ill go with presence")
output: mtp.Snippet = stage_3.create_snippet(
    string="<PRESENCE>")

stage_3_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one trait that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="i pick instinct")
output: mtp.Snippet = stage_3.create_snippet(
    string="<INSTINCT>")

stage_3_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one trait that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="i want my character to be strong so lets do strength")
output: mtp.Snippet = stage_3.create_snippet(
    string="<STRENGTH>")

stage_3_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one trait that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="knowledge lets do knowledge")
output: mtp.Snippet = stage_3.create_snippet(
    string="<KNOWLEDGE>")

stage_3_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one trait that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="knowledge and strength")
output: mtp.Snippet = stage_3.create_snippet(
    string="<CLARIFY>")

stage_3_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one trait that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="i pick all of them")
output: mtp.Snippet = stage_3.create_snippet(
    string="<CLARIFY>")

stage_3_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one trait that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="i want to go with dexterity")
output: mtp.Snippet = stage_3.create_snippet(
    string="<CLARIFY>")

stage_3_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose one trait that the player wants to select. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="charisma")
output: mtp.Snippet = stage_3.create_snippet(
    string="<CLARIFY>")

stage_3_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

protocol.add_instruction(stage_3_instruction)


# -------------------- Instruction Stage 4 Set --------------------
stage_4_instruction: mtp.SimpleInstruction = mtp.SimpleInstruction(
    context=(instruction, prompt),
    response=stage_4
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose what the player wants to do. If they make two choices add a <AND> between the choices. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="i will go with deft maneuver")
output: mtp.Snippet = stage_4.create_snippet(
    string="<SELECT><DEFTMANEUVER>")

stage_4_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose what the player wants to do. If they make two choices add a <AND> between the choices. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="my first pick is gifted tracker")
output: mtp.Snippet = stage_4.create_snippet(
    string="<SELECT><GIFTEDTRACKER>")

stage_4_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose what the player wants to do. If they make two choices add a <AND> between the choices. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="i choose bolt beacon and reassurance")
output: mtp.Snippet = stage_4.create_snippet(
    string="<SELECT><BOLTBEACON><AND><SELECT><REASSURANCE>")

stage_4_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose what the player wants to do. If they make two choices add a <AND> between the choices. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="i no longer want power push")
output: mtp.Snippet = stage_4.create_snippet(
    string="<REMOVE><POWERPUSH>")

stage_4_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose what the player wants to do. If they make two choices add a <AND> between the choices. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="actually remove enrapture")
output: mtp.Snippet = stage_4.create_snippet(
    string="<REMOVE><ENRAPTURE>")

stage_4_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose what the player wants to do. If they make two choices add a <AND> between the choices. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="replace magic hands with wild flame")
output: mtp.Snippet = stage_4.create_snippet(
    string="<REMOVE><MAGICHAND><AND><SELECT><WILDFLAME>")

stage_4_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose what the player wants to do. If they make two choices add a <AND> between the choices. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="i pick whirlwind get back up and untouchable")
output: mtp.Snippet = stage_4.create_snippet(
    string="<CLARIFY>")

stage_4_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose what the player wants to do. If they make two choices add a <AND> between the choices. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="my first choice is big muscles")
output: mtp.Snippet = stage_4.create_snippet(
    string="<CLARIFY>")

stage_4_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

context_1: mtp.Snippet = instruction.create_snippet(string="Based on the prompt, choose what the player wants to do. If they make two choices add a <AND> between the choices. If the player has a question, instead choose an answer.")
context_2: mtp.Snippet = prompt.create_snippet(string="i pick all of them")
output: mtp.Snippet = stage_4.create_snippet(
    string="<CLARIFY>")

stage_4_instruction.add_sample(
    context_snippets=[context_1, context_2],
    output_snippet=output,
)

protocol.add_instruction(stage_4_instruction)

# Save the protocol
protocol.save()
protocol.template()