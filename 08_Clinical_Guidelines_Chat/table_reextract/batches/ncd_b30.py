exec(open('batches/ncd_common.py').read())
IH = CH3 + " > Ischemic Heart Disease"
ITEMS = [
 D("fig-chest-pain-approach", 124, IH + " > Approach to Patient with Chest Pain",
   "Approach to the patient with chest pain (flowchart: ACS, STEMI/NSTEMI/unstable angina, pericarditis, pneumothorax, pneumonia, aortic dissection, pulmonary embolism)", ["0344"],
   "1. Initial assessment with vitals (BP, all peripheral pulses, RR, temperature, JVP, SpO2) and physical examination (CVS, respiratory system, GIS).\n"
   "   - Hemodynamically unstable: stabilize and immediately assess for STEMI, aortic dissection, massive pulmonary embolism, pericardial tamponade.\n"
   "   - Hemodynamically stable: evaluate the causes of chest pain.\n"
   "2. Obtain a 12-lead ECG, echo and CXR (all patients).\n"
   "3. ECG diagnostic or suggestive of ACS? YES → Does the patient have typical or atypical angina pattern, radiation, diaphoresis, cardiac risk factors?\n"
   "   - ST elevation → STEMI.\n"
   "   - ST depression and/or T wave inversion → check cardiac markers (troponin, CK-MB) at baseline and repeat at 6 hrs:\n"
   "     - Suggestive history, positive cardiac enzymes and ECG changes = NSTEMI.\n"
   "     - Cardiac markers negative, new onset, crescendo or rest angina = unstable angina.\n"
   "   - Pericarditis.\n"
   "4. History and ECG suggestive of ACS? NO → X-ray chest or echo:\n"
   "   - X-ray chest: area of lucency in lung parenchyma and chest wall → pneumothorax; infiltrate (with history and labs consistent with infection) → pneumonia.\n"
   "   - Widened mediastinum (and history consistent with aortic dissection) and flap on echo → refer for dedicated imaging (CT aortogram): aortic dissection.\n"
   "5. Assess risk for pulmonary embolism:\n"
   "   - Low risk: send D-dimer, X-ray evaluation. Elevated D-dimer, or echo showing dilated RA/RV or McConnell sign → high risk.\n"
   "   - High risk for pulmonary embolism (D-dimer elevated): refer for CT pulmonary angiogram to rule out PE.\n"
   "6. If ECG, X-ray, cardiac markers and echo are normal: rule out other causes of chest pain based on history and available investigations. Patients with nonspecific chest pain, no ECG changes at presentation and at discharge from emergency, and normal cardiac enzymes can be discharged and followed up in OPD.",
   ["'angina pattern1' has a footnote marker with no footnote printed.", "'Tropinin', 'Mcconel' printed."]),
]
