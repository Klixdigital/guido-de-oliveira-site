"""Textes légaux : conditions générales de vente et politique de confidentialité.

Source : les deux documents de l'artiste (more info/, reçus le 2026-11-05), repris fidèlement en français,
mise en forme et coquilles corrigées seulement. NL et EN : traductions de courtoisie faites par nos soins,
la version française prévaut (mention affichée sur ces pages).

Écarts volontaires par rapport aux documents, tous à faire valider par l'artiste :
- CGV, section « Vendeur » ajoutée : identification obligatoire du vendeur en ligne ; adresse et numéro
  d'entreprise affichés « À fournir ».
- CGV, « Contact » : e-mail du site au lieu de « l'adresse électronique ou le numéro de téléphone fournis
  sur le site », aucun téléphone n'y figurant.
- Confidentialité : « [adresse e-mail de contact] » remplacé par l'e-mail du site.
- Confidentialité, section « Newsletter » ajoutée (2026-11-05) : le site a un formulaire d'inscription,
  le document de l'artiste n'en parlait pas.

Balises dans les textes : {email} et {redbubble} deviennent des liens, {todo} la mention « À fournir ».
Blocs : ('p', texte) ou ('li', intitulé ou None, texte) ; les 'li' qui se suivent forment une liste.
"""

UPDATED = {'fr': 'Dernière mise à jour : 5 novembre 2026',
           'nl': 'Laatst bijgewerkt: 5 november 2026',
           'en': 'Last updated: 5 November 2026'}

COURTESY = {'nl': 'Vertaling ter informatie. Bij verschillen tussen de versies heeft de Franse tekst voorrang.',
            'en': 'Courtesy translation. In case of any discrepancy, the French version prevails.'}

# ── Conditions générales de vente ─────────────────────────────────────

