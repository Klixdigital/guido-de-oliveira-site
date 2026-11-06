"""Contenu du site, tiré des fichiers de l'artiste (2026-11-05) :
- « Oeuvres originales disponibles/ » : les œuvres, rangées par série ;
- « more info/ » : notes sur la maquette (NotesSiteWeb_2.odt), FAQ.pdf, book 2025 et CV (années, techniques, formats).
Une valeur à None s'affiche « à fournir » sur le site. Descriptions (CV) et histoires (book) : 8 œuvres, voir
DESCRIPTIONS et HISTOIRES. Les prix et les textes manquants viendront d'une fiche séparée de l'artiste : ne rien
inventer en attendant.
"""

# ── Liens (None = message « lien à fournir » au clic) ──
LIENS = {
    'etsy': None,  # « le lien suivra très prochainement » (notes de l'artiste)
    'redbubble': 'https://www.redbubble.com/people/GuiarteSMS/shop',
    'instagram': 'https://www.instagram.com/guiarteofficial/',
    'tiktok': 'https://www.tiktok.com/@guiarteofficial',
    'pinterest': 'https://www.pinterest.com/atguiarteofficial/',  # @atguiarteofficial selon les notes, @guiarteofficial selon le book : à confirmer
    'youtube': 'https://www.youtube.com/@guiarteofficial',
    'email': 'info@guidodeoliveira.com',
    'newsletter': None,
    'video': 'assets/video/a-propos.mp4',
    # Flux JSON des dernières publications Instagram (ex. Behold.so, compte de Guido à relier). None = bouton « Suivre » seul.
    'instagram_feed': None,
}

# ── Séries, dans l'ordre voulu par l'artiste ──
SERIES = [
    ('phares', {'fr': 'Phares', 'nl': 'Vuurtorens', 'en': 'Lighthouses'}),
    ('glories', {'fr': 'Glories of the Past', 'nl': 'Glories of the Past', 'en': 'Glories of the Past'}),
    ('message', {'fr': 'Message in a Bottle', 'nl': 'Message in a Bottle', 'en': 'Message in a Bottle'}),
    ('peluches', {'fr': 'Peluches', 'nl': 'Knuffels', 'en': 'Plush Toys'}),
    ('divers', {'fr': 'Divers', 'nl': 'Diversen', 'en': 'Other works'}),
]

TECH = {
    'toile': {'fr': 'Acrylique sur toile', 'nl': 'Acryl op doek', 'en': 'Acrylic on canvas'},
    'carton': {'fr': 'Acrylique sur toile cartonnée', 'nl': 'Acryl op canvasboard', 'en': 'Acrylic on canvas board'},
}


def oeuvre(id, serie, titre, source, alt, annee=None, tech=None, dim=None):
    """Une œuvre originale. source : fichier dans « Oeuvres originales disponibles/ »."""
    return {'id': id, 'serie': serie, 'titre': titre, 'source': source, 'alt': alt,
            'annee': annee, 'tech': TECH[tech] if tech else None, 'dim': dim,
            'prix': None, 'vendue': False, 'desc': None, 'histoire': None}


