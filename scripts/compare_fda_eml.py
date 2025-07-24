import pandas as pd

# Load the FDA drug approval dataset
fda_df = pd.read_csv("data/fda_approved_drugs.csv")

# Get the top 50 most frequently approved generic names from the FDA dataset
top_fda = fda_df['generic_name'].dropna().str.lower().str.strip().value_counts().head(50)
top_fda_names = top_fda.index.tolist()
print(top_fda_names)
"""['clobetasol propionate', 'gabapentin', 'bupropion hydrochloride', 'triamcinolone acetonide', 'desipramine hydrochloride', 'fluocinolone acetonide', 'glycopyrrolate', 'sumatriptan', 'dimethyl fumarate', 'ondansetron', 'deflazacort', 'metronidazole', 'ibuprofen', 'aminocaproic acid', 'phenylephrine hydrochloride', 'naproxen sodium', 'heparin sodium', 'omeprazole', 'bortezomib', 'valproic acid', 'mycophenolate mofetil', 'darunavir', 'saxagliptin', 'voriconazole', 'carbinoxamine maleate', 'folic acid', 'carbidopa and levodopa', 'pregabalin', 'promethazine hydrochloride', 'dexmethylphenidate hydrochloride', 'methylphenidate hydrochloride', 'bupivacaine hydrochloride', 'everolimus', 'roflumilast', 'hydroxychloroquine sulfate', 'furosemide', 'trientine hydrochloride', 'bumetanide', 'ofloxacin', 'prednisone', 'solifenacin succinate', 'acitretin', 'milrinone lactate', 'allopurinol', 'colchicine', 'moxifloxacin hydrochloride', 'fluorouracil', 'betamethasone dipropionate', 'nicardipine hydrochloride', 'gemcitabine']
"""
# Load the WHO Essential Medicines List (EML)
import pandas as pd

eml_df = pd.read_csv("data/who_essential_medicines.csv")
print(eml_df.columns)

# Extract the medicine names from the WHO dataset, removing nulls and standardizing formatting
eml_names = eml_df['Medicine name'].dropna().str.lower().str.strip().unique()

# Dictionary to account for regional or synonymous naming differences between FDA and WHO
synonym_dict = {"acetaminophen": "paracetamol",
    "epinephrine": "adrenaline",
    "albuterol": "salbutamol",
    "oxacillin": "methicillin",
    "azithromycin dihydrate": "azithromycin"}

# Perform matching: compare the top FDA generic names with the WHO EML names
# (Note: synonym mapping is not applied here, as direct string comparison is used)
matched = [drug for drug in top_fda_names if drug in eml_names]

# Print the total number of matches and list the matched substances
print(f"\nOut of the top 50 FDA-approved active substances, {len(matched)} are included in the WHO Essential Medicines List.")
print("Matched substances:")
for m in matched:
    print("✅", m)

# Output example for reference:
"""✅ gabapentin
✅ sumatriptan
✅ ondansetron
✅ metronidazole
✅ ibuprofen
✅ heparin sodium
✅ omeprazole
✅ bortezomib
✅ darunavir
✅ voriconazole
✅ folic acid
✅ everolimus
✅ furosemide
✅ bumetanide
✅ ofloxacin
✅ prednisone
✅ allopurinol
✅ colchicine
✅ fluorouracil
✅ gemcitabine"""

# Print match rate as a percentage of the top 50 drugs
print(f"Match rate: {len(matched)/50:.0%}")
# Output:
# Match rate: 40%



