## Lipinski Descriptors Calculator

### 🟧 Lipinski's Rule of 5
**Dr. Christopher A. Lipinski**, a medicinal chemist and researcher at Pfizer, conceived the Rule of 5 in the mid-1990s out of a practical necessity to address the high attrition rate of promising drug candidates due to poor oral bioavailability. 
He systematically analyzed the physicochemical properties of compounds that had successfully progressed to later stages of clinical trials, rather than focusing solely on compounds with initial biological activity. By examining and plotting the data, 
Lipinski observed recurring patterns: successful oral drugs consistently exhibited molecular weights under 500 Daltons, no more than 5 hydrogen bond donors, no more than 10 hydrogen bond acceptors, and a Log P value not exceeding 5. 
This empirical observation, where the thresholds conveniently aligned with the number five or its multiples, led to the formulation of his influential "rule of thumb," 
which was subsequently adopted internally at Pfizer to flag potentially problematic compounds and later widely published in 1997.

The rule states that poor absorption, permeation or distribution is more likely when a compound violates more than one of the following criteria:

<table>
  <tr>
    <td>
      <img src="https://github.com/shihjen/Lipinski_Descriptors_Calculator/blob/main/img/molecules.png" width="100">
    </td>
    <td>
      <strong>Molecular weight greater than 500 Daltons</strong>: Larger molecules diffuse more slowly and have difficulty crossing cell membranes. 
      The size of a molecule affects its ability to passively diffuse through the lipid bilayer of cell membranes. Larger molecules encounter greater resistance and require more energy to traverse the membrane.
    </td>
  </tr>

  <tr>
    <td>
      <img src="https://github.com/shihjen/Lipinski_Descriptors_Calculator/blob/main/img/hydrogen.png" width="100">
    </td>
    <td>
      <strong>More than 5 hydrogen bond donors</strong>: These are typically nitrogen or oxygen atoms with one or more hydrogen atoms (e.g., -OH, -NH). 
      A high number of hydrogen bond donors increases the polarity of the molecule. While hydrogen bonding is essential for drug-target interactions, an excessive number of hydrogen bonds can reduce membrane permeability. 
      Polar molecules tend to interact more strongly with water, which can hinder their ability to partition into the lipid-rich environment of cell membranes.
    </td>
  </tr>

  <tr>
    <td>
      <img src="https://github.com/shihjen/Lipinski_Descriptors_Calculator/blob/main/img/oxygen.png" width="100">
    </td>
    <td>
      <strong>More than 10 hydrogen bond acceptors</strong>: These are typically nitrogen or oxygen atoms (e.g., =O, -N-). Similar to hydrogen bond donors, a high number of hydrogen bond acceptors increases the polarity of the molecule. 
      This increased polarity can reduce membrane permeability and hinder the compound's ability to cross cell membranes.
    </td>
  </tr>

  <tr>
    <td>
      <img src="https://github.com/shihjen/Lipinski_Descriptors_Calculator/blob/main/img/lipid.png" width="100">
    </td>
    <td>
      <strong>Calculated Log P (CLogP) greater than 5</strong>: Log P is a measure of lipophilicity (fat-liking). A balance between lipophilicity and hydrophilicity is essential for good oral bioavailability. 
      Highly lipophilic compounds (high Log P) may have poor aqueous solubility, which can limit their absorption from the gastrointestinal tract. They may also be sequestered in fatty tissues, reducing their bioavailability.
    </td>
  </tr>
  
</table>


### 🟧 Exceptions & Limitations
---

It's important to note that Lipinski's Rule of Five is a guideline, not an absolute rule. There are many exceptions, and some drugs that violate the rule are still orally bioavailable. Some limitations include:

:x: **Active Transport:** The rule does not account for active transport mechanisms, which can facilitate the absorption of larger, more polar molecules.

:x: **Prodrugs:** The rule does not apply to prodrugs, which are inactive compounds that are converted into active drugs after administration.

:x: **Specific Chemical Classes:** The rule may not be applicable to certain classes of compounds, such as peptides and macrocycles.

:x: **Beyond Oral Bioavailability:** The rule primarily focuses on oral bioavailability and does not consider other aspects of drug development, such as toxicity, metabolism, and target affinity.


### 🟧 Application In Drug Discovery
---

Lipinski's Rule of Five is a valuable tool in the early stages of drug discovery. 
It helps medicinal chemists prioritize compounds that are more likely to be orally bioavailable, 
reducing the risk of wasting resources on compounds that are unlikely to succeed in clinical trials. 
By considering these parameters, researchers can design and select compounds with a higher probability of becoming successful drugs.

### 🟧 Interactive Web Application with Streamlit
---

This project includes a Streamlit-based web application that allows users to interactively compute Lipinski's Rule of Five descriptors from SMILES strings — no coding required.

Users can:

1️⃣ Upload a .csv file containing SMILES data

2️⃣ Automatically compute key descriptors: molecular weight, H-bond donors, H-bond acceptors, and LogP

3️⃣ Download the processed results


### 🟧 Try It Out:
---
<div>⏩ <a href = "https://shihjen-lipinski-descriptors-calculator-app-fkay2n.streamlit.app/">Web Application</a></div>