# Années, techniques et formats : book 2025 et CV. Absents de ces documents = à fournir.
OEUVRES = [
    # Phares
    oeuvre('lighthouse-1', 'phares', 'Lighthouse 1', 'Serie_Phares/Lighthouse_1.jpg', {
        'fr': 'Phare posé sur une petite planète, au-dessus d’une nébuleuse orange dans l’espace',
        'nl': 'Vuurtoren op een kleine planeet, boven een oranje nevel in de ruimte',
        'en': 'Lighthouse on a small planet above an orange nebula in space'}),
    oeuvre('lighthouse-2', 'phares', 'Lighthouse 2', 'Serie_Phares/Lighthouse_2.JPG', {
        'fr': 'Phare allumé au milieu de dunes de sable rouge, sous un ciel embrasé',
        'nl': 'Brandende vuurtoren tussen rode zandduinen onder een gloeiende hemel',
        'en': 'Lit lighthouse among red sand dunes under a glowing sky'}),
    oeuvre('lighthouse-3', 'phares', 'Lighthouse 3', 'Serie_Phares/Lighthouse_3.png', {
        'fr': 'Phare au cœur d’une mer de nuages bleus, sous une trouée de ciel doré',
        'nl': 'Vuurtoren midden in een zee van blauwe wolken, onder een opening van gouden hemel',
        'en': 'Lighthouse in a sea of blue clouds beneath a break of golden sky'}),
    oeuvre('lighthouse-4', 'phares', 'Lighthouse 4', 'Serie_Phares/Lighthouse_4.png', {
        'fr': 'Phare dressé dans un volcan en éruption, des coulées de lave descendant vers la mer',
        'nl': 'Vuurtoren in een uitbarstende vulkaan, met lavastromen die naar de zee lopen',
        'en': 'Lighthouse inside an erupting volcano, lava flowing down to the sea'}),
    oeuvre('lighthouse-5', 'phares', 'Lighthouse 5', 'Serie_Phares/Lighthouse_5.png', {
        'fr': 'Phare couleur rouille sur un fond marin couvert de coraux, sous un tourbillon de lumière',
        'nl': 'Roestrode vuurtoren op een zeebodem vol koralen, onder een draaikolk van licht',
        'en': 'Rust-red lighthouse on a coral seabed beneath a swirl of light'}),
    # Glories of the Past
    oeuvre('glory-of-the-past-2', 'glories', 'Glory of the Past II', 'Serie_Gloriesofthepast/GloryofthepastII_Low_Res.png', {
        'fr': 'Voiture ancienne rouge et rouillée, abandonnée dans un sous-bois',
        'nl': 'Roestige rode oldtimer, achtergelaten in een bos',
        'en': 'Rusty red vintage car abandoned in a forest'}, 2018, 'carton', '33 × 41 cm'),
    oeuvre('glory-of-the-past-4', 'glories', 'Glory of the Past IV', 'Serie_Gloriesofthepast/GloryofthePastIVGalleryLowRes.png', {
        'fr': 'Moto de police blanche garée dans un vieux garage en bois',
        'nl': 'Witte politiemotor in een oude houten garage',
        'en': 'White police motorcycle parked in an old wooden garage'}, 2020, 'carton', '55 × 46 cm'),
    oeuvre('glory-of-the-past-5', 'glories', 'Glory of the Past V', 'Serie_Gloriesofthepast/GloryofthePastV_Low_Res.png', {
        'fr': 'Navette spatiale sur le dos d’un Boeing 747 posé dans l’herbe',
        'nl': 'Spaceshuttle op de rug van een Boeing 747 in het gras',
        'en': 'Space shuttle mounted on a Boeing 747 resting in the grass'}, 2020, 'carton', '55 × 46 cm'),
    oeuvre('glory-of-the-past-6', 'glories', 'Glory of the Past VI', 'Serie_Gloriesofthepast/Glory_of_the_past_VI.JPG', {
        'fr': 'Locomotive à vapeur rouillée au milieu d’une forêt de bouleaux',
        'nl': 'Roestige stoomlocomotief in een berkenbos',
        'en': 'Rusty steam locomotive in a birch forest'}),
    oeuvre('glory-of-the-past-7', 'glories', 'Glory of the Past VII', 'Serie_Gloriesofthepast/Glory_of_the_past_7.png', {
        'fr': 'Batmobile garée de nuit à l’orée d’un bois, sous la pleine lune',
        'nl': 'Batmobiel ’s nachts aan de rand van een bos, onder de volle maan',
        'en': 'Batmobile parked at the edge of a wood at night, under a full moon'}),
    # Message in a Bottle
    oeuvre('message-in-a-bottle', 'message', 'Message in a Bottle', 'Serie_Messageinabottle/MessageInABottle_LowRes.JPG', {
        'fr': 'Plage de galets au coucher du soleil, entre une falaise et des rochers dressés dans la mer',
        'nl': 'Kiezelstrand bij zonsondergang, tussen een klif en rotsen in zee',
        'en': 'Pebble beach at sunset between a cliff and sea stacks'}),
    oeuvre('message-in-a-bottle-2', 'message', 'Message in a Bottle II', 'Serie_Messageinabottle/Message in a bottle II.jpg', {
        'fr': 'Lac aux reflets roses et bleus semé de pierres rouges, un arbre isolé à l’horizon au soleil couchant',
        'nl': 'Meer met roze en blauwe weerspiegelingen en rode stenen, een eenzame boom aan de horizon bij zonsondergang',
        'en': 'Lake with pink and blue reflections and red stones, a lone tree on the horizon at sunset'}),
    # Peluches
    oeuvre('triceratops', 'peluches', 'Triceratops', 'Serie Peluches/Triceratops.jpg', {
        'fr': 'Tricératops en peluche à moitié mécanique, assis sur fond noir',
        'nl': 'Half mechanische knuffeltriceratops op een zwarte achtergrond',
        'en': 'Half-mechanical plush triceratops sitting on a black background'}),
    # Divers
    oeuvre('methuselah', 'divers', '24h in the Life of Methuselah', 'Divers/24h in the life of Methuselah_Low_Res.JPG', {
        'fr': 'Pin millénaire noueux, peint moitié de nuit sous les étoiles, moitié de jour sous un ciel bleu',
        'nl': 'Knoestige eeuwenoude den, half ’s nachts onder de sterren, half overdag onder een blauwe hemel',
        'en': 'Gnarled ancient pine, painted half at night under the stars, half by day under a blue sky'}, 2024, 'toile', '40 × 40 cm'),
    oeuvre('candies', 'divers', 'Candies', 'Divers/Candies_LowRes.jpg', {
        'fr': 'Grand bocal en verre rempli de bonbons colorés, sur fond orange',
        'nl': 'Grote glazen pot vol kleurrijke snoepjes op een oranje achtergrond',
        'en': 'Large glass jar full of colourful sweets on an orange background'}, 2024, 'carton', '27 × 35 cm'),
    oeuvre('puma', 'divers', 'Puma', 'Divers/Puma_Low_Res.jpg', {
        'fr': 'Félin noir aux yeux verts dans la pénombre de la jungle',
        'nl': 'Zwarte katachtige met groene ogen in het halfduister van de jungle',
        'en': 'Green-eyed black big cat in the shadows of the jungle'}),
    oeuvre('reflections', 'divers', 'Reflections', 'Divers/Reflections_v2.jpg', {
        'fr': 'Arbre isolé dans une plaine près d’une forêt blanche ; sous le sol, un monde étoilé',
        'nl': 'Eenzame boom in een vlakte bij een wit bos; onder de grond een wereld vol sterren',
        'en': 'Lone tree on a plain beside a white forest; beneath the ground, a starry world'}, 2024, 'carton', '60 × 40 cm'),
    oeuvre('sunset-at-mar-menor', 'divers', 'Sunset at Mar Menor', 'Divers/SunsetatMarMenor.jpg', {
        'fr': 'Coucher de soleil jaune sur la lagune, ciel bleu et rose reflété dans l’eau',
        'nl': 'Gele zonsondergang boven de lagune, blauwe en roze lucht weerspiegeld in het water',
        'en': 'Yellow sunset over the lagoon, blue and pink sky reflected in the water'}),
    oeuvre('the-cosmic-cat', 'divers', 'The Cosmic Cat', 'Divers/ThecosmicCatLowRes.jpg', {
        'fr': 'Ocelot debout au milieu des fleurs, sur un fond de ciel étoilé',
        'nl': 'Ocelot tussen de bloemen, tegen een sterrenhemel',
        'en': 'Ocelot standing among flowers against a starry sky'}, 2024, 'toile', '50 × 70 cm'),
    oeuvre('wave-at-sunset', 'divers', 'Wave at Sunset', 'Divers/WaveatSunset_Low_Res.jpg', {
        'fr': 'Vague qui déferle au coucher du soleil et se change en ciel étoilé',
        'nl': 'Golf die breekt bij zonsondergang en overgaat in een sterrenhemel',
        'en': 'Wave breaking at sunset and turning into a starry sky'}, 2024, 'toile', '40 × 40 cm'),
]

