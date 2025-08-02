# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

image kiddo = "kiddo.png"
image kiddo laugh = "kiddo laugh.png"
image kiddo happy = "kiddo happy.png"
image kiddo sad = "kiddo sad.png"

image facteur = "facteur.png"
image facteur happy = "facteur happy.png"
image facteur sad = "facteur sad.png"

image roi = "king.png"
image roi happy = "king happy.png"
image roi sad = "king sad.png"
image roi angry = "king angry.png"

image princess = "princess.png"
image princess happy = "princess happy.png"
image princess sad = "princess sad.png"
image princess laugh = "princess laugh.png"

#exemple de chemins d'accès si les personnages sont dans un sous-dossier dans IMAGES
image queen = "queen/queen.png"
image queen happy = "queen/queen happy.png"
image queen laugh = "queen/queen laugh.png"
image queen sad = "queen/queen sad.png"

# Déclarez les personnages utilisés dans le jeu.

define k = Character("Kiddo", color="#000000ff", image="kiddo")
define m = Character("Max", color="#ff0000ff")
define f = Character("Facteur", color="#3d3d3dff", image="facteur")
define p = Character("[princess_name]", color="#662e56ff", image="princess")
define r = Character("Le Roi", image="roi")
define q = Character("La Reine", image="queen")
# ---- le coin des variables ----

# On initialise le compteur de pièces d'or à 0
default goldCoins = 0
default princess_name = "Sam"
default adventurers_guild = False
define potion_price = 40

# Le jeu commence ici
label start:
    scene bg forest
    "C'est l'histoire de Max, le barde asthmatique qui vit dans la forêt"
    "Max aimerait bien s'acheter une potion magique pour guérir son asthme"
    "Mais les potions magiques, ça coûte cher. Et max doit trouver assez d'or pour s'acheter sa potion"
    "Un jour, Max rencontre un gamin dans la forêt..."
    show kiddo at center with easeinright
    k "Salut! T'es le musicien de la forêt non?"
    m "Je suis un Barde. Musicien. Poète. Comédien..."
    m "Qu'est-ce que je peux faire pour toi?"
    k "Tu peux me chanter une chanson?"
    k "Si tu me chantes une chanson trop cool, je te donnerai plein de pièces d'or!"
    menu:
        "Quelle chanson choisir?"
        "Une composition personnelle avant-gardiste":
            "Max chante sa dernière oeuvre, un morceau révolutionnaire"
            m "Owwww AH AH AH AH!"
            k laugh "Oah! C'est trop fort comme musique!"
            k "Merci m'sieur le barde!"
            $ goldCoins = goldCoins + 20 # Même chose que $ goldCoins += 20
            m "La créativité et l'audace, c'est ça, l'art!"
            "Max recoit 20 pièces d'or"
        "Un classique, sans prise de risque":
            "Max entonne une ballade populaire bien connue"
            m "Pom pom pom pom pom pompom..."
            k happy "J'la connais celle-là!"
            k "C'est chouette de l'entendre chantée par un vrai pro!"
            k "Merci m'sieur!"
            $ goldCoins += 10
            "Max reçoit 10 pièces d'or"
            m "Un client satisfait, ça réchauffe le coeur!"
        "Paniquer: C'est trop dur de choisir!":
            "Pris de panique, Max fredonne Mahna Mahna"
            m "Mahna Mahna tu tu tu lulu"
            k sad "Euh... c'était pas vraiment ce que j'avais en tête"
            k "Bon, je dois quand même te payer..."
            $ goldCoins += 5
            m "Je ferai mieux la prochaine fois..."
            "Max reçoit 5 pièces d'or"
    hide kiddo with easeoutleft
    "Le temps passe, et un jour, un messager du roi trouve Max dans les bois..."
    show facteur at left with easeinleft
    f "J'en peux plus de ces bois"
    show facteur at right with ease
    f "Tous les arbres se ressemblent"
    show facteur at center with ease
    f "Ah! Mais vous êtes là! C'est bien vous, le Barde? Je vous cherchais!"
    m "Vous me cherchiez?"
    f "Le roi a besoin de vos services de poète. Suivez-moi s'il vous plaît."
    hide facteur with easeoutright
    "Max se met donc en route vers le château..."
    jump name_the_princess

