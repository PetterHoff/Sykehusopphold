
**Prediksjon av sykehusopphold basert på pasientdata**

## Innhold

* [Om prosjektet](#om-prosjektet)
* [Forutsetninger](#forutsetninger)
* [Installasjon](#installasjon)
* [Kjøre prosjektet](#kjøre-prosjektet)

  * [Trene / modellgenerering](#trene--modellgenerering)
  * [Nettside / applikasjon](#nettside--applikasjon)
* [Data](#data)
* [Filstruktur](#filstruktur)
* [Hvordan bruke applikasjonen](#hvordan-bruke-applikasjonen)
* [Resultater / output](#resultater--output)
* [Avhengigheter / biblioteker](#avhengigheter--biblioteker)
* [Kontakt / videre arbeid](#kontakt--videre-arbeid)

---

## Om prosjektet

Dette prosjektet har som mål å **predikere sykehusopphold** for pasienter basert på historiske pasientdata.
Ved hjelp av maskinlæring trenes en modell som estimerer hvorvidt og eventuelt hvor lenge en pasient vil være innlagt, gitt data om pasienten.

Detaljert dokumentasjon og analyser finnes i `Rapport.pdf` og `prosjektbeskrivelse.pdf`.

---

## Forutsetninger

Før du kjører programmet må du ha:

* `Python` installert (anbefalt 3.8 eller nyere)
* Datasettfilene:

  * `raw_data/` katalog
  * `sample_data/` katalog

---

## Installasjon

1. Klon eller last ned repository:

   ```bash
   git clone https://github.com/PetterHoff/Sykehusopphold.git
   cd Sykehusopphold
   ```

2. Opprett et virtuelt miljø (anbefalt) og aktiver det:

   ```bash
   python -m venv venv
   source venv/bin/activate   # på Linux / macOS
   venv\Scripts\activate      # på Windows
   ```

3. Installer nødvendige pakker:

   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Kjøre prosjektet

### Trene / modellgenerering

* Åpne `Main.ipynb` i Jupyter Notebook eller VS Code
* Pass på at mappene `raw_data/` og `sample_data/` ligger i prosjektmappen
* Trykk på **Run All** for å kjøre alle celler
* Da vil følgende filer bli laget:

  | Fil               | Innhold                       |
  | ----------------- | ----------------------------- |
  | `modell.pkl`      | Den ferdig trente modellen    |
  | `predictions.csv` | Prediksjoner på `sample_data` |
  | `X_train.csv`     | Treningsdata lagret som CSV   |

---

### Nettside / applikasjon

* Start webapplikasjonen ved å kjøre:

  ```bash
  python app.py
  ```
* Åpne nettleser på: [http://localhost:8080](http://localhost:8080)
* HTML-malen ligger i `templates/`-mappen

---

## Data

* `raw_data/`: Rådata brukt for å trene modellen
* `sample_data/`: Eksempeldata som modellen kan predikere på

---

## Filstruktur

```
Sykehusopphold/
├── raw_data/          
├── sample_data/       
├── templates/         
├── Main.ipynb         
├── app.py             
├── model.pkl          
├── predictions.csv    
├── X_train.csv        
├── Rapport.pdf        
├── prosjektbeskrivelse.pdf
└── README.md           
```

---

## Hvordan bruke applikasjonen

1. Sørg for at `modell.pkl` er generert ved å kjøre `Main.ipynb`
2. Start webapplikasjonen med `app.py`
3. Fyll ut alle feltene i skjemaet på nettsiden
4. Trykk **Send inn**
5. Prediksjonen vises nederst på siden

---

## Resultater / output

Når alt er kjørt vil du ha:

* `modell.pkl` – lagret modell som kan brukes på nye data
* `predictions.csv` – prediksjoner på `sample_data`
* `X_train.csv` – treningsdata i CSV-format
* Webapplikasjon som viser prediksjon direkte i nettleseren

---

## Avhengigheter / biblioteker

Prosjektet bruker blant annet:

```
numpy
pandas
plotly
scikit-learn
seaborn
matplotlib
flask
joblib
waitress
nbformat
ipython
jupyter
```

Installer gjerne via:

```bash
pip install -r requirements.txt
```

---