# ── Textes de l'artiste sur ses œuvres (FR repris tels quels, coquilles corrigées ; NL et EN : nos traductions,
#    à faire valider). Les œuvres absentes de ces documents restent sans texte en attendant sa fiche. ──

# Description : CV (« Sélection d'œuvres », 4 œuvres).
DESCRIPTIONS = {
    'glory-of-the-past-2': {
        'fr': 'Une automobile ancienne abandonnée dans la végétation, issue de la série Glory of the Past, consacrée aux lieux et aux objets oubliés. La scène met en tension la mémoire industrielle, le passage du temps et la reprise du vivant.',
        'nl': 'Een oude auto, achtergelaten tussen het groen, uit de reeks Glory of the Past, gewijd aan vergeten plekken en voorwerpen. De scène zet het industriële geheugen, het verstrijken van de tijd en de terugkeer van de natuur tegenover elkaar.',
        'en': 'A vintage car abandoned in the undergrowth, from the Glory of the Past series, devoted to forgotten places and objects. The scene sets industrial memory, the passing of time and nature’s return against one another.'},
    'candies': {
        'fr': 'Une étude de la transparence et de la lumière sur le verre. La bonbonnière devient une scène de couleur, de matière et de reflets, où l’abondance sucrée dialogue avec la précision hyperréaliste.',
        'nl': 'Een studie van transparantie en licht op glas. De snoeppot wordt een scène van kleur, textuur en weerspiegelingen, waarin zoete overvloed en hyperrealistische precisie met elkaar in dialoog gaan.',
        'en': 'A study of transparency and light on glass. The sweet jar becomes a scene of colour, texture and reflections, where sugary abundance meets hyperrealist precision.'},
    'the-cosmic-cat': {
        'fr': 'Une figure féline au cœur d’un paysage nocturne et fleuri. L’animal, motif récurrent de l’artiste, devient une présence presque cosmique, à la fois sauvage, contemplative et mystérieuse.',
        'nl': 'Een katachtige figuur in het hart van een nachtelijk, bloeiend landschap. Het dier, een terugkerend motief van de kunstenaar, wordt een bijna kosmische aanwezigheid, tegelijk wild, beschouwend en mysterieus.',
        'en': 'A feline figure at the heart of a flowering night landscape. The animal, a recurring motif for the artist, becomes an almost cosmic presence, at once wild, contemplative and mysterious.'},
    'wave-at-sunset': {
        'fr': 'Une vision de la mer où le coucher de soleil, la vague et le ciel se fondent dans un mouvement de transformation. La mémoire des plages portugaises se traduit par une palette intense et une énergie presque planétaire.',
        'nl': 'Een beeld van de zee waarin zonsondergang, golf en hemel samensmelten in een beweging van verandering. De herinnering aan de Portugese stranden vertaalt zich in een intens palet en een bijna planetaire energie.',
        'en': 'A vision of the sea where sunset, wave and sky merge in a movement of transformation. Memories of Portuguese beaches come through in an intense palette and an almost planetary energy.'},
}