label name_the_princess:
    scene bg castle
    show facteur at left with easeinleft
    f "Sire! Sire! J'ai le Barde avec moi!"
    show roi at right with easeinright
    r happy "Mon bon messager, tu as accompli ta mission, comme je te l'avais demandé."
    r "Tu peux disposer pour le moment."
    hide facteur with easeoutleft

    # show prefix - emotion: remet la sprite par défaut du personnage
    show roi -happy at center with ease

    r "C'est donc vous, le barde de la forêt"
    r "J'ai besoin de vos services"
    r "La nouvelle princesse est née, et je n'arrive pas à lui trouver de nom"
    r "Pour le moment, ma seule idée est \"Sam\", mais peut-être qu'un poète de votre talent pourrait avoir une meilleure idée?"
    r "Si vous accomplissez cette tâche avec brio, vous serez récompensé généreusement."
    "Trouver un nom pour la princesse!"
    python:
        princess_name = renpy.input("Comment appeler la princesse?", default="Sam")
        princess_name = princess_name.strip() or "Sam"
    m "Je vais l'appeler [princess_name]"
    if princess_name == "Max":
        r angry "Absolument pas!"
        r "L'art n'excuse pas tout!"
        r "Quelle impertinence!"
        r "Je ne vous laisserai pas vivre une seconde de plus!"
        r "Qu'on lui coupe la tête!"
        jump bad_ending_1

    elif princess_name != "Sam":
        r happy"Magnifique! Merveilleux! Inspiré!"
        r "Merci, cher barde!"
        r "Je savais qu'il me fallait faire appel à vos services!"
        r "Comme promis, voici votre récompense!"
        show roi -happy
        $ goldCoins += 20
        "Max reçoit 20 pièces d'or!"
    else:
        r "J'imagine que ma première idée n'était pas si mauvaise après tout..."
        r sad "Vous comprendrez bien que je ne peux pas vous rémunérer pour ceci?"
        r "J'espérais pouvoir être témoin de la créativité d'un artiste"
        show roi -sad
        r "Peu importe; Merci quand même"
    r "Mon messager vous raccompagnera chez vous"
    show roi at right with ease
    r "Facteur!"
    show facteur at center with easeinleft
    f "Oui, Sire?"
    r "Je vous laisse vous occuper de notre invité"
    f "Très bien, Sire"
    hide roi with easeoutright
    f "Je vais vous escorter à la forêt"

    f "Mais d'abord, est-ce que vous souhaitez rejoindre la GUILDE DES AVENTURIERS?"
    f "Pour la modique somme de 5 pièces d'or, vous ajouterez votre nom à la liste des aventuriers auxquels nous pourrions faire appel, en cas de besoin"
    f "Cela pourrait vous offrir des opportunités lucratives à l'avenir!"
    menu:
        "Rejoindre la GUILDE DES AVENTURIERS? (5 pièces d'or)"
        "Oui":
            m "Inscrivez-moi sur votre liste!"
            $ goldCoins -= 5
            $ adventurers_guild = True
            f happy "Un excellent choix!"
        "Non merci":
            m "Non merci, je suis un artiste, pas un aventurier"
            $ adventurers_guild = False
            f sad "Dommage..."
    f "Laissez-moi vous raccompagner chez vous..."
    hide facteur with easeoutleft
    jump forest_waiting

label forest_waiting:
    scene bg forest
    "De retour dans sa forêt, Max compose des ballades pour passer le temps"
    "Le temps passe, au rythme de ses créations musicales, et des chants des oiseaux"
    if adventurers_guild:
        jump adventure_time
    else:
        jump tavern_gambling

