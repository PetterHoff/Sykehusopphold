from flask import Flask, request, render_template
from waitress import serve
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)

# Load model
model_path = "model.pkl"
model = pickle.load(open(model_path, 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    
    features_form =  dict(request.form)

    features = {}

    for variabel, verdi in features_form.items():

        if variabel == "kreft":
            if verdi == "Ja":
                features["kreft_yes"] = 1
                features["kreft_no"] = 0
                features["sykdomskategori_Cancer"] = 1
            else:
                features["kreft_no"] = 1
                features["kreft_yes"] = 0
                features["sykdomskategori_Cancer"] = 0

        if variabel == "kjønn":
            if verdi == "Mann":
                features["kjønn_male"] = 1
            else:
                features["kjønn_male"] = 0
    
        if variabel == "sykdom_underkategori_CHF":
            if verdi == "Ja":
                features["sykdom_underkategori_CHF"] = 1
            else:
                features["sykdom_underkategori_CHF"] = 0
        
        if variabel == "etnisitet":
            if verdi == "Hvit":
                features["etnisitet_white"] = 1
            else:
                features["etnisitet_white"] = 0
   
        if variabel == "diabetes":
            if verdi == "Ja":
                features["diabetes"] = 1
            else:
                features["diabetes"] = 0

        if variabel == "demens":
            if verdi == "Ja":
                features["demens"] = 1
            else:
                features["demens"] = 0

        if variabel == "inntekt":
            if verdi == "mangler":
                features["inntekt_mangler"] = 1
                features["inntekt_$25-$50k"] = 0
                features["inntekt_>$50k"] = 0
                features["inntekt_under $11k"] = 0
            elif verdi == "25-50k":
                features["inntekt_mangler"] = 0
                features["inntekt_$25-$50k"] = 1
                features["inntekt_>$50k"] = 0
                features["inntekt_under $11k"] = 0
            elif verdi == "over_50k":
                features["inntekt_mangler"] = 0
                features["inntekt_$25-$50k"] = 0
                features["inntekt_>$50k"] = 1
                features["inntekt_under $11k"] = 0
            elif verdi == "under_11k":
                features["inntekt_mangler"] = 0
                features["inntekt_$25-$50k"] = 0
                features["inntekt_>$50k"] = 0
                features["inntekt_under $11k"] = 1

        if variabel == "sykdom_underkategori_COPD":
            if verdi == "Ja":
                features["sykdom_underkategori_COPD"] = 1
            else:
                features["sykdom_underkategori_COPD"] = 0

        if variabel == "sykdom_underkategori_Cirrhosis":
            if verdi == "Ja":
                features["sykdom_underkategori_Cirrhosis"] = 1
            else:
                features["sykdom_underkategori_Cirrhosis"] = 0

        if variabel == "sykdom_underkategori_Colon_Cancer":
            if verdi == "Ja":
                features["sykdom_underkategori_Colon Cancer"] = 1
            else:
                features["sykdom_underkategori_Colon Cancer"] = 0

        if variabel == "sykdom_underkategori_Coma":
            if verdi == "Ja":
                features["sykdom_underkategori_Coma"] = 1
            else:
                features["sykdom_underkategori_Coma"] = 0

        if variabel == "sykdom_underkategori_Lung_Cancer":
            if verdi == "Ja":
                features["sykdom_underkategori_Lung Cancer"] = 1
            else:
                features["sykdom_underkategori_Lung Cancer"] = 0

        if variabel == "sykdom_underkategori_MOSF w/Malig":
            if verdi == "Ja":
                features["sykdom_underkategori_MOSF w/Malig"] = 1
            else:
                features["sykdom_underkategori_MOSF w/Malig"] = 0

        if variabel == "sykdomskategori_COPD/CHF/Cirrhosis":
            if verdi == "Ja":
                features["sykdomskategori_COPD/CHF/Cirrhosis"] = 1
            else:
                features["sykdomskategori_COPD/CHF/Cirrhosis"] = 0

        if variabel == "sykdomskategori_Coma":
            if verdi == "Ja":
                features["sykdomskategori_Coma"] = 1
            else:
                features["sykdomskategori_Coma"] = 0
    
    
    features["sykdomskategori_Coma"] = 0
    features["alder"] = int(features_form["alder"])
    features["utdanning"] = int(features_form["utdanning"])
    features["blodtrykk"] = int(features_form["blodtrykk"])
    features["hvite_blodlegemer"] = int(features_form["hvite_blodlegemer"])
    features["hjertefrekvens"] = int(features_form["hjertefrekvens"])
    features["respirasjonsfrekvens"] = int(features_form["respirasjonsfrekvens"])
    features["kroppstemperatur"] = int(features_form["kroppstemperatur"])
    features["lungefunksjon"] = int(features_form["lungefunksjon"])
    features["serumalbumin"] = int(features_form["serumalbumin"])
    features["kreatinin"] = int(features_form["kreatinin"])
    features["natrium"] = int(features_form["natrium"])
    features["blod_ph"] = int(features_form["blod_ph"])
    features["blodurea_nitrogen"] = int(features_form["blodurea_nitrogen"])
    features["urinmengde"] = int(features_form["urinmengde"])
    features["antall_komorbiditeter"] = int(features_form["antall_komorbiditeter"])
    features["koma_score"] = int(features_form["koma_score"])
    features["fysiologisk_score"] = int(features_form["fysiologisk_score"])
    features["apache_fysiologisk_score"] = int(features_form["apache_fysiologisk_score"])
    features["overlevelsesestimat_2mnd"] = int(features_form["overlevelsesestimat_2mnd"])
    features["overlevelsesestimat_6mnd"] = int(features_form["overlevelsesestimat_6mnd"])
    features["lege_overlevelsesestimat_2mnd"] = int(features_form["lege_overlevelsesestimat_2mnd"])
    features["lege_overlevelsesestimat_6mnd"] = int(features_form["lege_overlevelsesestimat_6mnd"])
    features["adl"] = int(features_form["adl"])
    features["adl_endring"] = 0


    features = {k: features[k] for k in [
        "alder", "utdanning", "blodtrykk", "hvite_blodlegemer", "hjertefrekvens", "respirasjonsfrekvens", 
        "kroppstemperatur", "lungefunksjon", "serumalbumin", "kreatinin", "natrium", "blod_ph", 
        "blodurea_nitrogen", "urinmengde", "antall_komorbiditeter", "koma_score", "fysiologisk_score", 
        "apache_fysiologisk_score", "overlevelsesestimat_2mnd", "overlevelsesestimat_6mnd", "diabetes", 
        "demens", "lege_overlevelsesestimat_2mnd", "lege_overlevelsesestimat_6mnd", "adl", "adl_endring", 
        "inntekt_mangler", "inntekt_$25-$50k", "inntekt_>$50k", "inntekt_under $11k", "kjønn_male", 
        "sykdom_underkategori_CHF", "sykdom_underkategori_COPD", "sykdom_underkategori_Cirrhosis", 
        "sykdom_underkategori_Colon Cancer", "sykdom_underkategori_Coma", "sykdom_underkategori_Lung Cancer", 
        "sykdom_underkategori_MOSF w/Malig", "sykdomskategori_COPD/CHF/Cirrhosis", "sykdomskategori_Cancer", 
        "sykdomskategori_Coma", "kreft_no", "kreft_yes", "etnisitet_white"
    ]}


    features = pd.DataFrame(features, index=[0])

    prediction = model.predict(features)

    return render_template('index.html', prediction_text='Det predikerte sykehusoppholdet for pasienten er: {} dager'.format(prediction[0]))
    

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)