# Histoire : book 2025 (« Galerie », pp. 8-17), dans les mots de l'artiste.
HISTOIRES = {
    'glory-of-the-past-2': {
        'fr': 'Ce chef-d’œuvre est le numéro deux de la saga « Gloire du passé » !',
        'nl': 'Dit werk is nummer twee uit de reeks “Glorie van het verleden”!',
        'en': 'This piece is number two in the “Glory of the Past” saga!'},
    'glory-of-the-past-4': {
        'fr': 'Pour ce chef-d’œuvre, numéro quatre de la saga « Glory of the Past », j’ai puisé mon inspiration dans la série télévisée culte des années 70, « CHiPs ».',
        'nl': 'Voor dit werk, nummer vier uit de reeks “Glory of the Past”, liet ik me inspireren door de cultserie uit de jaren 70, “CHiPs”.',
        'en': 'For this piece, number four in the “Glory of the Past” saga, I drew my inspiration from the cult 1970s TV series “CHiPs”.'},
    'glory-of-the-past-5': {
        'fr': 'Cette toile est le numéro cinq de la saga « Gloire du passé ». Ici, j’ai puisé mon inspiration dans une image qui m’a ébloui, gamin, lors d’une escapade à l’Atomium de Bruxelles.',
        'nl': 'Dit doek is nummer vijf uit de reeks “Glorie van het verleden”. Hier liet ik me inspireren door een beeld dat me als kind verblindde tijdens een uitstapje naar het Atomium in Brussel.',
        'en': 'This canvas is number five in the “Glory of the Past” saga. Here I drew on an image that dazzled me as a kid during a trip to the Atomium in Brussels.'},
    'methuselah': {
        'fr': 'Un toast à l’arbre le plus âgé de la planète !',
        'nl': 'Een toast op de oudste boom van de planeet!',
        'en': 'A toast to the oldest tree on the planet!'},
    'candies': {
        'fr': 'J’ai un faible pour tout ce qui brille en verre et pour la danse de la lumière sur ce matériau. Quant à cette bonbonnière, son contenu sucré m’a donné un bon coup de sucre !',
        'nl': 'Ik heb een zwak voor alles wat in glas schittert en voor de dans van het licht op dat materiaal. En de zoete inhoud van deze snoeppot gaf me een flinke suikerstoot!',
        'en': 'I have a soft spot for anything that sparkles in glass and for the dance of light on it. As for this sweet jar, its sugary contents gave me quite a sugar rush!'},
    'reflections': {
        'fr': 'Pour ce chef-d’œuvre, j’ai puisé mon inspiration dans un paysage enchanteur de Nouvelle-Zélande.',
        'nl': 'Voor dit werk liet ik me inspireren door een betoverend landschap in Nieuw-Zeeland.',
        'en': 'For this piece, I drew my inspiration from an enchanting landscape in New Zealand.'},
    'the-cosmic-cat': {
        'fr': 'Cette toile est une ode à mon adoration pour les félins. Au début, un pote m’avait confié qu’il serait ravi de voir un tableau d’un chat sauvage qu’il avait vu en photo. Mais son souhait s’est vite envolé, se métamorphosant en une aventure artistique personnelle pour moi.',
        'nl': 'Dit doek is een ode aan mijn liefde voor katachtigen. Eerst vertelde een vriend me dat hij graag een schilderij zou zien van een wilde kat die hij op een foto had gezien. Maar zijn wens verdween al snel en veranderde in een persoonlijk artistiek avontuur voor mij.',
        'en': 'This canvas is an ode to my love of felines. At first, a friend told me he would love to see a painting of a wild cat he had seen in a photo. But his wish soon faded away, turning into a personal artistic adventure for me.'},
    'wave-at-sunset': {
        'fr': 'Après avoir passé une éternité de mes étés à flâner sur les plages portugaises, il n’est guère surprenant que la mer et ses vagues aient fini par me marquer profondément.',
        'nl': 'Na eindeloze zomers op de Portugese stranden is het geen verrassing dat de zee en haar golven een diepe indruk op me hebben nagelaten.',
        'en': 'After spending an eternity of summers wandering along Portuguese beaches, it is hardly surprising that the sea and its waves ended up leaving a deep mark on me.'},
}