label adventure_time:
    "Alors que l'ennui se fait sentir, un pigeon voyageur apporte une missive de la plus haute importance à Max:"
    "{i} A tous les aventuriers de la GUILDE DES AVENTURIERS:{/i}"
    "{i} Reine disparue dans les montagnes{/i}"
    "{i} Récompense si ramenée au château saine et sauve{/i}"
    "{i} Bonne chance!{/i}"
    m "Une aventure! Une récompense! C'est pour moi ça!"
    "Max se met immédiatement en route pour les montagnes"

    scene bg mountain
    "Arrivé dans la montagne, Max voit deux choix s'offrir à lui: Le Lac Mystérieux ou Les Grottes Sombres"
    menu:
        "Quel chemin emprunte Max?"
        "Le Lac":
            "Max décide de sonder le lac: Peut-être que la Reine a décidé de se baigner?"
            "Malheureusement, après quelques mètres à la nage, l'asthme de Max le met en difficulté"
            "Et Max se noie."
            jump drowned_ending
        "Les Grottes Sombres":
            "Max décide de braver l'obscurité des grottes"
            jump grottes_sombres
    
    label grottes_sombres:
        scene bg tunnels
        "Ces grottes portent bien leur nom. Elles sont vraiment sombres"
        menu:
            "Max arrive à une intersection, et 3 choix s'offrent à lui"
            "A gauche":
                "Max emprunte le tunnel de gauche"
                "Après quelques mètres, Max trouve une bourse pleine de pièces d'or!"
                $ goldCoins += 50
                "Max est trop essouflé pour continuer son exploration"
                "Et décide de rentrer dans la forêt, 50 pièces plus riche qu'auparavant"
                "Mais sans la Reine"
                jump back_to_the_forest

            "A droite":
                "Max emprunte le tunnel de droite"
                "Après quelques mètres, Max trouve une pierre précieuse"
                "Elle vaut au moins 20 pièces d'or!"
                $ goldCoins += 20
                "Max est trop essouflé pour continuer son exploration"
                "Peut-être que quelqu'un d'autre trouvera la Reine"
                "Sa pierre précieuse dans sa poche, il retourne dans la forêt"
                jump back_to_the_forest

            "Au centre":
                "Max emprunte le tunnel du centre"
                "Il fait sombre"
                "Il fait froid"
                "Après ce qui lui semble être une éternité, Max arrive dans une chambre de la grotte"
                "Et là, au sol, il trouve la Reine, endormie"
                "Max a trouvé la Reine!"
                jump queen_found
    
    label queen_found:
        m "Votre Altesse?"
        m "Réveillez-vous!"
        show queen at center with easeinbottom
        q sad "Je me suis perdue dans la montagne"
        q happy "Mais vous m'avez sauvée!"
        q laugh "Comment vous remercier?!"
        q happy "Escortez-moi au château, vous serez récompensé!"
        hide queen with easeoutright
        "Max escorte la Reine hors des tunnels"
        jump queen_found_ending

    label queen_found_ending:
        scene bg castle
        show queen at center with easeinleft
        q happy"Merci de m'avoir sauvée, Barde"
        show roi at right with easeinright
        r "Ma Mie! Vous êtes de retour!"
        r happy"Barde! Vous l'avez sauvée!"
        r "Merci!!"
        r "Pour vous récompenser, je vous nomme BARDE OFFICIEL de la cour"
        r happy "Vous pourrez venir vivre au château"
        r "De plus, il me semble que vous êtes fort essouflé"
        r "Mon Druide vous concoctera une potion pour guérir votre asthme"
        r "C'est la moindre des choses pour vous remercier"
        hide queen
        hide roi
        with easeoutright
        "Ainsi, Max gagna non seulement une potion miraculeuse"
        "Mais une chambre magnifique au château"
        "Max n'était plus le barde asthmatique vivant dans la forêt"
        "Max était le barde du roi"
        window hide
        centered "{size=128}FIN{/size}"
        return

label tavern_gambling:
    "Un jour, l'ennui se fait sentir"
    "Max décide donc de se rendre en ville"
    "Pour passer du temps à la taverne"
    scene bg town
    "La taverne est pleine de monde!"
    "Soudain, quelqu'un l'approche..."
    show princess at center with easeinright
    p "Salut! Alors, c'est toi le fameux barde?"
    if princess_name != "Sam":
        p happy"Il paraît que tu as aidé à me nommer!"
        show princess -happy
    else:
        p sad"Il paraît que tu as essayé de me trouver un nom, mais que tu n'étais pas inspiré"
        show princess -sad
    p "Qu'est-ce que tu fais là?"
    m "Euh... Je passe le temps..."
    m "Mais... Comment as-tu pu grandir autant, si vite?"
    p happy"J'ai bu une potion magique qui fait grandir!"
    p "Les potions, ça marche vraiment!"
    m "J'aimerais bien une potion pour guérir mon asthme"
    m "Mais j'ai pas assez de pièces d'or pour le moment..."
    p sad"Mince, c'est dommage ça..."
    
    # Ici, on regarde si Max a assez de pièces d'or pour que la princesse lui propose de jouer à pile ou face
    if goldCoins >= 10:
        jump can_gamble
    else: 
        jump cannot_gamble

label can_gamble:
    p happy"Dis, si tu veux, on peut jouer à un jeu!"
    p "Mise 10 pièces d'or, et devine si ma pièce dira pile ou face"
    p "Quitte ou double!"
    show princess at right with ease
    p "Ca te tente?"
    menu:
        "Tu veux jouer à pile ou face?"
        "Oui":
            jump heads_or_tails
        "Non":
            m "Non, merci."
            p sad"Pas de soucis! Je te laisse profiter de ta soirée à la taverne alors!"
            hide princess with easeoutright
            jump tavern_evening

