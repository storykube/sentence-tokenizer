#!/usr/bin/python3
from sentence_tokenizer import SentenceTokenizer

s = SentenceTokenizer()

s = s.set("OVER 500,000. THAT was the number of people who have died from Covid-19 as of early March. " \
    "The pandemic continues stealing mothers, brothers, sisters, friends. So much loss is hard to grasp. Death is not a subject "\
    "we want to talk about, but the tragedy becomes worse when a loved one dies without a will or plans for burial, and familial "\
    "infighting begins as assets are divided and argued over. My father died suddenly at 39 years old, and it tore my family apart."
    "How are you today. But I have some problem (for real!). How are you S.Marco? And he told me \"How are you man? I need to listen. Ciao!\""
    )


print(s.get())



s = s.set("Elon Musk è cofondatore e CEO di un'azienda che produce auto elettriche. L'obiettivo dell'azienda dal 2003 "
          "è stato quello di accelerare la transizione globale dalle energie rinnovabili. La berlina-sella Model S è "
          "stata introdotta nel 2012 e il modello X SUV è stato lanciato nel 2015. La Model S è stata premiata come "
          "miglior auto in assoluto da Consumer Reports ed è stata nominata da Motor Trend come miglior veicolo "
          "dell'anno. Tesla produce anche tre prodotti per l'immagazzinamento dell'energia, tra cui una batteria "
          "domestica Powerwall e un megapack. L'azienda ha anche un nuovo modello chiamato cybertruck, "
          "che avrà caratteristiche migliori di un camion tradizionale. Il capo progettista di Tesla è responsabile "
          "di razzi e astronavi. Ha lavorato a missioni sulla terra e su altri pianeti. SpaceX ha completato il suo "
          "primo volo del razzo a combustibile liquido nel 2018. Il più grande razzo operativo del mondo, "
          "Falcon Heavy, ha terminato il suo primo volo. La prima versione della navicella spaziale Dragon che può "
          "trasportare equipaggio ha completato la sua prima missione dimostrativa nel 2019. Sulla base di questi "
          "risultati, SpaceX sta sviluppando Starship, un sistema di trasporto completamente riutilizzabile che "
          "porterà equipaggio e carico sulla Luna, su Marte e oltre. SpaceX sta perseguendo l'obiettivo a lungo "
          "termine di rendere gli esseri umani una specie multi-planetaria creando una città autosufficiente su "
          "Marte. Elon è anche CEO di Neuralink. Sta sviluppando interfacce cervello-macchina a banda ultra larga per "
          "collegare il cervello umano ai computer. The Boring Company combina una tecnologia di tunneling veloce ed "
          "economica con un sistema di trasporto pubblico completamente elettrico. L'azienda ha co-fondato zip2 e sta "
          "costruendo sistemi di trasporto pubblico. The Boring Company combina una tecnologia di tunneling veloce ed "
          "economica con un sistema di trasporto pubblico completamente elettrico. L'azienda ha co-fondato Zip2 e sta "
          "costruendo sistemi di trasporto pubblico.")

print(s.get())
