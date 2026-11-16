# Bumle Business – VPN-logovervågning

## 1. Introduktion

Bumle Business er en virksomhed, der bruger VPN til at oprette sikre forbindelser til deres servere. Virksomheden har oplevet mistænkelig aktivitet og har derfor brug for en måde at undersøge, hvad der sker på deres servere.

I dette projekt har jeg lavet et Python-program, der kan indlæse og analysere logdata. Formålet er at gøre det nemmere at få overblik over de forskellige hændelser og finde frem til aktiviteter, der virker mistænkelige.

Programmet indlæser en logfil med 541 registreringer, som bliver vist i en tabel. Derudover har jeg brugt Pandas og Matplotlib til at lave forskellige diagrammer, så man nemmere kan se mønstre i dataene. Det kan for eksempel være mange mislykkede loginforsøg på kort tid eller malware-alarmer fra bestemte IP-adresser.

Jeg har også delt koden op i flere Python-filer, så den er mere overskuelig, og så funktionerne kan bruges flere steder. Derudover har jeg lavet fejlhåndtering, så programmet kan give en besked, hvis logfilen mangler eller indeholder linjer med forkert format.
### Sådan bruges programmet

For at køre programmet skal man have Python installeret samt bibliotekerne Pandas og Matplotlib. De kan installeres i terminalen med:

pip install pandas matplotlib

Derefter åbner man projektet i PyCharm og kører filen main.py.

Programmet indlæser automatisk logfilen og viser en oversigt over logdataene i terminalen.

Herefter åbnes seks diagrammer i denne rækkefølge:

Scatter-plot: IP-adresser og tidspunkter.

Loginforsøg: Antal mislykkede loginforsøg pr. time.

Malware: Antal malware-alarmer pr. IP-adresse.

Sikkerhedsniveauer: Fordeling af INFO, WARN og ALERT.

IP-adresser: De 10 mest aktive IP-adresser.

Hændelsestyper: Fordeling af de forskellige hændelser.

Diagrammerne åbnes ét ad gangen. Når man lukker et diagramvindue, åbner det næste automatisk.

Når alle seks diagrammer er lukket, afsluttes programmet.
## 2. SCRUM

Jeg har brugt SCRUM til at planlægge og holde styr på mit projekt. SCRUM er en arbejdsmetode, hvor man deler et projekt op i mindre opgaver, så det bliver nemmere at overskue, hvad der skal laves.

Jeg har planlagt projektet i ét sprint og brugt Scrumwise til at holde styr på mine opgaver og følge med i, hvor langt jeg er nået.

### User Stories

Jeg har lavet seks User Stories, som beskriver de funktioner, programmet skal have, ud fra brugerens behov.

En User Story beskriver, hvad brugeren gerne vil kunne gøre med programmet, og hvorfor funktionen er vigtig.

Et eksempel fra mit projekt er:

*"Som IT-chef hos Bumle Business vil jeg se de vigtigste fund i et tydeligt diagram, så jeg kan forstå, hvad der er sket, uden at kende de rå data."*

User Stories har hjulpet mig med at holde fokus på, hvad programmet skal kunne, i stedet for bare at begynde at programmere uden en plan.
### Tasks

Jeg har delt mine User Stories op i mindre opgaver, som kaldes Tasks. Det har gjort det nemmere for mig at arbejde med projektet, fordi jeg kunne fokusere på én opgave ad gangen.

Hver Task hører til en bestemt User Story og beskriver, hvad jeg konkret skal lave for at få funktionen til at virke.

Et eksempel er User Story 4, hvor jeg havde disse tre Tasks:

- **T10:** Find de vigtigste fund i logdataene.
- **T11:** Lav en genbrugelig funktion til søjlediagrammer.
- **T12:** Vis diagrammet i `main.py`, og test, at det virker.

Når jeg var færdig med en Task, opdaterede jeg dens status i Scrumwise, så jeg hele tiden kunne følge med i, hvor langt jeg var nået.
### Acceptkriterier