label heads_or_tails:
    p "Alors tu vas essayer de deviner ma pièce, et si tu trouves le bon résultat, je te donnerai 20 pièces d'or"
    p "Sinon, tu perdras 10 pièces d'or"

    # la "boucle" du jeu pile ou face
    label game_loop:
        ### VARIABLES POUR LE PETIT JEU
        # La variable du choix de Max
        $ max_guess = None
        # Le résultat de la pièce de la princesse
        $ princess_coin = None

        p happy"Alors, à ton avis, pile ou face?"
        menu:
            "Pile":
                m "Pile!"
                $ max_guess = "pile"
            "Face":
                m "Face!"
                $ max_guess = "face"

        # Choix aléatoire entre "Pile" et "Face" pour la pièce de la princesse
        $ princess_coin = renpy.random.choice(["pile","face"])
        "La princesse lance la pièce..."
        "..."
        # Annonce du résultat de la pièce de la princesse
        "C'est [princess_coin]!"

        # On regarde si max a deviné le bon résulat
        if max_guess == princess_coin:
            p laugh"Tu as bien deviné! Bravo!"
            "Max gagne 20 pièces d'or"
            $ goldCoins += 20
        else: 
            p sad"Mince... Pas de chance!"
            "Max perd 10 pièces d'or"
            $ goldCoins -= 10
        
        # le bloc qui permet de rejouer si on a assez de pièces d'or 
        if goldCoins >= 10:
            menu:
                "Jouer à nouveau?"
                "Oui!":
                    p happy"D'accord, on rejoue!"
                    jump game_loop
                "Non, merci":
                    p sad"D'accord! Alors je te laisse tranquille"
                    p sad"Au revoir, Max!"
                    hide princess with easeoutright
                    jump tavern_evening

        # le bloc où on ne peut pas rejouer car on n'a pas assez de pièces d'or
        else:
            "Max ne peut plus jouer, il n'a pas assez de pièces d'or!"
            p sad"Mince, tu ne peux plus jouer"
            p sad"Je vais te laisser tranquille..."
            p sad"Au revoir, Max!"
            hide princess with easeoutright
            jump tavern_evening

# Ici, max ne joue pas du tout à pile ou face, car il n'a jamais eu assez de pièce d'or pour jouer
label cannot_gamble:
    p sad"Je t'aurais bien proposé un jeu mais je crois que tu n'as pas assez de pièces d'or"
    p "Je te laisse profiter de ta soirée tranquillement!"
    p happy"Au revoir, Max! Et bonne chance!"
    hide princess with easeoutright
    jump tavern_evening

# La suite de la scène de la taverne
label tavern_evening:
    "Max s'installe pour profiter de la musique"
    "La soirée passe sans autre évènement particulier"
    "Même pas une bagarre de bar"
    "Le temps passe, et il se fait tard"
    "Max décide de rentrer dans sa forêt"
    jump back_to_the_forest

# Max retourne dans la forêt pour compter ses pièces d'or
label back_to_the_forest:
    scene bg forest
    "De retour dans la forêt, Max compte ses pièces d'or"
    "Il en a [goldCoins]"
    if goldCoins >= potion_price:
        jump good_ending
    if goldCoins == 0:
        jump broke_ending
    else:
        jump bad_ending_2

# La fin où Max se fait décapiter pour son arrogance
label bad_ending_1:
    "Ainsi, Max fut puni pour son arrogance"
    "C'est dommage de terminer sa vie ainsi"
    centered "{size=128}FIN{/size}"
    return

# La fin où Max se noie dans le lac
label drowned_ending:
    "Personne ne revit Max"
    scene bg forest
    "Sa disparition ne fut remarquée que par les oiseaux"
    "Qui n'avaient plus de luth pour accompagner leurs chants"
    "Peut-être que les artistes ne devraient pas partir à l'aventure"
    "Mais se contenter de les rêver"
    centered "{size= 128} FIN {/size}"
    return

# La fin où Max arrive à s'acheter la potion magique
label good_ending:
    "Max peut s'acheter la potion!"
    "Max est guéri!"
    "Félicitations!!"
    centered "{size=128} FIN {/size}"
    return

# La fin où Max termine avec 0 pièces d'or
label broke_ending:
    "Max n'a pas un sou..."
    "C'est vraiment difficile, la vie d'artiste."
    "Peut-être devrait-il considérer une autre carrière?"
    centered "{size=128} FIN {/size}"
    return

# La fin où Max n'arrive pas à s'acheter la potion magique
label bad_ending_2:
    "Malheureusement, Max n'a pas réussi à s'acheter sa potion magique"
    "Il n'a tout simplement pas assez de pièces d'or"
    "Peut-être qu'avec le temps, il arrivera à son objectif"
    "Mais cela ne sera pas raconté dans cette histoire..."
    centered "{size=128} FIN... pour le moment {/size}"
    return

    return