for _o in OEUVRES:
    _o['desc'] = DESCRIPTIONS.get(_o['id'])
    _o['histoire'] = HISTOIRES.get(_o['id'])
assert set(DESCRIPTIONS) | set(HISTOIRES) <= {o['id'] for o in OEUVRES}, 'identifiant d’œuvre inconnu'

# ── Prints : tirages d'art (vendus sur Etsy) — prix « à partir de », à revoir par l'artiste avec son fournisseur ──
PRINT_FORMATS = [
    ({'fr': 'Petit', 'nl': 'Klein', 'en': 'Small'}, '30 × 40 cm', 18),
    ({'fr': 'Moyen', 'nl': 'Middel', 'en': 'Medium'}, '40 × 50 cm', 23),
    ({'fr': 'Grand', 'nl': 'Groot', 'en': 'Large'}, '45 × 61 cm', 28),
    ({'fr': 'Très grand', 'nl': 'Extra groot', 'en': 'Extra large'}, '61 × 81 cm', 46),
]

# ── FAQ : FAQ.pdf de l'artiste (EN) ; FR et NL traduits par nos soins, à faire valider ──
FAQ = {
    'fr': [
        ('Qu’est-ce qui vous a donné envie de devenir artiste ?', 'J’ai toujours été passionné par l’envie d’exprimer des émotions et de saisir la beauté du monde et de l’esprit humain à travers l’art. Mon parcours a commencé très jeune et a évolué au fil des années, à mesure que j’explorais différents médiums et styles.'),
        ('Avec quels médiums travaillez-vous ?', 'Je travaille surtout à l’acrylique et à l’aquarelle, mais j’aime aussi expérimenter les techniques mixtes pour donner à mes pièces d’autres textures et d’autres dimensions.'),
        ('Pouvez-vous nous en dire plus sur votre parcours artistique ?', 'J’ai suivi des cours d’art pendant ma scolarité, puis quelques cours pendant plusieurs années, mais je suis surtout autodidacte. J’ai exposé en Espagne : collectivement en 2017, dans une foire d’art en 2018 et en galerie en 2019. Mon style est influencé par des surréalistes comme Salvador Dalí et René Magritte, et je puise mon inspiration dans la nature, la société et la vie sauvage.'),
        ('À quel rythme la galerie est-elle mise à jour ?', 'J’ajoute de nouvelles œuvres chaque mois : revenez régulièrement pour découvrir les dernières.'),
        ('Les œuvres de la galerie sont-elles à vendre ?', 'Oui, la plupart des œuvres de la galerie sont disponibles, en original ou en print. Vous trouverez plus de détails dans la boutique, ou contactez-moi directement.'),
        ('Quels moyens de paiement acceptez-vous ?', 'La boutique accepte les principales cartes de crédit, PayPal et le virement bancaire. Toutes les transactions sont sécurisées et chiffrées.'),
        ('Livrez-vous à l’international ?', 'Oui, j’expédie toutes les œuvres à l’international. Les frais et délais de livraison dépendent de la destination : consultez les conditions de livraison de la boutique.'),
        ('Quelle est votre politique de retour ?', 'Je tiens à ce que vous soyez entièrement satisfait de votre achat. Si ce n’est pas le cas, contactez-moi dans les 15 jours suivant la réception de l’œuvre pour convenir d’un retour ou d’un échange.'),
        ('Comment vous contacter pour une commande ou une collaboration ?', 'Par la page Contact du site, ou directement par e-mail à info@guidodeoliveira.com. Je suis toujours ouvert aux commandes et aux projets en collaboration.'),
        ('Donnez-vous des cours ou des ateliers ?', 'Pas pour le moment, mais c’est prévu dans un avenir proche. Suivez les actualités du site ou abonnez-vous à la newsletter : elle vous tient informé chaque mois de mes activités et vous permet de participer à mes concours mensuels.'),
        ('Puis-je voir vos œuvres en vrai ?', 'Mes œuvres sont régulièrement présentées dans des expositions et des galeries. Consultez la page À propos pour connaître les expositions en cours et à venir.'),
    ],
    'nl': [
        ('Wat inspireerde u om kunstenaar te worden?', 'Ik heb altijd een passie gehad voor het uitdrukken van emoties en het vastleggen van de schoonheid van de wereld en de menselijke geest door kunst. Mijn reis begon op jonge leeftijd en is door de jaren heen gegroeid, terwijl ik verschillende media en stijlen bleef verkennen.'),
        ('Met welke media werkt u?', 'Ik werk vooral met acrylverf en aquarel, maar experimenteer ook graag met gemengde technieken om mijn werken andere texturen en dimensies te geven.'),
        ('Kunt u meer vertellen over uw artistieke achtergrond?', 'Ik volgde kunstlessen op school en daarna enkele jaren bijkomende lessen, maar ik ben grotendeels autodidact. Ik heb in Spanje tentoongesteld: in groep in 2017, op een kunstbeurs in 2018 en in galerieën in 2019. Mijn stijl is beïnvloed door surrealisten zoals Salvador Dalí en René Magritte, en ik haal mijn inspiratie uit de natuur, de maatschappij en het wilde leven.'),
        ('Hoe vaak wordt de galerij bijgewerkt?', 'Ik voeg elke maand nieuwe werken toe: kom dus regelmatig terug voor de nieuwste.'),
        ('Zijn de werken in de galerij te koop?', 'Ja, de meeste werken in de galerij zijn te koop, als origineel of als print. Meer details vindt u in de winkel, of neem rechtstreeks contact met me op.'),
        ('Welke betaalmiddelen aanvaardt u?', 'De winkel aanvaardt de belangrijkste kredietkaarten, PayPal en overschrijving. Alle transacties zijn beveiligd en versleuteld.'),
        ('Levert u ook internationaal?', 'Ja, ik verzend alle werken internationaal. Verzendkosten en levertijden hangen af van de bestemming: zie de leveringsvoorwaarden van de winkel.'),
        ('Wat is uw retourbeleid?', 'Ik wil dat u volledig tevreden bent met uw aankoop. Is dat niet het geval, neem dan binnen 15 dagen na ontvangst contact met me op om een retour of omruiling af te spreken.'),
        ('Hoe neem ik contact op voor een opdracht of samenwerking?', 'Via de contactpagina van de website, of rechtstreeks per e-mail op info@guidodeoliveira.com. Ik sta altijd open voor opdrachten en samenwerkingen.'),
        ('Geeft u lessen of workshops?', 'Op dit moment niet, maar dat staat gepland in de nabije toekomst. Volg het nieuws op de website of schrijf je in op de nieuwsbrief: zo blijf je elke maand op de hoogte van mijn activiteiten en maak je kans in mijn maandelijkse wedstrijden.'),
        ('Kan ik uw werken in het echt zien?', 'Mijn werken zijn regelmatig te zien op tentoonstellingen en in galerieën. Op de pagina Over mij vindt u de lopende en komende tentoonstellingen.'),
    ],
    'en': [
        ('What inspired you to become an artist?', 'I have always been passionate about expressing emotions and capturing the beauty of the world and the human mind through art. My journey began at a young age and has evolved over the years as I continued to explore various mediums and styles.'),
        ('What mediums do you work with?', 'I primarily work with acrylic paints and watercolours, but I also enjoy experimenting with mixed media to bring different textures and dimensions to my pieces.'),
        ('Can you tell us more about your artistic background?', 'I attended art lessons at school and further lessons for some years, but for the most part I am self-taught. I have exhibited my work in Spain: collectively in 2017, at an art fair in 2018 and in galleries in 2019. My style is influenced by surrealist artists like Salvador Dalí, René Magritte and others, and I draw inspiration from nature, society and wildlife.'),
        ('How often do you update the gallery with new works?', 'I update the gallery with new works every month, so be sure to check back regularly for the latest additions.'),
        ('Are the artworks in the gallery available for purchase?', 'Yes, most of the artworks displayed in the gallery are available for purchase, either as originals or prints. You can find more details in the shop or contact me directly.'),
        ('What payment methods do you accept?', 'The shop accepts major credit cards, PayPal and bank transfers. All transactions are secure and encrypted for your safety.'),
        ('Do you offer international shipping?', 'Yes, I offer international shipping for all artworks. Shipping fees and delivery times vary depending on the destination: please refer to the shop’s shipping policy.'),
        ('What is your return policy?', 'I want you to be completely satisfied with your purchase. If you’re not, please contact me within 15 days of receiving the artwork to discuss a return or exchange.'),
        ('How can I contact you for commissions or collaborations?', 'Through the Contact page of the website, or email me directly at info@guidodeoliveira.com. I am always open to discussing commissions and collaborative projects.'),
        ('Do you offer art classes or workshops?', 'Not at present, but I intend to in the near future. Check the news on my website regularly or subscribe to my newsletter to hear every month about my current and upcoming activities, and for a chance to win my monthly giveaways.'),
        ('Can I view your artworks in person?', 'My works are occasionally featured in exhibitions and galleries. Visit the About page for current and upcoming exhibitions where you can see my work in person.'),
    ],
}