Til hver User Story har jeg lavet nogle acceptkriterier. Det er krav, som skal være opfyldt, før jeg kan sige, at en User Story er færdig.

Jeg har brugt acceptkriterierne til at teste, om mine funktioner virker, som de skal, og om jeg har fået lavet det, der var planlagt.

Et eksempel er User Story 6, som handler om fejlhåndtering. Her havde jeg følgende acceptkriterier:

- Hvis logfilen mangler, skal programmet vise en tydelig fejlbesked.
- Hvis en loglinje har forkert format, skal den springes over med en advarsel.
- Programmet skal kunne fortsætte efter en advarsel.

Jeg testede blandt andet dette ved at lave en testfil med en korrekt og en forkert loglinje. Programmet viste en advarsel og indlæste kun den korrekte linje.

På den måde kunne jeg kontrollere, at kravene var opfyldt, inden jeg afsluttede User Storyen.
### Task Board

Jeg har brugt Scrumwise som mit Task Board til at holde styr på opgaverne i projektet.

På boardet har jeg opdelt opgaverne i forskellige statusser som *To Do*, *In Progress*, *To Test* og *Done*. På den måde har jeg kunnet se, hvilke opgaver jeg manglede, hvilke jeg var i gang med, og hvilke der var færdige.

Undervejs har jeg flyttet mine Tasks mellem de forskellige statusser, efterhånden som jeg arbejdede på dem. Når en opgave var programmeret og testet, flyttede jeg den til Done.

Det har hjulpet mig med at holde overblik over projektet og arbejde mere struktureret, selvom jeg har lavet projektet alene.
### Sammenhængen mellem SCRUM-elementerne

De forskellige dele af SCRUM hænger sammen. Mine User Stories beskriver, hvad programmet skal kunne, og hver User Story er delt op i mindre Tasks, som fortæller, hvad jeg konkret skal lave.

Acceptkriterierne bruger jeg til at kontrollere, om funktionerne virker, som de skal. På mit Task Board i Scrumwise kan jeg følge med i, hvor langt jeg er nået med opgaverne.

På den måde har jeg kunnet arbejde med én opgave ad gangen og holde styr på hele projektet.
## 3. Konklusion

I projektet har jeg lavet et Python-program, der kan indlæse og analysere logdata fra Bumle Business. Ved hjælp af tabeller og diagrammer har jeg fået et bedre overblik over sikkerhedshændelserne og fundet nogle mistænkelige aktiviteter.

Jeg analyserede i alt 541 logregistreringer og fandt blandt andet:
- 105 mislykkede loginforsøg, hvor 18 kom fra samme IP-adresse inden for få minutter. Det kan være tegn på et brute force-angreb.
- 17 malware-alarmer, hvor tre kom fra samme IP-adresse og var rettet mod tre forskellige servere.
- 59 sikkerhedsalarmer (ALERT) og 170 advarsler (WARN).
- 27 portscanninger og 15 forsøg på at opnå højere adgangsrettigheder.
- Mistænkelige IP-adresser, hvor nogle havde mange registreringer, mens andre havde usædvanlig aktivitet inden for kort tid.
Analysen viste mig, at det ikke kun handler om antallet af hændelser, men også om, hvornår de sker, og hvilke servere der bliver påvirket. Hændelserne kan være tegn på angreb, men beviser ikke, at nogen har fået adgang.

En forbedring kunne være at lave en menu, hvor man selv kan vælge diagrammer, eller få programmet til automatisk at opdage mistænkelig aktivitet.

Jeg har brugt GitHub til at gemme min kode og holde styr på ændringerne undervejs.

Jeg har selvfølgelig også fået oprettet den meget vigtige YAML-fil med teksten "Bøf med bløde løg, brun sovs og kartofler." Hvad den har med VPN-sikkerhed at gøre, er stadig et mysterium, men kravet er opfyldt.