# DrugMatch: FDA vs WHO Essentials

### “How meaningful is FDA approval for global health?”

## Overview

This project investigates the intersection between pharmaceutical regulatory activity and global health priorities by comparing the top 50 most frequently approved drugs by the U.S. Food and Drug Administration (FDA) with the World Health Organization (WHO) Essential Medicines List (EML).

## Why This Matters

The FDA is a leading regulatory body whose decisions significantly influence pharmaceutical investment and market direction. However, regulatory approval alone does not guarantee a drug’s global health relevance. The WHO EML represents medications deemed essential for meeting the priority healthcare needs of populations worldwide. By analyzing the overlap between FDA’s most frequently approved drugs and WHO's essential list, we ask a critical question:

> **"To what extent do market-driven approvals reflect essential public health needs?"**

## Key Insight

🎯 **Only 40% of the top 50 FDA-approved drugs are listed on the WHO EML.**

This result suggests a partial but limited alignment between the regulatory focus of the FDA and WHO's global health priorities. While many drugs appear in both lists, a significant portion of frequently approved medications by the FDA are absent from the essential medicines list, possibly reflecting commercial priorities over public health needs.

## Data Sources

| File Name                     | Description                                 |
| ----------------------------- | ------------------------------------------- |
| `fda_approved_drugs.csv`      | Cleaned list of FDA-approved generic drugs  |
| `who_essential_medicines.csv` | Official WHO Essential Medicines List (EML) |

## Methodology

1. Extract top 50 most frequent generic names from the FDA dataset  
2. Standardize and clean both FDA and WHO drug names  
3. Perform direct string-based matching between the two lists  
4. Calculate match rate and output matched drugs  
5. Create a manual synonym dictionary to account for regional naming differences (e.g., “acetaminophen” vs. “paracetamol”) and optionally normalize names accordingly for more accurate comparison


## Results

* **Matched drugs:** 20 out of 50
* **Match rate:** 40%

### Matched Drugs

```
gabapentin
sumatriptan
ondansetron
metronidazole
ibuprofen
heparin sodium
omeprazole
bortezomib
darunavir
voriconazole
folic acid
everolimus
furosemide
bumetanide
ofloxacin
prednisone
allopurinol
colchicine
fluorouracil
gemcitabine
```

## Interpretation

This analysis reveals that only 40% of the most frequently approved drugs by the FDA are aligned with WHO’s Essential Medicines List. While this suggests some overlap between regulatory approvals and public health needs, the significant gap highlights how regulatory priorities—driven by innovation and market dynamics—may not always match the essential needs of global health systems.

## 🧠 Interpretation & Context
This analysis reveals that only 40% of the most frequently approved drugs by the FDA are also considered essential by the World Health Organization. While this partial overlap suggests that some regulatory priorities do align with global health needs, the limited match highlights a critical gap.

FDA approvals are often influenced by innovation, market demands, and profitability, whereas the WHO Essential Medicines List is grounded in criteria like population-level impact, cost-effectiveness, and accessibility—especially in low- and middle-income countries. The fact that a majority of FDA top drugs do not appear on the EML may indicate that global health priorities are underrepresented in high-income regulatory systems.

This finding raises a broader question:

To what extent does pharmaceutical regulation reflect global public health priorities rather than commercial interests?

By drawing attention to this misalignment, the project encourages reflection on how medicine approval pipelines can better serve global needs—not just local or economic incentives.

## Limitations

* Analysis is limited to generic name matching (no form/dose normalization)
* No time-based trend analysis was conducted
* Synonyms were only partially accounted for manually
* Therapeutic class or usage data not included

## Future Work

* Add approval data from EMA, Health Canada, and other agencies
* Explore temporal trends: how has the overlap changed over time?
* Include WHO country-level medicine availability data
* Expand synonym normalization with NLP or fuzzy string matching

## Project Structure

```
project/
├── data/
│   ├── fda_approved_drugs.csv
│   └── who_essential_medicines.csv
├── outputs/
│   └── matched_drugs.txt
├── scripts/
│   └── compare_fda_eml.py
└── README.md
```


## License

This project is open-source and available under the MIT License.