# ── Expositions, distinctions, presse (book 2025 p. 19 et CV ; affiché dans « À propos ») ──
# Dates au format AAAA-MM-JJ, mises en forme par build.py. La FAQ de l'artiste cite 2017-2019 :
# rien de tel dans le book ni le CV, donc pas repris ici (à faire préciser par l'artiste).
EXPOSITIONS = [
    ('Hotel Casa Palacio Maria-Luisa', {'fr': 'Jerez de la Frontera, Espagne', 'nl': 'Jerez de la Frontera, Spanje',
                                        'en': 'Jerez de la Frontera, Spain'}, '2020-03-06', '2020-04-06'),
    ('Hotel Oca Puerta del Camino', {'fr': 'Saint-Jacques-de-Compostelle, Espagne', 'nl': 'Santiago de Compostela, Spanje',
                                     'en': 'Santiago de Compostela, Spain'}, '2020-09-11', '2020-10-11'),
    ('Modern & Contemporary Art Show Marbella', {'fr': 'Marbella, Espagne', 'nl': 'Marbella, Spanje',
                                                 'en': 'Marbella, Spain'}, '2020-10-24', '2020-11-03'),
]

# « Mundoarti » dans le book, « Munduarti » dans le CV : orthographe du book retenue, à confirmer.
DISTINCTIONS = [
    ({'fr': 'Finaliste du 5e Salon de printemps de la peinture réaliste, organisé par les galeries Avatarte (Madrid) '
            'et Mundoarti (Valence)',
      'nl': 'Finalist van de 5de Lentesalon van de realistische schilderkunst, georganiseerd door de galerieën '
            'Avatarte (Madrid) en Mundoarti (Valencia)',
      'en': 'Finalist, 5th Spring Salon of Realist Painting, organised by the Avatarte (Madrid) and Mundoarti (Valencia) '
            'galleries'}, '2020-04'),
]

PRESSE = [('House & Garden', 2017), ('The World of Interiors', 2017), ('Mayfair Life', 2023)]

COLLABORATIONS = {'fr': ['Couverture de livre', 'Single LP'],
                  'nl': ['Boekomslag', 'Lp-single'],
                  'en': ['Book cover', 'LP single']}