CGV = {
    'fr': {
        'title': 'Conditions générales de vente',
        'lead': 'Les conditions applicables aux achats d’œuvres originales et d’impressions sur ce site.',
        'sections': [
            ('Vendeur', [
                ('li', 'Nom', 'Guido De Oliveira (Guiarte), artiste peintre'),
                ('li', 'Adresse', '{todo}'),
                ('li', 'Numéro d’entreprise et TVA', '{todo}'),
                ('li', 'E-mail', '{email}'),
            ]),
            ('Description des produits', [
                ('li', 'Peintures originales', 'Pièces uniques, peintes à l’aquarelle, à l’acrylique ou en technique mixte. '
                 'Toile de première qualité (lin belge ou 100 % coton) sur châssis de différentes tailles selon le sujet. '
                 'Papier aquarelle 100 % coton avec un grain de 300 g/m².'),
                ('li', 'Impressions HQ', 'Reproductions de haute qualité : l’œuvre originale est numérisée en haute résolution '
                 'à l’aide de scanners numériques de pointe, puis imprimée à l’aide d’imprimantes d’art sur du papier ou de la '
                 'toile de qualité supérieure.'),
                ('li', 'Accessoires de merchandising', 'Divers articles imprimés avec les œuvres de l’artiste sont disponibles '
                 'sur la boutique {redbubble}. Les CGV de cette catégorie de produits sont celles du fournisseur de ces articles, '
                 'accessibles sur son site web.'),
            ]),
            ('Processus de commande', [
                ('li', 'Étapes de la commande', 'Lorsque le client choisit un produit, il est invité à suivre les instructions '
                 'à l’écran pour une meilleure expérience d’achat.'),
                ('li', 'Confirmation de commande', 'Lorsque la commande est confirmée, le client reçoit un message indiquant '
                 'qu’un courriel de confirmation lui a été envoyé à l’adresse e-mail qu’il a indiquée.'),
            ]),
            ('Paiement', [
                ('li', 'Modes de paiement acceptés', 'Carte de crédit ou de débit, PayPal, virement bancaire, etc.'),
                ('li', 'Sécurité des transactions', 'Guiarte utilise un système de paiement en ligne sécurisé (Stripe).'),
            ]),
            ('Livraison', [
                ('li', 'Délais de livraison', 'Selon la destination (nationale ou internationale), les œuvres sont expédiées '
                 'dans les 10 jours ouvrables suivant la confirmation de commande, sauf indication contraire.'),
                ('li', 'Frais de livraison', 'Les frais de livraison sont inclus pour toute commande d’un montant total minimum '
                 'de 75 € HTVA. En dessous de ce montant, ils sont calculés en fonction de la destination et du poids '
                 '(volume en m³ ou poids en kg) des œuvres.'),
                ('li', 'Transporteurs', 'DHL, UPS Express.'),
            ]),
            ('Retours et remboursement', [
                ('li', 'Délai de rétractation', 'Le client dispose d’un délai de 14 jours à compter de la réception de la '
                 'commande pour exercer son droit de rétractation, sans avoir à justifier de motifs.'),
                ('li', 'Procédure de retour', 'Pour exercer ce droit, le client doit retourner l’œuvre dans son emballage '
                 'd’origine et en parfait état.'),
            ]),
            ('Service client', [
                ('li', 'Contact', 'Pour toute question ou réclamation, les clients peuvent contacter le service client à '
                 'l’adresse {email}.'),
                ('li', 'Heures d’ouverture', 'Sans objet : le service est en ligne.'),
            ]),
            ('Propriété intellectuelle', [
                ('li', 'Droits d’auteur', 'Toutes les œuvres et images présentées sur le site sont protégées par le droit '
                 'd’auteur. Toute reproduction est interdite sans autorisation préalable.'),
            ]),
            ('Responsabilité', [
                ('li', 'Exactitude des informations', 'Bien que les descriptions des œuvres soient aussi précises que possible, '
                 'de légères variations de couleur peuvent apparaître en raison des différences d’affichage des écrans.'),
                ('li', 'Limitation de responsabilité', 'L’artiste ne peut être tenu responsable des dommages indirects '
                 'résultant de l’achat des œuvres.'),
                ('li', 'Garanties', 'Le vendeur est tenu de garantir à l’acheteur que l’objet vendu ne présente pas de vices '
                 'cachés et qu’il est conforme à la description donnée lors de la vente.'),
            ]),
            ('Modification des CGV', [
                ('li', 'Droit de modification', 'L’artiste se réserve le droit de modifier les CGV à tout moment. '
                 'Les modifications sont applicables dès leur mise en ligne.'),
            ]),
        ],
    },
    'nl': {
        'title': 'Algemene verkoopvoorwaarden',
        'lead': 'De voorwaarden voor de aankoop van originele werken en prints op deze website.',
        'sections': [
            ('Verkoper', [
                ('li', 'Naam', 'Guido De Oliveira (Guiarte), kunstschilder'),
                ('li', 'Adres', '{todo}'),
                ('li', 'Ondernemingsnummer en btw', '{todo}'),
                ('li', 'E-mail', '{email}'),
            ]),
            ('Beschrijving van de producten', [
                ('li', 'Originele schilderijen', 'Unieke stukken, geschilderd in aquarel, acryl of gemengde techniek. '
                 'Doek van topkwaliteit (Belgisch linnen of 100 % katoen) op spieraam, in verschillende formaten naargelang '
                 'het onderwerp. Aquarelpapier van 100 % katoen met een korrel van 300 g/m².'),
                ('li', 'HQ-prints', 'Reproducties van hoge kwaliteit: het originele werk wordt met geavanceerde digitale '
                 'scanners in hoge resolutie ingescand en vervolgens met kunstprinters afgedrukt op papier of doek van '
                 'superieure kwaliteit.'),
                ('li', 'Merchandising', 'Verschillende artikelen met de werken van de kunstenaar zijn verkrijgbaar in de winkel '
                 '{redbubble}. Voor deze productcategorie gelden de verkoopvoorwaarden van de leverancier van deze artikelen, '
                 'te raadplegen op diens website.'),
            ]),
            ('Bestelproces', [
                ('li', 'Stappen van de bestelling', 'Wanneer de klant een product kiest, wordt hij gevraagd de instructies op '
                 'het scherm te volgen voor een betere aankoopervaring.'),
                ('li', 'Bevestiging van de bestelling', 'Zodra de bestelling bevestigd is, ontvangt de klant een bericht dat er '
                 'een bevestigingsmail is verzonden naar het e-mailadres dat hij heeft opgegeven.'),
            ]),
            ('Betaling', [
                ('li', 'Aanvaarde betaalmiddelen', 'Krediet- of debetkaart, PayPal, overschrijving, enz.'),
                ('li', 'Veiligheid van de transacties', 'Guiarte gebruikt een beveiligd onlinebetaalsysteem (Stripe).'),
            ]),
            ('Levering', [
                ('li', 'Leveringstermijn', 'Afhankelijk van de bestemming (binnenland of buitenland) worden de werken binnen '
                 '10 werkdagen na de bevestiging van de bestelling verzonden, tenzij anders vermeld.'),
                ('li', 'Verzendkosten', 'De verzendkosten zijn inbegrepen voor elke bestelling met een totaalbedrag van minimaal '
                 '75 € exclusief btw. Onder dat bedrag worden ze berekend op basis van de bestemming en het gewicht (volume in m³ '
                 'of gewicht in kg) van de werken.'),
                ('li', 'Vervoerders', 'DHL, UPS Express.'),
            ]),
            ('Retour en terugbetaling', [
                ('li', 'Herroepingstermijn', 'De klant beschikt over een termijn van 14 dagen vanaf de ontvangst van de '
                 'bestelling om zijn herroepingsrecht uit te oefenen, zonder opgave van redenen.'),
                ('li', 'Retourprocedure', 'Om dit recht uit te oefenen, stuurt de klant het werk terug in de originele '
                 'verpakking en in perfecte staat.'),
            ]),
            ('Klantenservice', [
                ('li', 'Contact', 'Voor vragen of klachten kunnen klanten contact opnemen met de klantenservice via {email}.'),
                ('li', 'Openingsuren', 'Niet van toepassing: de dienst is online.'),
            ]),
            ('Intellectuele eigendom', [
                ('li', 'Auteursrecht', 'Alle werken en afbeeldingen op deze website zijn auteursrechtelijk beschermd. '
                 'Elke reproductie zonder voorafgaande toestemming is verboden.'),
            ]),
            ('Aansprakelijkheid', [
                ('li', 'Juistheid van de informatie', 'Hoewel de beschrijvingen van de werken zo nauwkeurig mogelijk zijn, '
                 'kunnen er lichte kleurverschillen optreden door verschillen in schermweergave.'),
                ('li', 'Beperking van aansprakelijkheid', 'De kunstenaar kan niet aansprakelijk worden gesteld voor indirecte '
                 'schade als gevolg van de aankoop van de werken.'),
                ('li', 'Garanties', 'De verkoper garandeert de koper dat het verkochte voorwerp geen verborgen gebreken vertoont '
                 'en overeenstemt met de beschrijving die bij de verkoop werd gegeven.'),
            ]),
            ('Wijziging van de voorwaarden', [
                ('li', 'Recht op wijziging', 'De kunstenaar behoudt zich het recht voor deze voorwaarden op elk moment te '
                 'wijzigen. Wijzigingen zijn van toepassing zodra ze online staan.'),
            ]),
        ],
    },
    'en': {
        'title': 'Terms of sale',
        'lead': 'The terms that apply to purchases of original works and prints on this website.',
        'sections': [
            ('Seller', [
                ('li', 'Name', 'Guido De Oliveira (Guiarte), painter'),
                ('li', 'Address', '{todo}'),
                ('li', 'Company and VAT number', '{todo}'),
                ('li', 'Email', '{email}'),
            ]),
            ('Product description', [
                ('li', 'Original paintings', 'One-of-a-kind pieces, painted in watercolour, acrylic or mixed media. '
                 'Top-quality canvas (Belgian linen or 100% cotton) on stretcher bars, in various sizes depending on the subject. '
                 '100% cotton watercolour paper, 300 g/m².'),
                ('li', 'HQ prints', 'High-quality reproductions: the original work is scanned at high resolution with '
                 'state-of-the-art digital scanners, then printed with fine-art printers on premium paper or canvas.'),
                ('li', 'Merchandise', 'Various items printed with the artist’s works are available from the {redbubble} shop. '
                 'The terms of sale for this product category are those of the supplier of these items, available on its website.'),
            ]),
            ('Ordering', [
                ('li', 'Order steps', 'Once the customer has chosen a product, they are asked to follow the on-screen '
                 'instructions for a smoother shopping experience.'),
                ('li', 'Order confirmation', 'When the order is confirmed, the customer receives a message stating that a '
                 'confirmation email has been sent to the email address they provided.'),
            ]),
            ('Payment', [
                ('li', 'Accepted payment methods', 'Credit or debit card, PayPal, bank transfer, etc.'),
                ('li', 'Secure transactions', 'Guiarte uses a secure online payment system (Stripe).'),
            ]),
            ('Delivery', [
                ('li', 'Delivery times', 'Depending on the destination (domestic or international), works are shipped within '
                 '10 working days of order confirmation, unless stated otherwise.'),
                ('li', 'Shipping costs', 'Shipping is included for any order with a total of at least €75 excluding VAT. '
                 'Below that amount, shipping is calculated according to the destination and the weight (volume in m³ or '
                 'weight in kg) of the works.'),
                ('li', 'Carriers', 'DHL, UPS Express.'),
            ]),
            ('Returns and refunds', [
                ('li', 'Withdrawal period', 'The customer has 14 days from receipt of the order to exercise their right of '
                 'withdrawal, without having to give any reason.'),
                ('li', 'Return procedure', 'To exercise this right, the customer must return the work in its original '
                 'packaging and in perfect condition.'),
            ]),
            ('Customer service', [
                ('li', 'Contact', 'For any question or complaint, customers can contact customer service at {email}.'),
                ('li', 'Opening hours', 'Not applicable: the service is online.'),
            ]),
            ('Intellectual property', [
                ('li', 'Copyright', 'All works and images shown on this website are protected by copyright. Any reproduction '
                 'without prior permission is prohibited.'),
            ]),
            ('Liability', [
                ('li', 'Accuracy of information', 'Although the descriptions of the works are as accurate as possible, slight '
                 'colour variations may occur due to differences between screens.'),
                ('li', 'Limitation of liability', 'The artist cannot be held liable for indirect damage resulting from the '
                 'purchase of the works.'),
                ('li', 'Warranties', 'The seller guarantees to the buyer that the item sold has no hidden defects and matches '
                 'the description given at the time of sale.'),
            ]),
            ('Changes to these terms', [
                ('li', 'Right to amend', 'The artist reserves the right to amend these terms at any time. Changes apply as '
                 'soon as they are published online.'),
            ]),
        ],
    },
}

