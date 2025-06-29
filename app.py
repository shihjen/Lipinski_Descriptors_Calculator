# import libraries
import pandas as pd
import numpy as np
from io import StringIO
from rdkit import Chem
from rdkit.Chem import Descriptors, Lipinski
import streamlit as st

# helper function to compute Lipinski Descriptors
def lipinski(smiles, verbose=False):
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        #raise ValueError(f"Invalid SMILES string: {smiles}")
        return cal.write("Invalid SMILES String.")
    
    desc_MolWt = Descriptors.MolWt(mol)
    desc_MolLogP = Descriptors.MolLogP(mol)
    desc_NumHDonors = Lipinski.NumHDonors(mol)
    desc_NumHAcceptors = Lipinski.NumHAcceptors(mol)

    if verbose:
        cal.markdown(f"	:one: **Molecular Weight**: {desc_MolWt:.2f}")
        cal.markdown(f" :two: **Lipophilicity (LogP)**: {desc_MolLogP:.2f}")
        cal.markdown(f" :three: **Number of H-bond donors**: {desc_NumHDonors}")
        cal.markdown(f" :four: **Number of H-bond acceptors**: {desc_NumHAcceptors}")
        return " "
    else:
        return {"MolWt" : desc_MolWt,
                "MolLogP" : desc_MolLogP,
                "NumHDonors" : desc_NumHDonors,
                "NumHAcceptors" : desc_NumHAcceptors}

# Streamlit Interface Configuration
st.set_page_config(page_title = "Lipinski Descriptors Calculator",
                   page_icon = ":computer:",
                   layout = "wide")
st.sidebar.header("Section")
st.sidebar.markdown("[Lipinski's Rule of 5](#section-1)")
st.sidebar.markdown("[Single Compound Calculator](#section-2)")
st.sidebar.markdown("[Batch Calculator](#section-3)")
st.title("Lipinski Descriptors Calculator")


# Container: Background of Lipinski's Rule of 5
# Define custom CSS for the container
css = """
.st-key-my_blue_container {
    background-color: rgba(0, 61, 124, 0.1);
    border-radius: 10px;
    padding: 22px;
}
"""

content = """
**Dr. Christopher A. Lipinski**, a medicinal chemist and researcher at Pfizer, 
conceived the Rule of 5 in the mid-1990s out of a practical necessity to address the high attrition rate of promising drug candidates due to poor oral bioavailability. 
He systematically analyzed the physicochemical properties of compounds that had successfully progressed to later stages of clinical trials, 
rather than focusing solely on compounds with initial biological activity. By examining and plotting the data, 
Lipinski observed recurring patterns: successful oral drugs consistently exhibited molecular weights under 500 Daltons, no more than 5 hydrogen bond donors, 
no more than 10 hydrogen bond acceptors, and a Log P value not exceeding 5. 
This empirical observation, where the thresholds conveniently aligned with the number five or its multiples, 
led to the formulation of his influential "rule of thumb," 
which was subsequently adopted internally at Pfizer to flag potentially problematic compounds and later widely published in 1997.
"""

content2 = """
The rule states that poor absorption, permeation or distribution is more likely when a compound violates more than one of the following criteria:
"""

content3 = """
It's important to note that Lipinski's Rule of Five is a guideline, not an absolute rule. 
There are many exceptions, and some drugs that violate the rule are still orally bioavailable. Some limitations include:
"""

content4 = """
:x: **Active Transport:** The rule does not account for active transport mechanisms, which can facilitate the absorption of larger, more polar molecules.

:x: **Prodrugs:** The rule does not apply to prodrugs, which are inactive compounds that are converted into active drugs after administration.

:x: **Specific Chemical Classes:** The rule may not be applicable to certain classes of compounds, such as peptides and macrocycles.

:x: **Beyond Oral Bioavailability:** The rule primarily focuses on oral bioavailability and does not consider other aspects of drug development, such as toxicity, metabolism, and target affinity.
"""

content5 = """
Lipinski's Rule of Five is a valuable tool in the early stages of drug discovery. 
It helps medicinal chemists prioritize compounds that are more likely to be orally bioavailable, 
reducing the risk of wasting resources on compounds that are unlikely to succeed in clinical trials. 
By considering these parameters, researchers can design and select compounds with a higher probability of becoming successful drugs.
"""

rule1 = """
**Molecular weight greater than 500 Daltons:**
Larger molecules diffuse more slowly and have difficulty crossing cell membranes. 
The size of a molecule affects its ability to passively diffuse through the lipid bilayer of cell membranes. 
Larger molecules encounter greater resistance and require more energy to traverse the membrane.
"""

rule2 = """
**More than 5 hydrogen bond donors:**
These are typically nitrogen or oxygen atoms with one or more hydrogen atoms (e.g., -OH, -NH). 
A  high number of hydrogen bond donors increases the polarity of the molecule. 
While hydrogen bonding is essential for drug-target interactions, an excessive number of hydrogen bonds can reduce membrane permeability. 
Polar molecules tend to interact more strongly with water, which can hinder their ability to partition into the lipid-rich environment of cell membranes.
"""

rule3 = """
**More than 10 hydrogen bond acceptors:**
These are typically nitrogen or oxygen atoms (e.g., =O, -N-). 
Similar to hydrogen bond donors, a high number of hydrogen bond acceptors increases the polarity of the molecule. 
This increased polarity can reduce membrane permeability and hinder the compound's ability to cross cell membranes.
"""

rule4 = """
**Calculated Log P (CLogP) greater than 5:**
Log P is a measure of lipophilicity (fat-liking). 
A balance between lipophilicity and hydrophilicity is essential for good oral bioavailability. 
Highly lipophilic compounds (high Log P) may have poor aqueous solubility, which can limit their absorption from the gastrointestinal tract. 
They may also be sequestered in fatty tissues, reducing their bioavailability.
"""

st.html(f"<style>{css}</style>")
desc = st.container(key = "my_blue_container")
desc.header("Lipinski's Rule of 5", divider="blue", anchor="section-1")
desc.markdown(content)
desc.markdown(content2)

col11, col12, col13, col14 = desc.columns(spec=[0.1, 0.4, 0.1, 0.4], gap="medium")
col11.image("img/molecules.png")
col12.markdown(rule1)
col13.image("img/hydrogen.png")
col14.markdown(rule2)

col21, col22, col23, col24 = desc.columns(spec=[0.1, 0.4, 0.1, 0.4], gap="medium")
col21.image("img/oxygen.png")
col22.markdown(rule3)
col23.image("img/lipid.png")
col24.markdown(rule4)

desc.subheader("Exceptions & Limitations", divider="blue")
desc.write(content3)
desc.markdown(content4)

desc.subheader("Application In Drug Discovery", divider="blue")
desc.write(content5)

# Container: Calculator for Single Compound
# Define custom CSS for the container
css2 = """
.st-key-my_orange_container {
    background-color: rgba(239, 124, 0, 0.3);
    border-radius: 10px;
    padding: 10px;
}
"""

st.html(f"<style>{css2}</style>")
cal = st.container(key = "my_orange_container")
cal.header("Single Compound Calculator", divider="orange", anchor="section-2")

smiles = cal.text_input(label="Enter the Simplified Molecular Input Line Entry System (SMILES) String of A Compound.")

if smiles:
    res = lipinski(smiles, verbose=True)
    cal.write(res)



# Container: Calculator for Single Compound
# Define custom CSS for the container
css3 = """
.st-key-my_red_container {
    background-color: rgba(255, 0, 0, 0.3);
    border-radius: 10px;
    padding: 10px;
}
"""

instruction = """
Calculate the molecular weight, number of hydrogen bond donors, number of hydrogen bond acceptors, and lipophilicity for compounds in batch mode. 
Upload a CSV file containing the SMILES strings of the compounds to process. Please ensure the column with SMILES strings is labeled 'SMILES'.
"""

st.html(f"<style>{css3}</style>")
mul = st.container(key = "my_red_container")
mul.header("Batch Calculator", divider="red", anchor="section-3")
uploaded_file = mul.file_uploader(instruction, type=["csv"], accept_multiple_files=False)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    cont = []
    for smile in df["SMILES"]:
        lipinski_desc = lipinski(smile, verbose=False)
        cont.append(lipinski_desc)
        df_lipinski = pd.DataFrame(cont)
        df_lipinski = pd.concat([df['SMILES'], df_lipinski], axis=1)
    mul.dataframe(df_lipinski)