# ── Politique de confidentialité ──────────────────────────────────────

PRIVACY = {
    'fr': {
        'title': 'Politique de confidentialité',
        'lead': 'Comment vos données personnelles sont collectées, utilisées et protégées sur ce site.',
        'sections': [
            ('Introduction', [
                ('p', 'Bienvenue sur le site web de Guido De Oliveira. La protection de votre vie privée est d’une importance '
                 'capitale pour nous. Cette politique de confidentialité décrit comment nous collectons, utilisons et protégeons '
                 'vos informations personnelles lorsque vous visitez notre site web et utilisez notre e-shop.'),
            ]),
            ('Informations collectées', [
                ('p', 'Nous collectons plusieurs types d’informations pour vous fournir nos services et améliorer votre '
                 'expérience sur notre site :'),
                ('li', 'Informations personnelles', 'telles que votre nom, votre adresse e-mail, votre adresse postale et votre '
                 'numéro de téléphone lorsque vous créez un compte ou effectuez un achat.'),
                ('li', 'Informations de paiement', 'les informations de carte de crédit ou d’autres moyens de paiement sont '
                 'traitées de manière sécurisée par nos partenaires de paiement.'),
                ('li', 'Informations sur l’utilisation', 'données concernant votre interaction avec le site, y compris les pages '
                 'visitées et les produits vus ou ajoutés à votre panier.'),
            ]),
            ('Utilisation des informations', [
                ('p', 'Nous utilisons vos informations pour :'),
                ('li', None, 'traiter vos commandes et gérer votre compte ;'),
                ('li', None, 'améliorer notre site web et personnaliser votre expérience d’achat ;'),
                ('li', None, 'communiquer avec vous au sujet de vos commandes, de nos produits et de nos offres spéciales ;'),
                ('li', None, 'respecter nos obligations légales et réglementaires.'),
            ]),
            ('Newsletter', [
                ('p', 'Si vous vous inscrivez à la newsletter, nous conservons votre nom et votre adresse e-mail dans le '
                 'seul but de vous l’envoyer : nouvelles œuvres, expositions et sorties de prints. Vous pouvez vous '
                 'désinscrire à tout moment, sur simple demande à {email} ; votre adresse est alors retirée de la liste.'),
            ]),
            ('Partage des informations', [
                ('p', 'Nous nous engageons à ne pas vendre, échanger ou louer vos informations personnelles à des tiers. '
                 'Nous pouvons cependant partager vos données avec des partenaires de confiance pour :'),
                ('li', None, 'traiter les paiements et livrer vos commandes ;'),
                ('li', None, 'gérer notre site web et ses services associés ;'),
                ('li', None, 'respecter nos obligations légales ou protéger nos droits et ceux de nos utilisateurs.'),
            ]),
            ('Sécurité des données', [
                ('p', 'Nous prenons des mesures de sécurité appropriées pour protéger vos informations contre l’accès non '
                 'autorisé, la divulgation, l’altération ou la destruction. Nos partenaires de paiement utilisent des '
                 'technologies de chiffrement pour sécuriser vos transactions financières.'),
            ]),
            ('Cookies', [
                ('p', 'Notre site utilise des cookies pour améliorer votre expérience en ligne. Les cookies sont de petits '
                 'fichiers stockés sur votre appareil qui nous aident à analyser le trafic web et à personnaliser le contenu. '
                 'Vous pouvez choisir de désactiver les cookies dans les paramètres de votre navigateur, bien que cela puisse '
                 'affecter le fonctionnement du site.'),
            ]),
            ('Vos droits', [
                ('p', 'Vous avez le droit de :'),
                ('li', None, 'accéder aux informations personnelles que nous détenons à votre sujet ;'),
                ('li', None, 'demander la correction de vos informations personnelles inexactes ;'),
                ('li', None, 'demander la suppression de vos informations personnelles, sous réserve de certaines exceptions '
                 'légales.'),
            ]),
            ('Modifications de la politique', [
                ('p', 'Nous pouvons mettre à jour cette politique de confidentialité de temps à autre. Toute modification sera '
                 'affichée sur cette page avec la date de mise à jour. Nous vous encourageons à consulter régulièrement cette '
                 'page pour être informé des changements.'),
            ]),
            ('Contact', [
                ('p', 'Si vous avez des questions ou des préoccupations concernant notre politique de confidentialité, '
                 'contactez-nous à l’adresse {email}.'),
                ('p', 'Merci de votre confiance et de votre fidélité.'),
            ]),
        ],
    },
    'nl': {
        'title': 'Privacybeleid',
        'lead': 'Hoe je persoonsgegevens op deze website worden verzameld, gebruikt en beschermd.',
        'sections': [
            ('Inleiding', [
                ('p', 'Welkom op de website van Guido De Oliveira. De bescherming van je privacy is voor ons van het grootste '
                 'belang. Dit privacybeleid beschrijft hoe wij je persoonsgegevens verzamelen, gebruiken en beschermen wanneer '
                 'je onze website bezoekt en onze webshop gebruikt.'),
            ]),
            ('Verzamelde gegevens', [
                ('p', 'Wij verzamelen verschillende soorten gegevens om je onze diensten te leveren en je ervaring op onze '
                 'website te verbeteren:'),
                ('li', 'Persoonsgegevens', 'zoals je naam, e-mailadres, postadres en telefoonnummer wanneer je een account '
                 'aanmaakt of een aankoop doet.'),
                ('li', 'Betaalgegevens', 'gegevens van je kredietkaart of andere betaalmiddelen worden veilig verwerkt door onze '
                 'betaalpartners.'),
                ('li', 'Gebruiksgegevens', 'gegevens over je interactie met de website, waaronder de bezochte pagina’s en de '
                 'producten die je hebt bekeken of in je winkelmand hebt gelegd.'),
            ]),
            ('Gebruik van de gegevens', [
                ('p', 'Wij gebruiken je gegevens om:'),
                ('li', None, 'je bestellingen te verwerken en je account te beheren;'),
                ('li', None, 'onze website te verbeteren en je aankoopervaring te personaliseren;'),
                ('li', None, 'met je te communiceren over je bestellingen, onze producten en onze speciale aanbiedingen;'),
                ('li', None, 'onze wettelijke en reglementaire verplichtingen na te komen.'),
            ]),
            ('Nieuwsbrief', [
                ('p', 'Als je je inschrijft op de nieuwsbrief, bewaren wij je naam en e-mailadres met als enig doel je '
                 'de nieuwsbrief te sturen: nieuwe werken, tentoonstellingen en nieuwe prints. Je kunt je op elk moment '
                 'uitschrijven door een eenvoudig verzoek naar {email} te sturen; je adres wordt dan van de lijst verwijderd.'),
            ]),
            ('Delen van gegevens', [
                ('p', 'Wij verbinden ons ertoe je persoonsgegevens niet te verkopen, te ruilen of te verhuren aan derden. '
                 'Wij kunnen je gegevens wel delen met betrouwbare partners om:'),
                ('li', None, 'betalingen te verwerken en je bestellingen te leveren;'),
                ('li', None, 'onze website en de bijbehorende diensten te beheren;'),
                ('li', None, 'wettelijke verplichtingen na te komen of onze rechten en die van onze gebruikers te beschermen.'),
            ]),
            ('Beveiliging van de gegevens', [
                ('p', 'Wij nemen passende beveiligingsmaatregelen om je gegevens te beschermen tegen ongeoorloofde toegang, '
                 'openbaarmaking, wijziging of vernietiging. Onze betaalpartners gebruiken versleutelingstechnologie om je '
                 'financiële transacties te beveiligen.'),
            ]),
            ('Cookies', [
                ('p', 'Onze website gebruikt cookies om je onlinebeleving te verbeteren. Cookies zijn kleine bestanden die op je '
                 'toestel worden opgeslagen en ons helpen het webverkeer te analyseren en de inhoud te personaliseren. Je kunt '
                 'cookies uitschakelen in de instellingen van je browser, al kan dat de werking van de website beïnvloeden.'),
            ]),
            ('Je rechten', [
                ('p', 'Je hebt het recht om:'),
                ('li', None, 'de persoonsgegevens in te zien die wij over je bewaren;'),
                ('li', None, 'onjuiste persoonsgegevens te laten verbeteren;'),
                ('li', None, 'de verwijdering van je persoonsgegevens te vragen, behoudens bepaalde wettelijke uitzonderingen.'),
            ]),
            ('Wijzigingen van dit beleid', [
                ('p', 'Wij kunnen dit privacybeleid van tijd tot tijd bijwerken. Elke wijziging wordt op deze pagina vermeld, '
                 'met de datum van bijwerking. Wij raden je aan deze pagina regelmatig te raadplegen.'),
            ]),
            ('Contact', [
                ('p', 'Heb je vragen of bedenkingen over ons privacybeleid? Neem dan contact met ons op via {email}.'),
                ('p', 'Bedankt voor je vertrouwen en je trouw.'),
            ]),
        ],
    },
    'en': {
        'title': 'Privacy policy',
        'lead': 'How your personal data is collected, used and protected on this website.',
        'sections': [
            ('Introduction', [
                ('p', 'Welcome to Guido De Oliveira’s website. Protecting your privacy is of the utmost importance to us. '
                 'This privacy policy describes how we collect, use and protect your personal information when you visit our '
                 'website and use our online shop.'),
            ]),
            ('Information we collect', [
                ('p', 'We collect several types of information to provide our services and improve your experience on our '
                 'website:'),
                ('li', 'Personal information', 'such as your name, email address, postal address and phone number when you '
                 'create an account or make a purchase.'),
                ('li', 'Payment information', 'credit card or other payment details are processed securely by our payment '
                 'partners.'),
                ('li', 'Usage information', 'data about your interaction with the website, including the pages you visit and '
                 'the products you view or add to your cart.'),
            ]),
            ('How we use your information', [
                ('p', 'We use your information to:'),
                ('li', None, 'process your orders and manage your account;'),
                ('li', None, 'improve our website and personalise your shopping experience;'),
                ('li', None, 'communicate with you about your orders, our products and our special offers;'),
                ('li', None, 'comply with our legal and regulatory obligations.'),
            ]),
            ('Newsletter', [
                ('p', 'If you subscribe to the newsletter, we keep your name and email address for the sole purpose of '
                 'sending it to you: new works, exhibitions and print releases. You can unsubscribe at any time by simply '
                 'writing to {email}; your address is then removed from the list.'),
            ]),
            ('Sharing your information', [
                ('p', 'We undertake not to sell, trade or rent your personal information to third parties. We may, however, '
                 'share your data with trusted partners in order to:'),
                ('li', None, 'process payments and deliver your orders;'),
                ('li', None, 'run our website and its related services;'),
                ('li', None, 'comply with legal obligations or protect our rights and those of our users.'),
            ]),
            ('Data security', [
                ('p', 'We take appropriate security measures to protect your information against unauthorised access, '
                 'disclosure, alteration or destruction. Our payment partners use encryption technology to secure your '
                 'financial transactions.'),
            ]),
            ('Cookies', [
                ('p', 'Our website uses cookies to improve your online experience. Cookies are small files stored on your '
                 'device that help us analyse web traffic and personalise content. You can disable cookies in your browser '
                 'settings, although this may affect how the website works.'),
            ]),
            ('Your rights', [
                ('p', 'You have the right to:'),
                ('li', None, 'access the personal information we hold about you;'),
                ('li', None, 'request the correction of inaccurate personal information;'),
                ('li', None, 'request the deletion of your personal information, subject to certain legal exceptions.'),
            ]),
            ('Changes to this policy', [
                ('p', 'We may update this privacy policy from time to time. Any change will be posted on this page together '
                 'with the date of the update. We encourage you to check this page regularly to stay informed.'),
            ]),
            ('Contact', [
                ('p', 'If you have any questions or concerns about our privacy policy, please contact us at {email}.'),
                ('p', 'Thank you for your trust and loyalty.'),
            ]),
        ],
    },
}
